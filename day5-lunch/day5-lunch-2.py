#!/usr/bin/env python3

"""
Usage: ./day5-lunch-2.py <ctab> 

"""



#~/qbb2019-answers/results/stringtie/SRR072893/t_data.ctab

import sys
import numpy as np
import pandas as pd



for i, line in enumerate(open(sys.argv[1])):
   if i == 0:
       continue
   fields = line.rstrip("\n").split("\t")
   chrom=str(fields[1])
   strand=fields[2]
   start=int(fields[3])
   end=int(fields[4])
   t_name=fields[5]
   
   if strand == "+":
       pstart = start - 500
       pend = start +500
       if pstart < 0:
           pstart=0
       print (chrom, pstart, pend, t_name, sep="\t")
   else:
       pstart = end + 500
       pend = end - 500
       if pend < 0:
           pend=0
       print (chrom, pstart, pend, t_name, sep="\t")





