# Imports.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotting import *

### (a) Distinct values.

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
        success_rate=sum(sum(success))/len(temp_df)
        sr_val.append(success_rate)
    sr_all.append(sr_val)


### (d) Plots
for i in range(len(a)):
    scatterPlot(a[i],sr_all[i],'2_(ii)_Fig_',i+1)


