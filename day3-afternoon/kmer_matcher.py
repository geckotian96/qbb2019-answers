#!/usr/bin/env python3

"""
map kmer in a FASTA file
kmer_matcher.py <target.fa> <query.fa> <k>

"""
#fasta is a py which can be reusable

from fasta import FASTAReader
import sys

reader1= FASTAReader(open(sys.argv[1]))
reader2= FASTAReader(open(sys.argv[2]))
k=int(sys.argv[3])

target_kmers={}

for ident, sequence in reader1:
    sequence1=sequence.upper()
    for i in range(0, len(sequence) -k + 1 ):
        target_kmer = sequence[i:i+k]
        if target_kmer in target_kmers:
            target_kmers[target_kmer].append((ident,i))
        else:
            target_kmers[target_kmer]=[(ident, i)]
        

query_kmers = []

for ident, sequence in reader2:
     sequence=sequence.upper()
     for q in range(0, len(sequence) -k + 1 ):
         query_kmer = sequence[q:q+k]
         if query_kmer in target_kmers:
             for identity, target_starting_point in target_kmers[query_kmer]:
                 print (identity, target_starting_point, q, query_kmer, sep="\t")
         
    

        
        
  


            
            
            
    
 #get key and value lambda can make the key list a specific order           
#for kmer, count in sorted(kmers.items(),
                          #key=lambda t: t[1]):
                          
    #print (kmer, count, sep="\t")
    