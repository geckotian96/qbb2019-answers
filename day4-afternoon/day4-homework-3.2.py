#!/usr/bin/env python3

"""
usage:./py <t_name> <samples_csv> <FPKMS>

create a timecourse of a given transcrip for females
./day4-homework-3.py FBtr0331261 ~/qbb2019/data/samples.csv
/Users/cmdb/qbb2019/data/repl
"""
#./day4-homework-3.2.py  FBtr0331261 ~/qbb2019/data/samples.csv ~/qbb2019/data/replicates.csv ~/qbb2019-answers/results/stringtie/


import sys
import pandas as pd
import matplotlib.pyplot as plt
import os

t_name = sys.argv[1]
samples=pd.read_csv(sys.argv[2])
replicates=pd.read_csv(sys.argv[3])
ctab_dir=sys.argv[4]


#fpkms = df.drop(columns="gene_name")

def sex_ident(sex, sampletypes):
   soi= sampletypes.loc[:,"sex"] == sex
   srr_ids= sampletypes.loc[soi,"sample"]
   
   my_data= []
   for srr_id in srr_ids:
       ctab_path = os.path.join (ctab_dir, srr_id, "t_data.ctab") # Find path to ctab fil.
       df = pd.read_csv (ctab_path, sep="\t", index_col="t_name") # Load ctab file
       my_data.append(df.loc[t_name,"FPKM"]) # Grab the FPKM value for our transcript, and append to my_data
       
   return my_data

f_vals1= sex_ident("female", samples)
f_vals2= sex_ident("female", replicates)
m_vals1= sex_ident("male", samples)
m_vals2= sex_ident("male", replicates)



fig, ax= plt.subplots()
ax.plot(f_vals1, color="red", label="female")
ax.plot(m_vals1, color="blue", label="male")
ax.plot(range(4,8),m_vals2, ".",color="orange", label="m. replicates")
ax.plot(range(4,8),f_vals2, ".",color="green", label="f. replicates")
ax.legend(loc="lower right", bbox_to_anchor=(1.0, 0.5))

fig.suptitle("FBtr0331261 Expression")
ax.set_xlabel("Developmental Stage")
ax.set_ylabel("mRNA Expression Level (FPKMs)")
ax.set_xticklabels(["0","10", "11", "12", "13", "14A", "14B", "14C", "14D"])

plt.tight_layout()
plt.subplots_adjust(top=0.9)
fig.savefig("timecoursefvs.png")
plt.close(fig)











    