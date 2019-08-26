#!/usr/bin/env python3

import sys

f = open (sys.argv[1])
count = 0 
for line in f:
    fields= line.split("\t")
    if fields[2] != "*":
        count += 1
        
print (count)    

#count = 0 
#for item in fields[2]:
    #if item != "*":
        #count += 1 

#print (count)
    



