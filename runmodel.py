# -*- coding: utf-8 -*-
"""
Created on Fri May 29 10:53:46 2020

@author: Administrator
"""
################ RUN ALL MODEL FITTINGS ############
import scipy.optimize as optimize
import pandas as pd
import numpy as np
import functions
import scipy.stats as stats
import math
from sklearn.metrics import mean_squared_error


# read data
towns=pd.read_csv("....\\reported511.csv")
Mij=pd.read_csv("....\\Mijnew.csv")

estall={}
for ii in range(10):
    
    # For model 0 (no intertown travel), M=0
    if(ii==0):
        M=0
    # for model 1-9, read-in M 
    if(ii!=0):    
        mod = pd.pivot_table(Mij, values=Mij.columns[10+ii], index=['i'],columns=['j'])
        M=np.array(mod)
    
    # get confirmed cases 
    data=np.array(towns.iloc[:,4:54])
    # set time period for model simulation
    times=np.arange(1.0,np.shape(data)[1]+1)
    times=np.array(times)
    # get population of each city
    N = np.array(towns['Pop2018'].astype(float))
    
    ## initialization of estimated parameters
    E0list=np.zeros(len(towns))
    E0list=E0list+N/100000  
    params=[1.0]+list(E0list)+[0.1]
    params=np.array(params)

    ## run model fitting by minimazing NLL by Nelder-Mead algorithm
    optimizer = optimize.minimize(functions.NLL, params,args=(data,times,np.array(M),towns), method='Nelder-Mead')
    # estimated parameters
    paramests = np.abs(optimizer.x)
    
    # model simulation output
    #  predict the next 60 days 
    esttimes=np.arange(1,113)
    res = functions.model(functions.ini(paramests,towns), esttimes, paramests,np.array(M),towns)
    # cumulative infected cases
    est=(res[:,3,:]+res[:,4,:]).T
    # store simulated infected cases for each model 
    estall[ii]=est

    # calculate r-squared, rmse and relative rmse 
    r2=[]
    rmse=[]
    rrmse=[]

    for i in range(len(towns)):
        x=data[i]
        y=est[i][0:50]
        slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
        r2i=r_value**2    
        rmse.append(math.sqrt(mean_squared_error(x, y)))
        r2.append(r2i)
        rrmse.append(math.sqrt(mean_squared_error(x, y))/np.mean(y))
    
    # store parameters and statistics      
    towns['mod'+str(ii)+'r2']=r2
    towns['mod'+str(ii)+'rmse']=rmse
    towns['mod'+str(ii)+'rrmse']=rrmse
    towns['mod'+str(ii)+'E0']=paramests[1:-1]
    towns['mod'+str(ii)+'beta']=paramests[0]
    towns['mod'+str(ii)+'a']=paramests[-1]

## store result
towns.to_csv("D://USERS//AAA//result.csv",encoding='utf_8_sig',index=True, header=True)



####### RUN MODEL PREDICTIONS USING ESTIMATED PARAMETERS #####
estall={}
rms=[]
rrms=[]
for ii in range(10):

    # For model 0 (no intertown travel), M=0
    if(ii==0):
        M=0
    # for model 1-9, read-in M 
    if(ii!=0):    
        mod = pd.pivot_table(Mij, values=Mij.columns[10+ii], index=['i'],columns=['j'])
        M=np.array(mod)
    
    
    beta=towns['mod'+str(ii)+'beta'][1]
    E0=towns['mod'+str(ii)+'E0']
    a=towns['mod'+str(ii)+'a'][1]
    paramests = [beta]+list(E0)+[a]
    paramests=np.array(paramests)
    times=np.arange(1,113)
    res = functions.model(functions.ini(paramests,towns), times, paramests,M,towns)
    est=(res[:,3,:]+res[:,4,:]).T
    estall[ii]=est
    
    towns['7.12premodel'+str(ii)]=estall[ii][:,-1]
