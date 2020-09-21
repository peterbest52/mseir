# Introduction

In the early development of COVID-19, large-scale preventive measures, such as border control and air travel restrictions, were implemented to slow international and domestic transmissions. When these measures were in full effect, new cases of infection would be primarily induced by community spread, such as the human interaction within and between neighboring cities and towns, which is generally known as the meso-scale. Existing studies of COVID-19 using mathematical models are unable to accommodate the need for meso-scale modeling, because of the unavailability of COVID-19 data at this scale and the different timings of local intervention policies. In this respect, we propose a meso-scale mathematical model of COVID-19, named **the meso-scale Susceptible, Exposed, Infectious, Recovered (MSEIR) model**, using town-level infection data in the state of Connecticut. We consider the spatial interaction in terms of the inter-town travel in the model. Based on the developed model, we evaluated how different strengths of social distancing policy enforcement may impact future epidemic curves based on two evaluative metrics: compliance and containment. The developed model and the simulation results will establish the foundation for community-level assessment and better preparedness for COVID-19.

**MSEIR** represents Meso-scale Susceptible, Exposed, Infectious, Recovered model. The meso-scale, generally known as a study area of 1–1000 kilometers, is of critical importance in the effective containment of the epidemic growth. The MSEIR model is developed to simulate the cases of COVID-19 infection at the town-level. 

# MSEIR Data and Codes 

The data and codes can be accessed on this Github repo.

## Data

*data.csv* is the raw data. It is the Connecticut COVID-19 cumulative cases of infection on the town level (March 23-Sep 7, 2020).
The data is derived from the CT Coronavirus daily report [https://portal.ct.gov/coronavirus]. The raw data is only for exploratory purposes. The equivalent COVID-19 data for running the codes is *reported511.csv*.

*Mij.csv* contains the mobility variable (i.e., trips between towns) for the model, including:

### *Model 1*: Mij_10%_20mi
### *Model 2*: Mij_10%_60mi
### *Model 3*: Mij_10%_140mi
### *Model 4*: Mij_30%_20mi
### *Model 5*: Mij_30%_60mi
### *Model 6*: Mij_30%_140mi
### *Model 7*: Mij_50%_20mi
### *Model 8*: Mij_50%_60mi
### *Model 9*: Mij_50%_140mi
### *Model R*: Mij_R

## Codes

Two Python codes are developed for the MSEIR model.

*Mij_calculation.py* derives the M_ij by the Huff model, generating the related mobility variables in *Mij.csv*.

*runmodel.py* is the main code for model fitting and simulation. It may take a few hours to derive the full results. 

Additional packages required: *SciPy* and *scikit-learn* are needed. The packages can be installed using *pip* or *conda*.

**Inputs:** Input data for running *runmodel.py* include the population and daily confirmed cases (filename: *reported511.csv*) and the estimated M_ij of each model (filename: *Mij.csv*; the file is derived by running *Mij_calculation.py*). Please change the reading and writing file paths to your own local directory, when running the codes.

**Outputs:** The outputs of *runmodel.py* is a csv file including daily cumulative cases of infection for each town, statistics (r-squared and RMSE), and estimated parameters for each MSEIR model. The simulated daily cases up to July 12, 2020 are stored in the dictionary *estall* but are not written in the local directory. 

We have also genereted case simulation by Model 7 and Model R with an end date of 12/31/2020, as shown in *result1231.csv*.
