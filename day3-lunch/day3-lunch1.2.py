#!/usr/bin/env python3

import sys


f=open(sys.argv[1])
mutation=21378950


gene_dictionary= {}
gene_list = []
for line in f:
    columns = line.rstrip("\n").split()    
    flybase_start=int(columns[3])
    flybase_end=int(columns[4])
    gene_name =columns[13]
    gene_dictionary[(flybase_start, flybase_end)]=gene_name
    
    gene_list.append((flybase_start, flybase_end))
   




#print (list_sorted) pass
lo=0
hi=len(gene_list)-1
mid=0
number_iter=0
list2=[]
while lo < hi:
    
    mid =int((hi+lo)/2)
    number_iter += number_iter+1
    if mutation < gene_list[mid][0]:
        gene_list = gene_list[:mid]
    elif mutation > gene_list[mid][1]:
        gene_list = gene_list[(mid+1):]
    else:
        break
    
    hi=len(gene_list)-1

gene_key= gene_dictionary[gene_list[0]]

listgene=list(gene_list[0])
distance1=abs((listgene[0])-mutation)
distance2=abs((listgene[1])-mutation)

if distance1 > distance2:
    print (gene_key, distance2, number_iter)
else:
    print (gene_key, distance1, number_iter)





        
    


    

