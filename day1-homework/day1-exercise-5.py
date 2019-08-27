#!/usr/bin/env python3

import sys

f = open (sys.argv[1])

count = 0 
map_total = 0

for line in f:
    fields= line.split("\t")
    count += 1
    map_total += int(fields[4])

average=map_total/count

print (average)

   

        

 
    
    
