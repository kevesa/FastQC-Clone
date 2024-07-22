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

#DONE: Per base sequence quality.
#DONE: Per sequence quality scores.
#DONE: Per base sequence content.
#TODO: Per sequence GC content (HALF DONE, the implementation of theoretical distribution curve is non-essential and could be skipped altogether without remorse).
#DONE: Per base N content.
#TODO: Sequence length distribution (READ TODO at def get_sequence_distribution() in baseContent.py).
#(TODO: Sequence duplication levels/Overrepresented sequences/Adapter content).
#TODO: Implement a CLI/GUI.
#TODO: Clean up the unnecessary print statements and do some unit testing.


def main():
    print("ABC")
    #utils.read_file("path")
    index, data1, data2 = utils.read_file("path")
    #print(data1)
    #print(data2)
    #doSeaborn(data)
    #sq.do_sequence_quality(data1)
    #bc.get_base_content(data2)
    print(data2)
    print("QIQIQIQIQIQIQIQIQIQIQIQIQIQI")
    get_sequence_distribution(data2)
    #utils.get_gc_content(data2)

if __name__ == "__main__":
    main()
    print("GHGHHHHH")
