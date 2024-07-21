import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


#This file contains functions necessary for base content analysis.

def get_base_content(data):
    counts = []
    counts2 = pd.DataFrame()
    possible_values = {"G":0, "C":0, "A":0, "T":0}
    print("blöö", len(data))
    for index in range(data.shape[1]):
        counts.append(data[index].value_counts(normalize=True)*100)
    
    counter = 1
    for x in counts:
        #print(x.index)
        #print(x)
        x = x.rename(counter)
        counter += 1
        counts2 = pd.concat([counts2, x], axis=1)
        counts2 = counts2.fillna(0)
    print("HADOOOOO")
    print(counts2)
    print("FRFRFRRFRRFRFRFRFR")
    counts2 = counts2.drop(index=["N", "a"])
    counts2 = counts2.reindex(["G", "C", "A", "T"])
    #print(counts2.iloc[2])
    #sns.lineplot(data=counts2)#.iloc[1])
    for index, row in counts2.iterrows():
        sns.lineplot(x=row.index, y=row.values, legend="auto", label = index)#, loc="")
        print(index)
    print(counts2.index[1][:-2])
    print(type(counts2.index[1]))
    ax = plt.gca()
    ax.set_ylim(0, 100)
    plt.legend(loc="upper right")
    plt.title("Per base sequence content")
    plt.xlabel("Position in read")
    plt.ylabel("% Base")
    plt.xticks(np.arange(0, data.shape[1]+10, 10))
    plt.show()

