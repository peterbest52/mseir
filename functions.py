# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:42:41 2020

@author: Administrator
"""
from scipy.stats import norm
from scipy.stats import poisson
import numpy as np



## the meso-scale SEIR model considering intertown mobility, for the no interaction model, set M=0
def model(Y, times, params,M,towns):


    S, E, I, R,beta2,N = Y
    
    # daily decay rate of beta
    a=params[-1]
    
    gamma=1/(9.1)
    sigma=1/(5.2)


    res=np.zeros((len(times),7,len(towns)))

    for d in times:
        
        i=int(d)-1
        
        res[i,0,:]=beta2
        res[i,1,:]=S
        res[i,2,:]=E
        res[i,3,:]=I
        res[i,4,:]=R
        res[i,5,:]=N
        
        
        beta2_ = beta2-beta2*a
        dS=- beta2 *  S * I / N - np.sum((M*(S/(N-I-R))[:,np.newaxis])*beta2*I/N,axis=1)
        dE= beta2* S *I/N -sigma*E +np.sum((M*(S/(N-I-R))[:,np.newaxis])*beta2*I/N,axis=1)
        dR=gamma * I
        S_ = S + dS
        E_ = E + dE
        I_ = I + sigma*E - gamma * I 
        R_ = R + dR
        N_ = N 
        
        beta2=beta2_
        S=S_
        E=E_
        I=I_
        R=R_
        N=N_
    
        
    return res

# initial state of SEIR
def ini(params,towns):

    S0 = towns['Pop2018'].astype(float)-params[1:(len(towns)+1)]
    I0 = np.zeros(len(S0))
    I0[I0==0] =  towns['Case0323']

    E=np.zeros(len(S0))
    E[E==0]=params[1:(len(S0)+1)]

    R0 = np.zeros(len(S0))
    N = np.array(towns['Pop2018'].astype(float))

    beta2=np.zeros(len(S0))
    beta2[beta2==0]=params[0]
    X0 = [np.array(S0), E, I0, R0, beta2,N]

    return X0

# cost function, 
def NLL(params,data,times,M,towns):

    params = np.abs(params)
    data = np.array(data)
    res=model(ini(params,towns), times, params,M,towns)

    y = (res[:,3,:]+res[:,4,:]).T
    y=np.array(y)

    nll = -np.sum(norm.logpdf(data, loc=y))

    return nll


