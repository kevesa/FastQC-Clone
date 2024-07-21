from Bio import SeqIO
import pandas as pd

#This file contains basic tools needed for handling user input data.

def read_file(path: str) -> tuple[int, pd.DataFrame, pd.DataFrame]:
    sequence_qualities = []
    base_contents = []
    amount_of_sequences = 0
    with open("C:/Users/Vesa/Python Code/bio/lyhyt.fastq") as handle:
        for index, sequence in enumerate(SeqIO.parse(handle, "fastq")):
            print(sequence.seq)
            quality_scores = sequence.letter_annotations["phred_quality"]
            sequence_qualities.append(quality_scores)
            amount_of_sequences = index
            
            base_contents.append(sequence.seq)
            print(type(quality_scores), quality_scores)
            print(type(sequence.seq), sequence.seq)



    #print(sum_of_sequences.T)
    return(amount_of_sequences+1, pd.DataFrame(zip(*sequence_qualities)).T, pd.DataFrame(zip(*base_contents)).T)