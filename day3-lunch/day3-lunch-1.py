#!/usr/bin/env python3

"""
this aims to search mutation near the closest coding protein

"""

import sys
f=open(sys.argv[1])

listsmall=[]
listbig=[]

for line in f:
    
    if "DROME" not in line and "FBgn" not in line:
        continue
    line = line.rstrip("\n")
    columns =line.split("\t")
    
    if "3R" in columns[0] and "gene" in columns[2] and "protein_coding" in line:
        print (line)
        

    

        


