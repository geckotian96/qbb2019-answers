#!/usr/bin/env python3

'''
Usage: ./manhattan.py phenoassoc.*.qassoc

'''

import sys
import matplotlib.pyplot as plt
import numpy as np
import statistics

filelist=[]
for files in sys.argv[1:]:
    
    fields=files.split(".")
    pheno=fields[1]
    filelist.append(files)
    #print (pheno)
  
    for name in filelist:
        dicval={}

        for i, line in enumerate (open(name)):

            if i == 0:
                continue
            columns= line.rstrip("\n").split()
            #print (columns[-1])
            if columns[-1] != "NA":
                pval=float(columns[-1])
                bp=int(columns[2])
                chrm=columns[0]
                if chrm not in dicval:
                    dicval[chrm]=[(bp,pval)]
                else:
                    dicval[chrm].append((bp, pval))
        #print (dicval)
                
        xaxis=[]

        for value, chromosome in enumerate (dicval):
            
            x, y= zip(*dicval[chromosome])
            y = np.array(-np.log10(y))
            x = np.array(x)
           
            if chromosome == "26":
                chromosome = "chrXXVI"
            elif chromosome == "23":
                chromosome = "chrXXIII"
            xaxis.append(chromosome)
           
        # print (x, y)
        # print (xaxis)
            
       
        fig, axes = plt.subplots(figsize=(10,10))
        fig.suptitle ("{}".format(name))
        sig= y>5
        plt.scatter(x[y>5], y[y>5], color="red", alpha=0.25)
        plt.scatter(x, y, color = "black", alpha=0.25)
        axes.set_xticklabels(xaxis)
        fig.savefig("Manhattan_{}.png".format(name))
        plt.close(fig)
#chrm ticks are not all present...some data seem to be missing 



      
     