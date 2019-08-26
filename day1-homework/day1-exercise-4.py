#!/usr/bin/env python3

import sys

f = open (sys.argv[1])

lines = f.readlines()
for i in lines[0:10]:
    fields = i.split("\t")
    chrm = fields[2]
    print (chrm),





