#!/usr/bin/env python3

"""
USAGE: ./00-scatter.py <ctab>
compare num_exons vs. length
"""
#../results/stringtie/SRR072893/t_data.ctab



import sys
import matplotlib.pyplot as plt
import os
import pandas as pd 
import numpy as np


name1=sys.argv[1].split(os.sep)[-2]
ctab1=pd.read_csv(sys.argv[1], sep="\t", index_col ="t_name")
name2=sys.argv[2].split(os.sep)[-2]
ctab2=pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")


fpkm = {name1: ctab1.loc[:, "FPKM"], name2: ctab2.loc[:, "FPKM"]} 

df = pd.DataFrame(fpkm)

x_srr=np.log2(df.loc[:, name1]+1)
y_srr=np.log2(df.loc[:, name2]+1)
cof=np.polyfit(x_srr, y_srr, 1)

xp=np.linspace(0, 15, 15)
yp=cof[0]*xp+cof[1]

fig, ax =plt.subplots()
ax.scatter( x= x_srr, y= y_srr, s=5, alpha=0.2)
ax.plot(xp, yp, color="red")

fig.suptitle("FPKM")
ax.set_xlabel ("SRR072893")
ax.set_ylabel ("SRR072894")

fig.savefig("893 vs. 894.png")
plt.close(fig)

#to open the file, first exe the scripts and then open <fig.savefig(name)>
#modify the plot so that can see the dots better
#the initial plot has chunk of mass in 20000
