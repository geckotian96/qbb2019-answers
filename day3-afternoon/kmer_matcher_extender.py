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
target_kmers_stored={}
for ident, sequence in reader1:
    sequence=sequence.upper()
    target_kmers_stored[ident] = sequence
    for i in range(0, len(sequence) -k + 1 ):
        target_kmer = sequence[i:i+k]
        if target_kmer in target_kmers:
            target_kmers[target_kmer].append((i, ident))
        else:
            target_kmers[target_kmer]=[(i, ident)]
        

query_kmers = []
final_output_target = []
for ident, sequence in reader2:
     sequence=sequence.upper()
     for q in range(0, len(sequence) -k + 1 ):
         query_kmer = sequence[q:q+k]
         if query_kmer in target_kmers:
             target_value=target_kmers[query_kmer]
             for ti, tident in target_value:
                 stored_sequence = target_kmers_stored[tident]
                 end_target= ti + k -1
                 end_query= q + k -1
                 matched_initial_query=query_kmer
                 while True:
                     if len(stored_sequence) -1 <= end_target:
                         break
                     new_target_sequence = stored_sequence[end_target+1]
                     new_query_sequence=sequence[end_query+1]
                     if new_target_sequence == new_query_sequence:
                        end_target += 1
                        end_query += 1
                        matched_initial_query += stored_sequence[end_target]
                     else:
                        break 
                 final_output_target.append(matched_initial_query)

for sequence_output in sorted(final_output_target, key=len, reverse=True):
    print (sequence_output)

            
            
            
         
             
         
             
#for identity, target_starting_point in target_kmers[query_kmer]:
#print (identity, target_starting_point, q, query_kmer, sep="\t")
         
    

        
        
  


            
            
            
    
 #get key and value lambda can make the key list a specific order           
#for kmer, count in sorted(kmers.items(),
                          #key=lambda t: t[1]):
                          
    #print (kmer, count, sep="\t")
    