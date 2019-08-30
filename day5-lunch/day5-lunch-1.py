#!/usr/bin/env python3

#~/qbb2019-answers/results/stringtie/SRR072893/t_data.ctab

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

ctab_file = sys.argv[1]


df=pd.read_csv(ctab_file, sep="\t")

clean_df=df.loc[:,["chr","start","end","t_name"]]

strand=df.loc[:,"strand"]=="+"

col_strand=strand.drop(columns="t_name")

new_df=clean_df.join(col_strand)


for index, row in new_df.iterrows():
    if row.loc["strand"] == True:
        row.loc["start"]=int(row.loc["start"])-500
        row.loc["end"]=int(row.loc["end"])+500
        print (row.loc["chr"], row.loc["start"], row.loc["end"], row.loc["t_name"], sep="\t" )
    else:
        row.loc["start"]=int(row.loc["start"])+500
        row.loc["end"]=int(row.loc["end"])-500
        print (row.loc["chr"], row.loc["start"], row.loc["end"], row.loc["t_name"], sep="\t" )

# print (new_df)




