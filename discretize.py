import pandas as pd
import numpy as np
import sys

def get_arguments():
    #print(len(sys.argv))
    if len(sys.argv)<2:
        print("Proper parameter not passed. default values will be used")
        print("default values: dating.csv and dating-binned.csv")
        args=["dating.csv","dating-binned.csv"]
        return args
    args=[sys.argv[1], sys.argv[2]]
    return args



def PutIntoBin(NB):
    n=len(sys.argv)
    labels = list(range(NB))
    exclusion= ["gender", "race", "race_o", "samerace", "field", "decision"]
    df = pd.read_csv(args[0])

    pref_scores= [col for col in df.columns if "pref_o" in col or "important" in col]
    all_attributes=[item for item in df.columns]
    attr_wo_exclusion=[item for item in all_attributes if item not in exclusion]

    for attribute in attr_wo_exclusion:
            if (attribute in pref_scores):
                custom_bins = np.linspace(0,1,NB + 1)
                df[attribute] = pd.cut(df[attribute], custom_bins, include_lowest = True, labels = labels)
                df[attribute] = df[attribute].fillna(labels[-1])

            elif (attribute in ["age","age_o"]):
                custom_bins = np.linspace(18 , 58, NB + 1)
                df[attribute] = pd.cut(df[attribute], custom_bins, include_lowest = True, labels = labels)
            elif (attribute == "interests_correlate"):
                custom_bins = np.linspace(-1 , 1, NB + 1)
                df[attribute] = pd.cut(df[attribute], custom_bins, include_lowest = True, labels = labels)
            else:
                minV = np.min(df[attribute])
                maxV = np.max(df[attribute])
                custom_bins = np.linspace(minV , maxV, NB + 1)
                df[attribute] = pd.cut(df[attribute], custom_bins, include_lowest = True, labels = labels)
                df[attribute] = df[attribute].fillna(labels[-1])
    df.to_csv(args[1], index = False)
    return attr_wo_exclusion,df


def PutIntoBin5_3(NB):

    labels = list(range(NB))
    exclusion= ["gender", "race", "race_o", "samerace", "field", "decision"]
    df = pd.read_csv("dating.csv")

    pref_scores= [col for col in df.columns if "pref_o" in col or "important" in col]
    all_attributes=[item for item in df.columns]
    attr_wo_exclusion=[item for item in all_attributes if item not in exclusion]

    for attribute in attr_wo_exclusion:
            if (attribute in pref_scores):
                custom_bins = np.linspace(0,1,NB + 1)
                df[attribute] = pd.cut(df[attribute], custom_bins, include_lowest = True, labels = labels)
                df[attribute] = df[attribute].fillna(labels[-1])

            elif (attribute in ["age","age_o"]):
                custom_bins = np.linspace(18 , 58, NB + 1)
                df[attribute] = pd.cut(df[attribute], custom_bins, include_lowest = True, labels = labels)
            elif (attribute == "interests_correlate"):
                custom_bins = np.linspace(-1 , 1, NB + 1)
                df[attribute] = pd.cut(df[attribute], custom_bins, include_lowest = True, labels = labels)
            else:
                minV = np.min(df[attribute])
                maxV = np.max(df[attribute])
                custom_bins = np.linspace(minV , maxV, NB + 1)
                df[attribute] = pd.cut(df[attribute], custom_bins, include_lowest = True, labels = labels)
                df[attribute] = df[attribute].fillna(labels[-1])
    df.to_csv("dating-binned.csv", index = False)
    return attr_wo_exclusion,df

def printVals(awe,df):
    count=0
    for attribute in awe:
        count=count+1
        print("%s: %s" % (attribute, list(df.groupby(attribute)[attribute].count())))
    #print("total lines:", count)

if __name__ == "__main__":
   args = get_arguments()
   awe,df=PutIntoBin(5)
   printVals(awe,df)
