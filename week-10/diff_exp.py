#!/usr/bin/env python3


# group unk, CFU // POLY, MYS (3,1,2,5)
# "standard Paired t test on normalized intensity with P value 􏰄0.05 followed by ratio change (ratio of normalized intensity 􏰅2.0 or 􏰄0.5) was used to generate the list of genes with significant change in expression profile during osteoblast differentiation."

import sys 
import numpy as np
import scipy.cluster.hierarchy as hac
import matplotlib.pyplot as plt
from scipy.cluster.vq import vq, kmeans, whiten
import scipy.stats as stats

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
gene_names_ordered=gene_list2[order]
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

gene_name=[]
upreg_late=[]
lateup_genes=[]
for i in range(500): #500 genes
    fields = line.rstrip("\n").split("\t")
    cfu=trans_cell_cluster[i,0]
    unk=trans_cell_cluster[i,1]
    poly=trans_cell_cluster[i,2]
    mys=trans_cell_cluster[i,3]
    early=(cfu+unk)/2
    late=(poly+mys)/2
    t, p_val=stats.ttest_rel([cfu, unk], [poly, mys])
    
    
    # if early/late >=2 or early/late <=0.5:
#         if p_val < 0.05:
#             gene=gene_names_ordered[i]
#             gene_name.append(gene)


    if p_val < 0.05 and early/late <=0.5:
        gene2=gene_names_ordered[i]
        upreg_late.append(early/late)
        lateup_genes.append(gene2)
        


idx=np.argmin(upreg_late)

#print (min(upreg_late)) 0.025225125741901753
#print (minidx)

most_lateup=gene_names_ordered[idx]

print (most_lateup) 
print (lateup_genes)
