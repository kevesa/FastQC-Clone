import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


#This file contains functions necessary for base content analysis.

def do_base_content(data):
    sns.lineplot(data=data)
    plt.show()