import xarray as xr
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string

def genRandom(yCount, pCount, sCount):
    coordinates = np.random.randint(450, 600, size=(yCount, pCount, sCount))
    return(coordinates)
def getVals():
      df = pd.read_csv('Data.csv', index_col=0)
      return(df)

def setVals(df):
      df.to_csv("Data.csv")


