#!/usr/bin/env python3


"""
This aims to parse the file with only flybase name + uniport name. 
usage: ./day2-homework1.py fly.txt

note: fly.txt is downloaded from the instruction.

"""



import sys

f=open(sys.argv[1])

for i, line in enumerate(f):
    if "DROME" and "FBgn" not in line: 
        continue
    columns = line.split()    
    #last column -1 is the FBgn code
    flybase=columns[-1]     
    uniport_name =columns[-2] 
    
    #sep="" can adjust how you want to sep the things (space, whitespace, or tab)
    print (flybase, uniport_name, sep = "\t")
        
