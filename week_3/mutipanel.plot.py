#!/usr/bin/env python3
"""
Make a dotplot from lastz output file
Usage: ./script.py snpeffoutput.vcf 
"""


import sys
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats


list_rd=[]
list_qual=[]
list_af=[]
list_type=[]


for i, line in enumerate(open(sys.argv[1])):
    
    if i == 0:
        
        continue
    
    fields = line.rstrip("\n").split("\t")
    
    subfields=fields[-1].split(":")
    rd=subfields[1]
    list_rd.append(rd)
    qual=fields[5]
    list_qual.append(qual)
    list_qual=sorted(list_qual, reverse=True)
    subfields2=fields[7].split(";")
    af=subfields2[3][-1]
    list_af.append(af)
    list_af=sorted(list_af, reverse=True)
    subfields3=fields[-3].split(";")
    muttype=subfields3[-3][5:]
    
    list_type.append(muttype)
print (max(list_rd), min(list_rd))
print (max(list_qual))
print (min(list_qual))



allele0=0
allele1=0

for allele in list_af:
    if allele == "0":
        allele0 += 1
    if allele == "1":
        allele1 += 1
list_afnum=[allele0, allele1]        
print(list_afnum)

snp = 0
dele = 0
ins=0
list_mutnum=[]
for item in list_type:
    if "snp" in item:
        snp += 1
    elif "del" in item:
        dele += 1
    elif "ins" in item:
        ins += 1

list_mutnum = [snp, dele, ins]
#print (snp, dele, ins)

fig, (ax1, ax2, ax3, ax4) = plt.subplots(1,4)
fig.set_size_inches(44, 44)

ax1.hist(list_rd, range=[0,100], density=True, bins=20, color= "red")
ax1.set_title("Read Depth Distribution")
ax1.xaxis.set_ticks(np.arange(0,100,10))
ax1.set_xticklabels(["0", "10", "20","30","40","50","60","70","80","90","100"])
ax1.set_xlabel("Reading Depth")
ax1.set_ylabel("Probability")

ax2.hist(list_qual, range=[100,1000], bins=100, density=True, color= "blue")
ax2.xaxis.set_ticks(np.arange(100,1000,100))
ax2.set_xticklabels(["100","200", "300", "400","500", "600", "700", "800", "900", "1000"])
ax2.set_xlabel("Quality Score")
ax2.set_ylabel("Probability")
ax2.set_title("Genotype Quality Distribution")

ax3.bar(["allele = 0","allele=1"], list_afnum, label = "Allele Frequency Spectrum ", color= "orange")
ax3.set_title("Allele Frequency")
ax3.set_xlabel("Allele")
ax3.set_ylabel("Freq.")

ax4.bar(["SNP", "Deletion", "Insertion"],list_mutnum, label="Freqeuncy of Variants", color="salmon")
ax4.set_title("Variant Type Frequency")

#ax4.set_xlabel("Type")
# ax4.set.ylabel("Freq")
plt.tight_layout()
plt.subplots_adjust(top=0.9)
fig.savefig("muti-vcf.png")
plt.close(fig)




    
# chrI = 0
# chrII = 0
# chrIII = 0
# chrIV = 0
# chrV = 0
# chrVI = 0
# chrVII = 0
# chrVIII = 0
# chrIX = 0
# chrX = 0
# chrXI = 0
# chrXII = 0
# chrXIII = 0
# chrXIV = 0
# chrXV = 0
# chrXVI = 0
#
# for var in variants:
#     if "chrI" in variants:
#         chrI += 1
#     if "chrII" in variants:
#         chrII += 1
#     if "chrIII" in variants:
#         chrIII += 1
#     if "chrIV" in variants:
#         chrIV += 1
#     if "chrV" in variants:
#         chrV += 1
#     if "chrVI" in variants:
#         chrVI +=1
#     if "chrVII" in variants:
#         chrVII +=1
#     if "chrVIII" in variants:
#         chrVIII += 1
#     if "chrIX" in variants:
#         chrIX += 1
#     if "chrX" in variants:
#         chrX += 1
#     if "chrXI" in variants:
#         chrXI += 1
#     if "chrXII" in variants:
#         chrXII += 1
#     if "chrXIII" in variants:
#         chrXIII += 1
#     if "chrXIV" in variants:
#         chrXIV += 1
#     if "chrXV" in variants:
#         chrXV += 1
#     if chrXVI in variants:
#         chrXVI += 1
#
# print (chrI)
#

    
