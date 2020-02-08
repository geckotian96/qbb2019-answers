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


#Assume population is 1000000, starting allele freq=500000
mean_time_list=[]
size_range=np.logspace(-6, 0, 15, base=10.0, dtype=np.float64)

for s in size_range:
    fix, time = one_simulation (300000, s, 1000)
    mean_time=time.mean()
    mean_time_list.append(mean_time)

mean_time_list=np.array(mean_time_list)

    


fig, ax = plt.subplots()
x=np.array(size_range)
y=mean_time_list
ax.scatter(x,y)
ax.set(xlabel="Selection (Favorable to Against)", ylabel="Mean Fixation Time", title="Starting Allele Number = 300000, Population = 1000000")
fig.savefig("evolution4.png")
plt.close()





    