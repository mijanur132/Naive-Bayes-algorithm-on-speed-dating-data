
import pandas as pd
import numpy as np
from data import*
import sys

def get_arguments():
    if len(sys.argv)<2:
        print("Proper parameter not passed. default values will be used")
        print("default values: dating-full.csv and dating.csv")
        args=["dating-full.csv","dating.csv"]
        return args
    args=[sys.argv[1], sys.argv[2]]
    return args


def part1():

    dfc=df_class(args[0])
    df=dfc.csvData


    # 1-(i) remove the quotes
    # 1-(ii) Convert all the values in the column field to lowercase
    sum=0
    sum2=0
    labelEnc=[]
    EncLabel=[]
    #df.rename(columns = {"intelligence_parter" : "intelligence_partner"}, inplace = True)


    for column in ["race","race_o","field"]:
            temp_column=df[column].copy()
            #print(df[column])
            df[column]=df[column].str.replace("'","")
            new_column = df[column]
            df2=temp_column.isin(new_column);
            sum=sum+(len(df2)-df2.sum())

            if(column=="field"):
                temp_column = df[column].copy()
                df[column] = df[column].str.lower()
                new_column = df[column]
                df2 = temp_column.isin(new_column);
                sum2 = sum2 + (len(df2) - df2.sum())



    print ("Quotes removed from %d cells. " %sum)
    print ("Standardized %d cells to lower case. " %sum2)



# 1.(iii) Use label encoding to convert the categorical values in columns

    index = 0
    for column in ["gender","race","race_o","field"]:
        df[column] = df[column].astype('category')
        df.sort_values(by = column, inplace = True)
        df.reset_index(drop = True)
        labelEncx=dict(zip(df[column].cat.codes, df[column]))
        EncLabelx=dict(zip( df[column],df[column].cat.codes))
        df[column] = df[column].cat.codes
        labelEnc.append(labelEncx)
        EncLabel.append(EncLabelx)


    outList = ["male","European/Caucasian-American","Latino/Hispanic American","law"]
    columns=["gender","race","race_o","field"]
    for i in range(len(outList)):
        print ("Value assigned for %s in column %s : %d." % (outList[i], columns[i] , EncLabel[i][outList[i]]))

    df.reset_index(drop = True, inplace = True)

    #1- (iv) Normalization

    for column in range(len(dfc.pref_scores_participant)):
            df[dfc.pref_scores_participant[column]] = df[dfc.pref_scores_participant[column]]/ dfc.pref_scores_participant_total
            print ("Mean of %s: %.2f" % (dfc.pref_scores_participant[column], np.mean(df[dfc.pref_scores_participant[column]])))


    for column in range(len(dfc.pref_scores_partner)):
            df[dfc.pref_scores_partner[column]] = df[dfc.pref_scores_partner[column]] / dfc.pref_scores_partner_total
            print ("Mean of %s: %.2f" % (dfc.pref_scores_partner[column], np.mean(df[dfc.pref_scores_partner[column]])))

    # Output in dating.csv.
    df.to_csv(args[1], index = False)

if __name__ == "__main__":
   args = get_arguments()
   part1()

