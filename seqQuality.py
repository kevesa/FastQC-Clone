import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

#This file contains functions necessary for sequence quality analysis and sequence length distribution.

#TODO: This doesn't seem to be working quite right. Possibly issues with correct binning? For reference, look at Per sequence quality scores in FastQC.
def get_sequence_quality(data):
    total_bases = data.size
    bins = [32.5, 33.5, 34.5, 35.5]
    labels = ["33", "34", "35"]
    print(type(total_bases))
    row_mean = data.mean(axis=1)
    #mean_counts = row_mean.value_counts()
    binned_means = pd.cut(row_mean, bins=bins, labels=labels, include_lowest=True, right = False)
    binned_means = binned_means.value_counts()
    binned_means = binned_means.sort_values()
    binned_means = binned_means.reindex(["33", "34", "35"])
    #binned_means = pd.to_numeric(binned_means, errors="coerce")
    #category_counts = binned_means.value_counts().reset_index(name='Count')

    print(row_mean)
    #print(mean_counts)
    print(binned_means)
    #print(category_counts)

    binned_means.plot(kind="line")#, order=["33", "34", "35"])
    plt.suptitle("Per sequence quality score")
    plt.xlabel("Mean sequence quality score")
    plt.ylabel("Number of sequences")
    plt.show()

def get_sequence_distribution(data):
    print("")