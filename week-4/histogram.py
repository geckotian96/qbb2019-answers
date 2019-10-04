#!/usr/bin/env python3





import sys
import matplotlib.pyplot as plt

freq=[]

for i, line in enumerate (open(sys.argv[1])):
    if i == 0:
        continue
    
    fields = line.rstrip("\n").split()
    freq.append(float(fields[5]))
   
print (freq) 
fig, ax =plt.subplots()
ax.hist(freq, color="orange", bins=100, alpha=0.8)
 #ax.plot([0, 40], [0, 20000], color = "red")
ax.set_title("Allele Frequency")
ax.set_xlabel("Allele")
ax.set_ylabel("Freq")
fig.savefig("AF.png")
plt.close(fig)