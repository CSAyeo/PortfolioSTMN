from matplotlib.pyplot import subplots_adjust, subplot

from IOHandler import *
from GenXData import *
from Gendata import *
from Model import *
import matplotlib

def getMean(df):
    fig, axs = plt.subplots(len(df), len(df.columns))
    subplots_adjust(hspace=0.000)
    if len(df) > 1 and len(df.columns) > 1:
        for x in range(len(df)):
            for y in range(len(df.columns)):
                axs[x,y].plot(df.iloc[x, y], label = "x: {x} y: {y}".format(x=x, y=y))
    else:
        axs.plot(df.iloc[0, 0], label = "x: {x} y: {y}".format(x=0, y=0))
    plt.show()


print("Testing \n Generating new data")
data =genTrend(5,5, 15)
print(data)
setVals(data)
print("Calculating mean")
getMean(data)
