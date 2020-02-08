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

def time_vs_pop_simulation (pop_size):
    pop_size=int(pop_size)
    fixations, times = one_simulation (2*pop_size, 0.6, 1000) #assume s=0.6
    time_mean=times.mean()
    
    return time_mean 

#print (time_vs_pop_simulation (100000000))

mean_fix_time=[]
size_range=np.logspace(2, 6, 15, base=10.0, dtype=np.uint64)
#numpy.logspace(start, stop, num=50, endpoint=True, base=10.0, dtype=None, axis=0)[source]
for size in size_range:
    time2=time_vs_pop_simulation(size)
    mean_fix_time.append(time2)


mean_fix_time=np.array(mean_fix_time)

fig, ax = plt.subplots()
x=size_range
y=mean_fix_time
ax.scatter(x,y)
ax.set(xlabel="Population Size", ylabel="Mean Fixation Time")
fig.savefig("evolution2.png")
plt.close()





    