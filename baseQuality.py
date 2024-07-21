import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#This file contains functions necessary for base quality analysis.

def do_base_quality(data):
    positions = range(0, len(data.columns), 10)
    labels = data.columns[positions]

    plot = sns.boxplot(data=data)
    plot.axhspan(0, 20, facecolor="red", alpha=0.5)
    plot.axhspan(20, 28, facecolor="orange", alpha=0.5)
    plot.axhspan(28, 41, facecolor="limegreen", alpha=0.5)
    plot.set_ybound(40)
    plt.xlabel("Position")
    plt.xticks(positions, labels)
    plt.ylabel("Quality")
    plt.ylim(0, 40)
    plt.title("Quality Scores across base positions")
    plt.suptitle("XxXxXxXxX")
    plt.show()

def  do_length_distribution(data):
    print("")