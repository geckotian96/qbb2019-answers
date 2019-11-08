#!/usr/bin/env python3

"""
Usage: ./densityplot.py regionoverlap.out 
"""




import sys 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


list1=[]

for i, line in enumerate (open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    pos=int(fields[3])
    seq_start=int(fields[10])
    seq_end=int(fields[11])
    seq_length=seq_end-seq_start
    ral_pos=(pos-seq_start)/seq_length
    list1.append(ral_pos) 
print (list1)
   

fig, ax =plt.subplots()
ax.hist(list1, color="orange", bins=40, alpha=0.8)
ax.set_title("Density plot")
ax.set_xlabel("Relative Position to Sequence")
ax.set_ylabel("Freq")
fig.savefig("densityplot.png")
plt.close(fig)

