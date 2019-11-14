#!/usr/bin/env python3

import sys 
import numpy as np
import scipy.cluster.hierarchy as hac
import matplotlib.pyplot as plt
from scipy.cluster.vq import vq, kmeans, whiten


file1=open(sys.argv[1])
gene_list=[]
expression_val=[]
for i, line in enumerate (file1):
    if i == 0:
        continue
    fields = line.rstrip("\n").split("\t")
    gene=fields[0]
    gene_list.append(gene)
    cfu_poly=fields[1:3]
   
    expression=[float(n) for n in cfu_poly]
    expression_val.append(expression)

#print (expression_val)
a=np.array(expression_val)
whitened=whiten(a)
e, f =kmeans(whitened,2)


fig, ax = plt.subplots(figsize=(6,6))
plt.title("K-means of CFU & poly")
plt.scatter(whitened[:, 0], whitened[:, 1], c="b")
plt.scatter(e[:,0],e[:,1], c='red')
fig.savefig("kmeans.png")
plt.close()