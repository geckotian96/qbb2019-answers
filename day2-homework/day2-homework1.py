#!/usr/bin/env python3

import sys

f=open(sys.argv[1])

for i, line in enumerate(f):
    if "DROME" and "FBgn" not in line:
        continue
    columns = line.split()
    flybase=columns[-1]
    uniport_name =columns[-2]
    
    print (flybase,"\t", uniport_name)
        
