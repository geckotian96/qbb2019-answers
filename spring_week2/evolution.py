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

fix, time = one_simulation(anum=10, s=0, repetitions=1000)


fig, ax = plt.subplots()

sns.distplot(time[fix], bins=20)
#ax.axvline(time[fix].mean(), color='k', ls='--')
ax.set(xlabel="Time to fixation", ylabel="Freq.", title="Population=100")
fig.savefig("evolution.png")
plt.close()
