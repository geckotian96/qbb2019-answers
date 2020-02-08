#!/usr/bin/env python3

import sys 
import numpy as np
from numpy.random import binomial 
import matplotlib.pyplot as plt
import seaborn as sns

#In other words, if an individual does not leave offspring (fitness is zero), the selection against it in a genetic sense is 1 (100%) s=1 no offspring 


def one_simulation (anum, s, repetitions = 1000):
    anum=int(anum)
    n1 = np.ones(repetitions, dtype=np.uint64)
    Tn = np.empty_like(n1)
    update = (n1 > 0)&(n1<anum)
    t=0
    
    while update.any():
        t += 1
        p1 = n1 * (1 + s) / (anum +n1*s)
        n1[update]= binomial(anum, p1[update])
        Tn[update] = t
        update = (n1 > 0) & (n1 < anum)
    
    return n1 == anum, Tn


#Assume population is 1000000, s=0.6
mean_fix_time=[]
size_range=np.logspace(2, 6, 15, base=10.0, dtype=np.uint64)

for anum in [0, 10, 200, 40000, 600000, 1000000]:
    fixations, times=one_simulation(anum, 0.6, repetitions = 1000)
    time_mean=times.mean()
    mean_fix_time.append(time_mean)
    
    
mean_fix_time=np.array(mean_fix_time)
allele_freq=np.array([0, 1000, 10000, 100000, 500000, 1000000])

fig, ax = plt.subplots()
x=allele_freq
y=mean_fix_time
ax.scatter(x,y)
ax.set(xlabel="Allele Number", ylabel="Mean Fixation Time")
fig.savefig("evolution3.png")
plt.close()





    