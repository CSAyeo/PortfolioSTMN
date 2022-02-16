import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import string
setYear = 2015


def genTrend(sCount, pCount, yCount):
    a = 0.9
    b = 50
    f = []
    hk, hi, hj = 0,0,0
    for j in range(sCount):
        pos = []
        for k in range (pCount):
            y = []
            for i in range(yCount):
                y.append(round((a * i + 0.1 ** 2 + b * i + 0.1) * random.random() + 450+i))
            pos.append(y)
        f.append(pos)
    indexlist = list(string.ascii_uppercase[:pCount])
    df = pd.DataFrame(f, index=[x for x in range(1,sCount+1)], columns=indexlist)
    print(df)

    return(df)

def getVals():
      df = pd.read_csv('Data.csv', index_col=0)
      return(df)

def setVals(df):
      df.to_csv("Data.csv")


