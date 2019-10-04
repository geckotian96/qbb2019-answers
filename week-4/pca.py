#!/usr/bin/env python3





import sys
import matplotlib.pyplot as plt

comp1= []
comp2= [] 

for i, line in enumerate (open(sys.argv[1])):
    fields = line.rstrip("\n").split("\t")
    comp1.append(float(fields[2]))
    comp2.append(float(fields[3]))
#notice that you need to convert stiring into integers 
#fig, ax = plt.subplots() fig is the overall figure, ax is the subpanel

fig, ax =plt.subplots()
ax.scatter(comp1,comp2, color="red", alpha=0.05)  
#ax.plot([0, 40], [0, 20000], color = "red")
ax.set_title("PCA")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
fig.savefig("PCA.png")
plt.close(fig)