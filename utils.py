from Bio import SeqIO
import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#This file contains basic tools needed for handling user input data.


#TODO: Added padding to ensure that sequences are of uniform length
def read_file(path: str) -> tuple[int, pd.DataFrame, pd.DataFrame]:
    sequence_qualities = []
    base_contents = []
    amount_of_sequences = 0
    with open("C:/Users/Vesa/Python Code/bio/lyhyt.fastq") as handle:
        for index, sequence in enumerate(SeqIO.parse(handle, "fastq")):
            print(type(sequence.seq))
            quality_scores = sequence.letter_annotations["phred_quality"]
            sequence_qualities.append(quality_scores)
            amount_of_sequences = index
            
            base_contents.append(sequence.seq)
            #print(type(quality_scores), quality_scores)
            #print(type(sequence.seq), sequence.seq)
    print("JOJOJJOJOJOJJOJOOOJJOJO")
    """get_gc_content(base_contents) #UNCOMMENT THIS"""



    #print(sum_of_sequences.T)
    return(amount_of_sequences+1, pd.DataFrame(zip(*sequence_qualities)).T, pd.DataFrame(zip(*base_contents)).T)

def get_gc_content(data):
    min_gc = 100
    max_gc = 0
    gc_list = []
    for sequence in data:
        sequence_gc = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
        if sequence_gc < min_gc:
            min_gc = sequence_gc
        if sequence_gc > max_gc:
            max_gc = sequence_gc

        gc_list.append(sequence_gc)

    gc_content = pd.DataFrame(list(zip(gc_list)))
    #TODO: The current theoretical distribution curve is as of now complete garbage and should be ignored. 
    # Need to look more into how it should be implemented. Histogram for counts and GC content works as expected.
    sns.histplot(data=gc_content, kde=True)#, bw=0.1)
    mu, sigma = norm.fit(gc_content)
    x_vals = np.linspace(min_gc, max_gc, 100)
    y_vals = norm.pdf(x_vals, mu, sigma)#*7000
    
    plt.plot(x_vals, y_vals, label='Normal Distribution (Theoretical)')
    #plt.ylim(0, 0.1)
    print("PELELELELELE")
    print("gc_content.min()", min_gc,"powpowpow", max_gc, "PEWPWE")
    print(x_vals)
    print(y_vals)
    print(mu, sigma)

    #plt.xlabel('Values')
    #plt.ylabel('Density')
    #plt.title('Distribution of Values')
    ax = plt.gca()
    ax.set_xlim(0, 100)
    plt.show()

    #print(gc_content)