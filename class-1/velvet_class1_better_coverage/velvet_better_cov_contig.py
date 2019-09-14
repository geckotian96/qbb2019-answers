#!/usr/bin/env python3

"""
9_13 class 

Compute the number of contigs, minimum/maximum/average contig length, and N50

Usage: ./name.py contigs.fasta/fa
 
"""



import sys 
from fasta import FASTAReader
from statistics import mean

reader = FASTAReader(open(sys.argv[1]))


 
sequence_list=[]
length_seq = []
accum_length = 0
for ident, seq in reader:
    sequence_list.append(seq)
    
    
        
    
#print (len(sequence_list))
  
for element in sequence_list:
        length_seq.append(len(element))
        
         
    
hi=max(length_seq)
lo=min(length_seq)
avg=sum(length_seq)/len(sequence_list)


print ("The longest, shortest and the average length of contigs are ", hi, lo, avg, " respectively.") 


sorted_sequence_list= sorted(sequence_list, key=len, reverse=True)
sorted_length_seq=sorted(length_seq, reverse= True)

count = 0 
for i, item in enumerate(sorted_length_seq):
    count += item
    if count >= sum(sorted_length_seq)/2:
        break
#print (sorted_sequence_list)
#print (i)
print ("The seq of N50 is ", sorted_sequence_list[i])
print ("The length of N50 is ", len(sorted_sequence_list[i]),".")
        

        
          
#print(count_contigs)




