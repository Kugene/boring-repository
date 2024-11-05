# Import Python Libraries
import warnings
warnings.filterwarnings('ignore')

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
from scipy.integrate import odeint
import pandas as pd
import os

import sys
from collections import Counter


# Set up function for running
def HypoxiaModel(variableshere):
    # Endothelial Cells
    
    
    return dO2, dGlucose

def plotSimulation(time,output):
    return

# Kinetic Rates Constants
# k = ... # [UNIT]

# Set up Timestep For Running The Model
dt = 0.01 #secs
t_final = 3600 #secs
n_steps = int(t_final/dt)

print("Timestep is: ", dt)
print("Time of Simulation is: ", t_final)
print("Total timestep is: ", n_steps)

# Set up Initial Concentrations for Variables into List

# CalL Integration Algorithm

# Extract Individual Vectors from Solution

# Plotting Results
plotSimulation(1,2)


def calcSSE(expts, sims): # Method to compare experiment and model
    return

def minimizeSSE(inputParamVarying,inputParamFixed):
    return
