#!/usr/bin/env python3


"""
Usage: ./py <metadata.csv> <ctab_dir>

create all.csv with FPKMS 

t_name, gene_name, samplel...samplen..

"""


import sys
import os
import pandas as pd

metadata = sys.argv[1]
ctab_dir = sys.argv[2]
fpkms={}
sex_stage={}



    

for i, line in enumerate (open(metadata)):
    if i==0:
        continue
    fields=line.rstrip("\n").split(",")
    
    srr_id=fields[0]
    sex=fields[1]
    stage=fields[2]
#
    ctab_path = os.path.join(ctab_dir, srr_id, "t_data.ctab")
#

#
    df = pd.read_csv(ctab_path, sep="\t", index_col="t_name")
    fpkms["gene_name"] =df.loc[:,"gene_name"]
    fpkms[((sex, stage))]=df.loc[:,"FPKM"]


df_fpkm = pd.DataFrame(fpkms)
 
print (df_fpkm)


pd.DataFrame.to_csv(df_fpkm, "sex_stage.csv")