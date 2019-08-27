#!/usr/bin/env python3


"""
This aims to parse the file with only flybase name + uniport name. 
usage: ./day2-homework1.py fly.txt

note: fly.txt is downloaded from the instruction.

"""



import sys

f=open(sys.argv[1])

for i, line in enumerate(f):
    if "DROME" and "FBgn" not in line: #if there are no Drome and FBgn in the line, it will pass those.
        continue
    columns = line.split()    #split the line based on whitespace
    flybase=columns[-1].     #grab the last column as flybase
    uniport_name =columns[-2] #grab the last second column as uniport name
    
    print (flybase,"\t", uniport_name). # \t sep those two with tab 
        
