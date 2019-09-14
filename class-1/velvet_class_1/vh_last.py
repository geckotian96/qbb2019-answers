#!/usr/bin/env python3

"""
9_13 class 
Make a dotplot for lastz output
Usage: ./name.py file.out

"""

import sys
import matplotlib.pyplot as plt
# import numpy as np
# import scipy.stats as stats

list_y=[]
list_x=[]
for i, line in enumerate(open(sys.argv[1])):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    y = int(fields[5]) - int(fields[4])
    x = int(fields[8])
    list_y.append(y)
    list_x.append(x)
#print (list_y)


fig, ax =plt.subplots()
fig.suptitle("Dotplot1")

ax.scatter(x=list_x,y=list_y, alpha=0.2)
ax.set_xlabel("total length of contigs")
ax.set_ylabel("length of ref.")
  
fig.savefig("vh.png")
plt.close(fig)
