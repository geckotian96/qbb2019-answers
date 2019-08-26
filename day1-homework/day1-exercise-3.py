#!/usr/bin/env python3

import sys

f = open (sys.argv[1])

count = 0 
for lines in f:
    fields = lines.rstrip("\n").split("\t")
    if "NH:i:1" in fields:
        count += 1
    
print (count)
