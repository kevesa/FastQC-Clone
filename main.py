from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def readFile(path: str) -> tuple[int, np.ndarray]:
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

def doStatistics(data):
    plt.boxplot(data)
    plt.xlabel("Position")
    plt.ylabel("Quality")
    plt.title("Box Plot with Matplotlib")
    plt.show()

def doSeaborn(data1):
    sns.boxplot(data=data1)
    plt.show()


def main():
    print("ABC")
    print(readFile("path"))
    index, data = readFile("path")
    doStatistics(data)
    #doSeaborn(data)

if __name__ == "__main__":
    main()
    print("GHGHHHHH")
