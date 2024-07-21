from Bio import SeqIO
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import utils
import baseContent as bc
import baseQuality as bq
import seqQuality as sq
from scipy.stats import norm

#DONE: Per base sequence quality
#DONE: Per sequence quality scores
#DONE: Per base sequence content
#TODO: Per sequence GC content (HALF DONE)
#TODO: Per base N content
#TODO: Sequence length distribution
#(TODO: Sequence duplication levels/Overrepresented sequences/Adapter content)
#TODO: Implement a CLI/GUI.
"""
def get_gc_content(data):
    gc_list = []
    for sequence in data:
        sequence_gc = (sequence.count("G") + sequence.count("C")) / len(sequence) * 100
        gc_list.append(sequence_gc)

    gc_content = pd.DataFrame(list(zip(gc_list)))

    print(gc_content)
"""

def main():
    print("ABC")
    utils.read_file("path")
    #index, data1, data2 = utils.read_file("path")
    #print(data1)
    #print(data2)
    #doSeaborn(data)
    #sq.do_sequence_quality(data1)
    #bc.get_base_content(data2)

if __name__ == "__main__":
    main()
    print("GHGHHHHH")
