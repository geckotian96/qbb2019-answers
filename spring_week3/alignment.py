#!/usr/bin/env python3#!/usr/bin/env python3

import sys 
import numpy as np

s1="CATAAACCCTGGCGCGCTCGCGGCCCGGCACTCTTCTGGTCCCCACAGACTCAGAGAGAACCCACCATGGTGCTGTCTCCTGCCGACAAGACCAACGTCAAGGCCGCCTGGGGTAAGGTCGGCGCGCACGCTGGCGAGTATGGTGCGGAGGCCCTGGAGAGGATGTTCCTGTCCTTCCCCACCACCAAGACCTACTTCCCGCACTTCGACCTGAGCCACGGCTCTGCCCAGGTTAAGGGCCACGGCAAGAAGGTGGCCGACGCGCTGACCAACGCCGTGGCGCACGTGGACGACATGCCCAACGCGCTGTCCGCCCTGAGCGACCTGCACGCGCACAAGCTTCGGGTGGACCCGGTCAACTTCAAGCTCCTAAGCCACTGCCTGCTGGTGACCCTGGCCGCCCACCTCCCCGCCGAGTTCACCCCTGCGGTGCACGCCTCCCTGGACAAGTTCCTGGCTTCTGTGAGCACCGTGCTGACCTCCAAATACCGTTAAGCTGGAGCCTCGGTGGCCATGCTTCTTGCCCCTTGGGCCTCCCCCCAGCCCCTCCTCCCCTTCCTGCACCCGTACCCCCGTGGTCTTTGAATAAAGTCTGAGTGGGCGGCAAAAAAAAAAAAAAAAAAAAAA"
s2="GGGGCTGCCAACACAGAGGTGCAACCATGGTGCTGTCCGCTGCTGACAAGAACAACGTCAAGGGCATCTTCACCAAAATCGCCGGCCATGCTGAGGAGTATGGCGCCGAGACCCTGGAAAGGATGTTCACCACCTACCCCCCAACCAAGACCTACTTCCCCCACTTCGATCTGTCACACGGCTCCGCTCAGATCAAGGGGCACGGCAAGAAGGTAGTGGCTGCCTTGATCGAGGCTGCCAACCACATTGATGACATCGCCGGCACCCTCTCCAAGCTCAGCGACCTCCATGCCCACAAGCTCCGCGTGGACCCTGTCAACTTCAAACTCCTGGGCCAATGCTTCCTGGTGGTGGTGGCCATCCACCACCCTGCTGCCCTGACCCCGGAGGTCCATGCTTCCCTGGACAAGTTCTTGTGCGCCGTGGGCACTGTGCTGACCGCCAAGTACCGTTAAGACGGCACGGTGGCTAGAGCTGGGGCCAACCCATCGCCAGCCCTCCGACAGCGAGCAGCCAAATGAGATGAAATAAAATCTGTTGCATTTGTGCTCCAG"


#initializing 
def zeros(rows, cols):
    val=[]
    for x in range(rows):
        val.append([])
        
        for y in range(cols):
            val[-1].append(0)
        
    return val
    
#print (zeros(3,3))

gap_penalty=-300

def match_score (a, b):
    if a==b=="A" or a==b=="T":
        return 91
    elif a==b=="C" or a==b=="G":
        return 100
    elif a =="A" and b =="C":
        return -114
    elif a =="A" and b=="G":
        return -31
    elif a=="A" and b=="T":
        return -123
    elif a =="C" and b=="A":
        return -114
    elif a=="G" and b=="A":
        return -31
    elif a=="T" and b == "A":
        return -123
    elif a =="C" and b =="T":
        return -31
    elif a =="T" and b =="C":
        return -31
    elif a == "T" and b=="G":
        return -114
    elif a =="G" and b =="T":
        return -114
    elif a =="C" and b=="G":
        return -125
    elif a=="G" and b=="C":
        return -125
#print (match_score("G", "T"))
    


def algor(seq1, seq2):
    n=len(seq1)
    m=len(seq2)
    
    score = zeros(m+1, n+1)
    
    for i in range(0, m + 1):
        score[i][0] = gap_penalty * i
    
    for j in range(0, n+1):
        score[i][0] = gap_penalty * j
        
            
    #return score
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            
            deletion=score[i-1][j]+gap_penalty
            insertion=score[i][j-1]+gap_penalty
            match=score[i-1][j-1]+match_score(s1[j-1], s2[i-1])
            
            score[i][j]=max(deletion, insertion, match)
            
    

#print (algor(s1, s2))
        
    a1=""
    a2=""

    i=m
    j=n

    while i > 0 and j > 0:
        current=score[i][j]
        diagonal=score[i-1][j-1]
        up=score[i-1][j] 
        left=score[i][j-1] 
        
        if current == diagonal + match_score(s1[j-1], s2[i-1]):
            a1 += s1[j-1]
            a2 += s2[i-1]
            i =i-1
            j =j-1
            
        elif current == up + gap_penalty:  #deletion on S1
            a1 += "-"
            a2 += s2[i-1]
            i=i-1
            
        elif current == left + gap_penalty: #insertion on S1
            a1 += s1[j-1]
            a2 += "-"
            j =j-1
        
    return (score, a1[::-1], a2[::-1])
    
score, align1, align2 = algor(s1, s2)

print (align1+"\n"+align2)


        




