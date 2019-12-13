#!/usr/bin/env python2
import sys
import hifive
import numpy


rna_bin= open(sys.argv[1])
enhancer= open(sys.argv[2]) 

rna_lib={}
enhancer_lib={}

for i, line in enumerate(rna_bin):
    if i == 0:
        continue
    fields= line.rstrip("\n").split("\t")
    if int(fields[1]) >= 5000000 and int(fields[2])<=40000000:
        index = (int(fields[2])-5000000)/5000
        rna_lib[index] = float(fields[4])
#print (rna_lib)

        
for i2, line2 in enumerate(enhancer):
    if i2 == 0:
        continue
    fields2=line2.rstrip("\n").split("\t")
    if int(fields2[1]) >= 5000000 and int(fields2[2])<=40000000:
        index2 = (int(fields2[2])-5000000)/5000
        enhancer_lib[index2] = float(fields2[4])
#print (enhancer_lib)


hic = hifive.HiC('PROJECT_FNAME', 'r')
data = hic.cis_heatmap(chrom='chr10', start=5000000, stop=40000000, binsize=5000, datatype='fend', arraytype='full')
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = numpy.log(data[:, :, 0] + 0.1)
data -= numpy.amin(data)

#print (len(data),len(data.T))
#print (data)
#print (data[1][2])
#
key2=[]
key3=[]
for enhancer_key in enhancer_lib:
     key2.append(enhancer_key)

for rna_key in rna_lib:
     key3.append(rna_key)

predic_lib={}
for index3 in key3:
    predic=0
    for index4 in key2:
        predic += float(enhancer_lib[index4])*data[index3][index4]
    predic_lib[index3]=predic
    print index3, predic

rna_exp=[]
predic_val=[]
for item in key3:
    rna_exp.append(float(rna_lib[item]))
    predic_val.append(float(predic_lib[item]))
    
rna=numpy.array(rna_exp)
predic_val_array=numpy.array(predic_val)


coeff=numpy.corrcoef(rna, predic_val_array)[0,1]

print "R=", coeff #r=0.44
    
    














