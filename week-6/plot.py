#!/usr/bin/env python3

"""
Usage: ./plot.py 
"""




import sys 
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

fig, (ax1, ax2) = plt.subplots (nrows=2)

labels=["intron", "exon", "promoter"]
beforediff=[301, 117, 51]
afterdiff=[349, 144, 72]
x=np.arange(len(labels))
width=0.35

rects1=ax1.bar(x-width/2, beforediff, width, label="G1E", color="orange") 
rects2=ax1.bar(x+width/2, afterdiff, width, label="ER4", color="blue")

ax1.set_title("Features Comparison")
ax1.set_ylabel("Counts")
ax1.set_xticks(x)
ax1.set_xticklabels(labels)
ax1.legend()

labels2=["loss", "gain"]
values=[56, 130]
x2=np.arange(len(labels2))

rects3=ax2.bar(x2, values, width, color="green")

ax2.set_title("Differential Binding")
ax2.set_ylabel("Counts")
ax2.set_xticks(x2)
ax2.set_xticklabels(labels2)


fig.tight_layout()

fig.savefig("barplot.png")
plt.show()
