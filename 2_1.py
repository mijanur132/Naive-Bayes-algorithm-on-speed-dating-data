# Imports.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from plotting import *


# 2 Visualizing interesting trends in data

df = pd.read_csv("dating.csv")

## (i) save in file named (2_1.py)

### (a) Divide the dataset into two sub-datasets by the gender of the participants.

male_df = df[df["gender"] == 1]
female_df = df[df["gender"] == 0]


### (b) Compute the mean values within each subset.


pref_scores_participant=[col for col in df.columns if "important" in col]


male_mean = []
female_mean = []
for column in range(len(pref_scores_participant)):
    male_mean.append(np.mean(male_df[pref_scores_participant[column]]))

for column in range(len(pref_scores_participant)):
    female_mean.append(np.mean(female_df[pref_scores_participant[column]]))

### (c) Use a single barplot to contrast how females and males value the six attributes.

barWidth = 3
heightMales = male_mean
heightFemales = female_mean

width = 1+np.arange(len(heightMales))


x = np.arange(len(pref_scores_participant))  # the label locations
barPlot(x+width,x+width+0.8,heightMales,heightFemales,\
        "Attribute vs Gender","Male / Female", pref_scores_participant,\
        "Mean", ["Males", "Females"], '2_(i)_c.png')














"""
fig, ax = plt.subplots()
ax.bar(x+width , heightMales, color='red')
ax.bar(x + width+0.8, heightFemales, color ='green')
plt.tight_layout()
ax.set_title("Attribute vs Gender")
ax.set_xlabel("Male / Female)")
ax.set_xticks(x+width)
ax.set_xticklabels(pref_scores_participant, rotation = 45)
ax.set_ylabel("Mean")
ax.legend(["Males", "Females"])

plt.savefig('2_(i)_c.png', bbox_inches='tight')
"""