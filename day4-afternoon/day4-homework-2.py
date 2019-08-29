#!/usr/bin/env python3

"""
USAGE: ./ py <sample_sex> <gene-name> <fpkm>

 ./01-boxplot.py Sxl all.csv 
"""

# SRR072893,male,10
# SRR072894,male,11
# SRR072895,male,12
# SRR072896,male,13
# SRR072897,male,14A
# SRR072899,male,14B
# SRR072901,male,14C
# SRR072903,male,14D
# SRR072905,female,10
# SRR072906,female,11
# SRR072907,female,12
# SRR072908,female,13
# SRR072909,female,14A
# SRR072911,female,14B
# SRR072913,female,14C
# SRR072915,female,14D

import sys
import pandas as pd
import matplotlib.pyplot as plt


gene_name =sys.argv[1]
fpkm_file = sys.argv[2]

columnf=[]
columnm=[]
df = pd.read_csv(fpkm_file, index_col="t_name")
#print (df)

goi =df.loc[:, "gene_name"] == gene_name

#box plot cannot plot gene name 
fpkms = df.drop(columns="gene_name")
column_names=fpkms.columns
#pass print (column_names)


for fname in column_names:
    if "female" in fname:
        columnf.append(True)
    else:
        columnf.append(False)

for mname in column_names:
    if "female" not in mname:
        columnm.append(True)
    else:
        columnm.append(False)

#pass print (columnf)
#pass print (columnm)

fig, (ax1, ax2) = plt.subplots(nrows=2)
fig.subplots_adjust(hspace=0.6)
ax1.boxplot(fpkms.loc[goi,columnf].T)
ax2.boxplot(fpkms.loc[goi,columnm].T)


fig.suptitle("Sxl Female & Male")
ax2.set_xlabel("Stage")
ax1.set_ylabel("FPKMs")
ax2.set_ylabel("FPKMs")
ax1.set_xticklabels(["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
ax2.set_xticklabels(["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
ax1.set_title("Female")
ax2.set_title("Male")

fig.savefig("boxplot.png")
plt.close(fig)