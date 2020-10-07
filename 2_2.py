# Imports.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotting import *

### (a) Distinct values for this attribute.

df = pd.read_csv("dating.csv")
partner_rating=[col for col in df.columns if "partner" in col]


uniq_val=[]
for i in range(len(partner_rating)):
    uniq_val.append(df[partner_rating[i]].unique())

a=list(zip(partner_rating,uniq_val))


### (c) Success rate
sr_all=[]
for name,vals in a:
    sr_val=[]
    for val in vals:
        temp_df=df[df[name]==val]
        success=[temp_df["decision"]==1]
        m=sum(success)
        m=sum(m)
        success_rate=m/temp_df.shape[0]
        sr_val.append(success_rate)
    sr_all.append(sr_val)


### (d) Plots
"""
def scatterPlot(a_i, sr_val_i):
    fig, ax = plt.subplots()
    ax.set_title(" Scatter Plot: Success rate vs %s." % (a_i[0]))
    ax.set_xlabel("Attribute : %s." % (a_i[0]))
    ax.set_ylabel("Success rate")
    ax.scatter(a_i[1],sr_val_i, color="red" )
"""

index = 1
for i in range(len(a)):
    scatterPlot(a[i],sr_all[i])
    plt.savefig('2_(ii)_Fig_' + str(index) + '.png')
    index += 1


# What do we infer from these plots ?
'''
    Ans :
'''
