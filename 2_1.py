# Imports.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotting import *


# 2 Visualizing interesting trends in data

df = pd.read_csv("dating.csv")


### (a) Two sub-datasets from gender.

male_df = df[df["gender"] == 1]
female_df = df[df["gender"] == 0]


### (b) Compute the mean values.


pref_scores_participant=[col for col in df.columns if "important" in col]


male_mean = []
female_mean = []
for column in range(len(pref_scores_participant)):
    male_mean.append(np.mean(male_df[pref_scores_participant[column]]))

for column in range(len(pref_scores_participant)):
    female_mean.append(np.mean(female_df[pref_scores_participant[column]]))



### (c) Barplot
width = 1+np.arange(len(male_mean))

x = np.arange(len(pref_scores_participant))  # the label locations
barPlot(x+width,x+width+0.8,male_mean,female_mean,\
        "Attribute vs Gender","Male / Female", pref_scores_participant,\
        "Mean", ["Males", "Females"], '2_(i)_c.png')










