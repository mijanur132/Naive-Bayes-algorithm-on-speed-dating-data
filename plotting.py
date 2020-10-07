import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def barPlot(x_locs,y_locs,x_data,y_data,title,x_label, xtick_data,y_label, legend, saveName):
    fig, ax = plt.subplots()
    ax.bar(x_locs , x_data, color='red')
    ax.bar(y_locs, y_data, color ='green')
    plt.tight_layout()
    ax.set_title(title)
    ax.set_xlabel(x_label)
    ax.set_xticks(x_locs)
    ax.set_xticklabels(xtick_data, rotation = 45)
    ax.set_ylabel(y_label)
    ax.legend(legend)
    plt.savefig(saveName, bbox_inches='tight')

def scatterPlot(a_i, sr_val_i):
    fig, ax = plt.subplots()
    ax.set_title(" Scatter Plot: Success rate vs %s." % (a_i[0]))
    ax.set_xlabel("Attribute : %s." % (a_i[0]))
    ax.set_ylabel("Success rate")
    ax.scatter(a_i[1],sr_val_i, color="red" )

