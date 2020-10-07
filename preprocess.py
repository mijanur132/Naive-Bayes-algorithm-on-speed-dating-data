
import pandas as pd
import numpy as np

# Read input
df = pd.read_csv("dating-full.csv")
df.rename(columns = {"intelligence_parter" : "intelligence_partner"}, inplace = True)


# 1-(i) remove the quotes
# 1-(ii) Convert all the values in the column field to lowercase
sum=0
sum2=0
labelEnc=[]
EncLabel=[]

for column in ["race","race_o","field"]:
        temp_column=df[column].copy()
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
pref_scores_participant=[col for col in df.columns if "important" in col]
pref_scores_participant_total = df[pref_scores_participant].sum(axis = 1)
pref_scores_partner=[col for col in df.columns if "pref_o" in col]
pref_scores_partner_total = df[pref_scores_participant].sum(axis = 1)

for column in range(len(pref_scores_participant)):
        df[pref_scores_participant[column]] = df[pref_scores_participant[column]] / pref_scores_participant_total
        print ("Mean of %s: %.2f" % (pref_scores_participant[column], np.mean(df[pref_scores_participant[column]])))


for column in range(len(pref_scores_partner)):
        df[pref_scores_partner[column]] = df[pref_scores_partner[column]] / pref_scores_partner_total
        print ("Mean of %s: %.2f" % (pref_scores_partner[column], np.mean(df[pref_scores_partner[column]])))

# Save the output in dating.csv.

df.to_csv("dating.csv", index = False)
