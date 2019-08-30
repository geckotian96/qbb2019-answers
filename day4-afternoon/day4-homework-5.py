#!/usr/bin/env python3

#argv[1] is the all.csv
import sys
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np

sample= sys.argv[1]


df=pd.read_csv(sample)

r=df.loc[:, "SRR072893"]
g=df.loc[:, "SRR072894"]
r += 1
g += 1
#np.log
m=np.log2(r/g)
a=np.log2(r*g)*(0.5)


fig, ax =plt.subplots()
fig.suptitle("MA-Plot SRR072893 vs. SRR072894")

ax.scatter(x=a,y=m, alpha=0.2)
ax.set_xlabel("A")
ax.set_ylabel("M")
  
fig.savefig("893vs.894.png")
plt.close(fig)


# fpkms["gene_name"] =df.loc[:,"gene_name"]
# fpkms[((sex_stage))]=df.loc[:,"FPKM"]
#
#
# df_fpkm = pd.DataFrame(fpkms)
#
# print (df_fpkm)
#
#
# pd.DataFrame.to_csv(df_fpkm, "two_stage.csv")