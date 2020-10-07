# Imports.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from discretize import *
from split import *

var5_1 = __import__('5_1')

F = [0.01, 0.1, 0.2, 0.5, 0.6, 0.75, 0.9, 1]
fracAcc = {}


PutIntoBin(5)
training_test_split()

TrainAcc = []
TestAcc=[]

for f in F:
    print ("Fraction of the Training Data(f) : %.2f" % f)
    Acc = []
    var5_1.nbc(f, Acc)
    TrainAcc.append(Acc[0])
    TestAcc.append(Acc[1])
    print("Training Accuracy:%f" % Acc[0])
    print("Testing Accuracy:%f" % Acc[1])

fig, ax = plt.subplots()
ax.set_title(" Plot of f vs. Accuracy")
ax.set_xlabel("f Values.")
ax.set_ylabel("Accuracies corresponding to these f values.")

ax.plot(F, TestAcc, '-x',color="red")
ax.plot(F, TrainAcc, '-o', color="green")
ax.legend(["Test","Train"])

plt.savefig('5_3.png')
