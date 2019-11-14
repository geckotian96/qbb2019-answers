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
    expression=[float(n) for n in fields[1:]]
    expression_val.append(expression)

#print (len(gene_list))
  
a=np.array(expression_val)
gene_list2=np.array(gene_list)
z=hac.linkage(a, "average")
order=hac.leaves_list(z)
#gene_names_ordered=gene_list2[order]
#print (gene_names_ordered)

b=np.transpose(a)
c_link=hac.linkage(b, "average")
cell_order=hac.leaves_list(c_link)
#print (cell_order) 120435

expression_cluster=a[order]
#print (a)
#print (expression_clustered)
trans_exp=np.transpose(expression_cluster)
cell_cluster=trans_exp[cell_order]
#print (cell_cluster)
trans_cell_cluster=np.transpose(cell_cluster)
#print (a)
#print (trans_cell_cluster)

average=np.average(trans_cell_cluster)
std=np.std(trans_cell_cluster)
z_score_normalized=(trans_cell_cluster-average)/std
#print (z_score_normalized)

##########################################
#cell_types=["CFU", "poly", "unk", "int", "mys", "mid"] order:120435
order_cell_names=["unk", "CFU", "poly", "mys", "int", "mid"]
fig, ax = plt.subplots(figsize=(100,100))
im = ax.imshow(z_score_normalized)
ax.set_xticks(np.arange(len(order_cell_names)))
ax.set_yticks(np.arange(len(gene_list)))
plt.setp(ax.get_xticklabels(cell_types), rotation=45,ha="right", rotation_mode="anchor")
ax.set_xticklabels(order_cell_names, rotation=45)
ax.set_title("Heatmap")
#fig.tight_layout()
fig.savefig("Heatmap.png")
plt.close(fig)
##########################################

fig1, ax1=plt.subplots(figsize=(6,6))
hac.dendrogram(c_link, labels=order_cell_names)
plt.title("Dendrogram of cell types")
plt.xlabel("Cell types")
fig1.savefig("Dendrogram.png")
plt.close(fig1)

#########################################


