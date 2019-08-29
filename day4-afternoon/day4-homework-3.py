#!/usr/bin/env python3

"""
usage:./py <t_name> <samples_csv> <FPKMS>

create a timecourse of a given transcrip for females
./day4-homework-3.py FBtr0331261 ~/qbb2019/data/samples.csv
"""


import sys
import pandas as pd
import matplotlib.pyplot as plt


t_name = sys.argv[1]
samples=pd.read_csv(sys.argv[2])



#fpkms = df.drop(columns="gene_name")

def sex_ident(sex):
   soi= samples.loc[:,"sex"] == sex
   srr_ids= samples.loc[soi,"sample"]

   fpkms= pd.read_csv(sys.argv[3], index_col="t_name")
   my_data= []
   for srr_id in srr_ids:
       my_data.append(fpkms.loc[t_name,srr_id])
   return my_data

f_vals= sex_ident("female")
m_vals= sex_ident("male")


fig, ax= plt.subplots()
ax.plot(f_vals, color="red", label="female")
ax.plot(m_vals, color="blue", label="male")
ax.legend()
fig.suptitle("FBtr0331261 Expression")
ax.set_xlabel("Developmental Stage")
ax.set_ylabel("mRNA Expression Level (FPKMs)")
ax.set_xticklabels(["0","10", "11", "12", "13", "14A", "14B", "14C", "14D"])
fig.savefig("timecoursefvs.png")
plt.close(fig)












    