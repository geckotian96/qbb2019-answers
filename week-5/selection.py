#!/usr/bin/env python3

"""
Usage: ./.py alignmafft.out backtonucleotides.out
"""

import sys
from fasta import FASTAReader
import numpy as np
import matplotlib.pyplot as plt
import math



am_reader = FASTAReader(open(sys.argv[1])) 
bk_reader= FASTAReader(open(sys.argv[2]))

align_am={}
align_nt={}
ident_aa=[]
ident_nt=[]
for (aa_ident, aa_seq), (dna_ident, dna_seq) in zip(am_reader, bk_reader):
    align_am[aa_ident]=aa_seq
    align_nt[dna_ident]=dna_seq
    ident_aa.append(aa_ident)
    ident_nt.append(dna_ident)
    #print (align_am, align_nt)
    #print (ident)


nt_num=len(align_nt["M12294"])
#print (len(ident))

dD_list=[]
for i in range (0, nt_num, 3):
   
    ref_con=align_nt["M12294"][i:i+3]
    ref_aa=align_am[ident_aa[1]]
    
    dN = 0
    dS = 0
    
    for n in range(len(ident_nt)):
        sample_seq=align_nt[ident_nt[n]]
        sample_con=sample_seq[i:i+3]
        if ref_con != sample_con:
            ref_amino=ref_aa[int(i/3)]
            sample_aa=align_am[ident_aa[n]]
            sample_amino=sample_aa[int(i/3)]
            if sample_amino != ref_amino:
                dN += 1
            else:
                dS += 1
    dD=dN-dS
    dD_list.append(dD)
#print (dD_list)

mean = np.mean(dD_list)
std = np.std(dD_list)

#print ("The mean is ", mean, "and the std is ", std)

z_score=[]
for t in range (len(dD_list)):
     z_score.append(abs((dD_list[t]-mean)/std))

print ("The z score for each sample is", z_score)
# fig, ax = plt.subplots()
# plt.hist(z_score, bins=200, alpha = 0.3, color = "orange")
# ax.set_title("Distribution")
# ax.set_ylabel("Freq")
# ax.set_xlabel("Z score")
# fig.savefig("distribution.png")
# plt.close(fig)


#print (z_score)
            
            
            
            
        

    