import pandas as pd
import numpy as np


def PutIntoBin(NB):
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
    for attribute in awe:
        print("%s: %s" % (attribute, list(df.groupby(attribute)[attribute].count())))


if __name__ == "__main__":
   awe,df=PutIntoBin(5)
   printVals(awe,df)
