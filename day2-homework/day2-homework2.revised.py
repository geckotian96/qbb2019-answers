#!/usr/bin/env python3


"""
This aims to traslate the ctab file with the name from uniport mapping file with uniport name 
usage: ./day2-homework1.py <mapping file i.e. fly.txt> <c_tab file> <argument 3>*

About argument3:
if "None": the nomatch line will be bypassed
if not typing "None": the gene_name will should the name typed in argument 3 (i.e nomatch etc...).



"""

import sys


f=open(sys.argv[1]) #mapping file
f2=open(sys.argv[2]) #c_tab file


gene_dictionary = {}

for line in f:
    columns = line.rstrip("\n").split("\t")    
    flybase=columns[0]
    uniport_name =columns[1]
    gene_dictionary[flybase]=uniport_name #here you build a dict where flybase is the key and its repective uniport name is the value.
    

for line in f2:
    columns = line.rstrip("\n").split("\t")    
    flybase_inctab=columns[-4]
    gene_name = columns[-3]

    if  flybase_inctab in gene_dictionary: #if..in can check if the key in the keys of dict
        line.rstrip("\n").split("\t")   
        uniprot_name = gene_dictionary[flybase_inctab]
        new_line = line.replace(gene_name, uniprot_name)
        print (new_line)
   
    elif flybase_inctab not in gene_dictionary and sys.argv[3] != "None": #replace the gene_name based on the commander line
        new_line = line.replace(gene_name, sys.argv[3])
        print (new_line)
        
    elif flybase_inctab not in gene_dictionary and sys.argv[3] == "None":
        continue
        
    

    
    



 
        