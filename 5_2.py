from split import *
from discretize import *
from plotting import *

var5_1 = __import__('5_1')

numBins = [2, 5, 10, 50, 100, 200]
NBin=len(numBins)
TrainAcc = []
TestAcc=[]

for NB in numBins:
    PutIntoBin5_3(NB)
    training_test_split()
    print ("Bin size: %d" % NB)
    Acc = []
    var5_1.nbc(1, Acc)
    TrainAcc.append(Acc[0])
    TestAcc.append(Acc[1])
    print("Training Accuracy:%f" %Acc[0])
    print("Testing Accuracy:%f" %Acc[1])

regPlot(numBins,numBins,TrainAcc,TestAcc," Number of Bins vs. Accuracy",\
        "Bin Numbers","Model Accuracy.",["Train","Test"],"5_2.png")


