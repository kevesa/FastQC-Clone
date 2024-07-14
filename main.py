from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt

def readFile(path: str) -> tuple[int, np.ndarray]:
    sum_of_sequences = []
    amount_of_sequences = 0
    with open("C:/Users/Vesa/Python Code/bio/testifastq.fastq") as handle:
        for index, sequence in enumerate(SeqIO.parse(handle, "fastq")):
            quality_scores = sequence.letter_annotations["phred_quality"]
            sum_of_sequences.append(quality_scores)
            amount_of_sequences = index

    return(amount_of_sequences+1, np.array(sum_of_sequences))

def doStatistics(data: np.ndarray):
    plt.boxplot(data)
    plt.xlabel("Position")
    plt.ylabel("Quality")
    plt.title("Box Plot with Matplotlib")
    plt.show()

def main():
    print("ABC")
    print(readFile("path"))
    index, data = readFile("path")
    doStatistics(data)



if __name__ == "__main__":
    main()
    print("GHGHHHHH")
