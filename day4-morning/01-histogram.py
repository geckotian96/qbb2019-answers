#!/usr/bin/env python3

"""
USAGE: ./00-scatter.py <ctab>
plot fpkm
"""
#../results/stringtie/SRR072893/t_data.ctab


import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats 

fpkms=[]
for i, line in enumerate (open(sys.argv[1])):
    if i ==0:
        continue
    fields = line.rstrip("\n").split("\t")
    if  float(fields[-1]) > 0: 
        fpkms.append(float(fields[-1]))
#notice that fpkms field is a string. you need to convert to float first 
#the reason to use log is becuase most of the data gather in the 10000, so need to take log to further visualize the sub columns 
my_data = np.log2(fpkms)
# mu = 0
# sigma =1
# x = np.linspace (-15, 15, 100)   #range of the normal distribution with how many groups
# y = stats.norm.pdf (x, mu, sigma)
#a=-2.1, mu=5.8, signma = 2.8

mu1=0
sigma1=1
x1 = np.linspace (-15, 15, 100)   #range of the normal distribution with how many groups
y1= stats.norm.pdf (x1, mu1, sigma1)



a=-2.1
mu=5.8
sigma=2.8
x2 = np.linspace(-15, 15, 100)
y2= stats.skewnorm.pdf(x2, a, mu, sigma)





fig, ax = plt.subplots()
ax.hist(my_data, bins=100, density=True) #bin=100 can divide the range into 100 columns, default is 10. Density??

ax.plot(x1, y1, label="Normal distribution")
ax.legend()
ax.plot(x2, y2, label="Skew curve")
ax.legend()
ax.set_xlabel ("Log2(FPKM)")
ax.set_ylabel ("Probability")
fig.suptitle("Distribution Curve of FPKM")
plt.text(-15, 0.20, "a=-2.1, mu=5.8, signma=2.8")


fig.savefig("fpkms.png")
plt.close(fig)


#x = np.linspace(norm.ppf(0.01), --> x coordinace 
               #norm.ppf(0.99), 100)
#ax.plot(x, norm.pdf(x),
       #'r-', lw=5, alpha=0.6, label='norm pdf')