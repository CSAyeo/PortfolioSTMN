import sys

from Model import *
from Gendata import getVals
def BeginUser():
    print(sys.version_info)
    while True:
        try:
            vI = [1, 2]
            dData = int(input("Do you want to \n 1) Build Model \n 2) Adjust Data\n"))
        except ValueError or not(dData in vI):
            print("Invalid input")
            continue
        else:
            break
    match dData:
        case 1:
            MakeModel()
        case 2:
            DisplayData()
        case default:
            print(f"Invalid input, erring {dData=}")
def DisplayData():
    print(getVals())
    while True:
        try:
            vI = [1, 2]
            dData = int(input("Do you want to \n 1) Adjust parameters \n 2) Generate new data\n"))
        except ValueError or not(dData in vI):
            print("Invalid input")
            continue
        else:
            break
    match dData:
        case 1:
            MakeModel()
        case 2:
            DisplayData()
        case default:
            print(f"Invalid input, erring {dData=}")
#def SelectData():
#def SaveOut():
#def Sentiment():
