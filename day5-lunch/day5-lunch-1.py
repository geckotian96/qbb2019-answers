#!/usr/bin/env python3

#~/qbb2019-answers/results/stringtie/SRR072893/t_data.ctab

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

ctab_file = sys.argv[1]


df=pd.read_csv(ctab_file, sep="\t", index_col="t_name")

clean_df=df.loc[:,["chr","start","end","t_name"]]

strand=df.loc[:,"strand"]=="+"

col_strand=strand.drop(columns="t_name")

new_df=clean_df.join(col_strand)


for index, row in new_df.iterrows():
    if row.loc["strand"] == True:
        row.loc["start"]=row.loc["start"]-500
        row.loc["end"]=row.loc["end"]+500
    else:
        row.loc["start"]=row.loc["start"]+500
        row.loc["end"]=row.loc["end"]-500

print (new_df)


