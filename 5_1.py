# Imports.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def calc_accuracy(df1, df2):
    return (np.mean(df1 == df2["decision"]))


def test(P_y_is, test_X, prob_0, prob_1, final_probs, trainSet = None):
    for row in range(len(test_X)):
        x_feature=[column for column in test_X.columns if  'decision' not in column]
        prod_0 = prob_0
        prod_1 = prob_1
        for feature in x_feature:
            try:
                prod_0 *= P_y_is[0][feature][test_X[feature].iloc[row]]
                prod_1 *= P_y_is[1][feature][test_X[feature].iloc[row]]
            except:
                prod_0 *= (1 / len(trainSet[feature].unique()))
                prod_1 *= (1 / len(trainSet[feature].unique()))

        final_probs.append(0 if prod_0 > prod_1 else 1)

def get_prob(y_0_xi,y_0_1,lenx):
     return (y_0_xi + 1) / (y_0_1 + lenx)


def nbc(t_frac,Ac):
    trainSet = pd.read_csv("trainingSet.csv").sample(random_state = 47, frac = t_frac)
    trainSet.reset_index(drop = True, inplace = True)
    testSet = pd.read_csv("testSet.csv")

    total_y_0 = len(trainSet[trainSet["decision"] == 0])
    total_y_1 = len(trainSet[trainSet["decision"] == 1])
    train_set_size=len(trainSet)
    Py_0 = total_y_0 / train_set_size
    Py_1 = total_y_1 / train_set_size
    x_all = [item for item in trainSet.columns if  'decision' not in item]

    P_y_is = {0:{},1:{}}

    for x_i in x_all:
        P_y_is[0][x_i] = {}
        P_y_is[1][x_i] = {}
        x_i_val_all=list(trainSet[x_i].unique())
        for x_i_val in x_i_val_all:
            y_0_xi = len(trainSet[(trainSet[x_i] == x_i_val) & (trainSet['decision'] == 0)])
            y_1_xi = len(trainSet[(trainSet[x_i] == x_i_val) & (trainSet['decision'] == 1)])
            lenx=len(trainSet[x_i].unique())+1
            P_y_is[0][x_i][x_i_val] =get_prob (y_0_xi,total_y_0,lenx)
            P_y_is[1][x_i][x_i_val] =get_prob (y_1_xi,total_y_1,lenx)

    trainRes=[]
    testRes=[]
    test(P_y_is, trainSet, Py_0, Py_1,trainRes)
    test(P_y_is, testSet, Py_0, Py_1,testRes, trainSet)
    Ac.append( calc_accuracy(trainRes,trainSet))
    Ac.append(calc_accuracy(testRes,testSet))



if __name__ == "__main__":
    Acc=[]
    nbc(1,Acc)
    print("Training Accuracy: %.2f." % Acc[0])
    print("Testing Accuracy: %.2f." % Acc[1])
