from split import *
from discretize import *

var5_1 = __import__('5_1')

numBins = [2, 5, 10, 50, 100, 200]
NBin=len(numBins)
TrainAcc = []
TestAcc=[]

for NB in numBins:
    PutIntoBin(NB)
    training_test_split()
    print ("Bin size: %d" % NB)
    Acc = []
    var5_1.nbc(1, Acc)
    TrainAcc.append(Acc[0])
    TestAcc.append(Acc[1])
    print("Training Accuracy:%f" %Acc[0])
    print("Testing Accuracy:%f" %Acc[1])

fig, ax = plt.subplots()
ax.set_title(" Number of Bins vs. Accuracy")
ax.set_xlabel("Bin Numbers.")
ax.set_ylabel("Model Accuracy.")
ax.plot(numBins, TrainAcc, '-x', color="red")
ax.plot(numBins, TestAcc, '-o', color="green")
ax.legend(["Train","Test"])
plt.savefig("5_2.png")
