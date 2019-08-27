#!/usr/bin/env python3


"""
This aims to traslate the ctab file with the name from uniport mapping file with uniport name 
usage: ./day2-homework1.py <mapping file i.e. fly.txt> <c_tab file> <argument 3:nothing by default>

note: 

"""
import sys


f=open(sys.argv[1])
f2=open(sys.argv[2])


gene_dictionary = {}

for i, line in enumerate(f):
    columns = line.rstrip("\n").split("\t")    
    flybase=columns[0]
    uniport_name =columns[1]
    gene_dictionary[flybase]=uniport_name
    

for i, line in enumerate(f2):
    columns = line.rstrip("\n").split("\t")    
    flybase_inctab=columns[8]
    line = line.rstrip("\n")
    if  flybase_inctab in gene_dictionary: #if..in can check if the key in the keys of dict
        respective_uniport_name = gene_dictionary[flybase_inctab]
        print (line, respective_uniport_name, sep="\t")
    elif flybase_inctab not in gene_dictionary and sys.argv[3] == "nomatch":
        print (line, "nomatch", sep="\t") 
    elif flybase_inctab not in gene_dictionary and sys.argv[3] == "nothing":
        continue
        
    
    
    



 
        