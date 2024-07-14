from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def readFile(path: str) -> tuple[int, pd.DataFrame]:
    sum_of_sequences = []
    amount_of_sequences = 0
    with open("C:/Users/Vesa/Python Code/bio/testifastq.fastq") as handle:
        for index, sequence in enumerate(SeqIO.parse(handle, "fastq")):
            quality_scores = sequence.letter_annotations["phred_quality"]
            sum_of_sequences.append(quality_scores)
            amount_of_sequences = index
            #print(type(quality_scores), quality_scores)

    #print(sum_of_sequences.T)
    return(amount_of_sequences+1, pd.DataFrame(zip(*sum_of_sequences)).T)

#TODO: This doesn't seem to be working quite right. Possibly issues with correct binning? For reference, look at Per sequence quality scores in FastQC.
def doStatistics(data):
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
    plt.show()


def doSeaborn(data1):
    positions = range(0, len(data1.columns), 10)
    labels = data1.columns[positions]

    plot = sns.boxplot(data=data1)
    plot.axhspan(0, 20, facecolor="red", alpha=0.5)
    plot.axhspan(20, 28, facecolor="orange", alpha=0.5)
    plot.axhspan(28, 41, facecolor="limegreen", alpha=0.5)
    plot.set_ybound(40)
    plt.xlabel("Position")
    plt.xticks(positions, labels)
    plt.ylabel("Quality")
    plt.ylim(0, 40)
    plt.title("Quality Scores across base positions")
    plt.show()

#TODO: Implement a GUI.
def main():
    print("ABC")
    print(readFile("path"))
    index, data = readFile("path")
    #doSeaborn(data)
    doStatistics(data)

if __name__ == "__main__":
    main()
    print("GHGHHHHH")
