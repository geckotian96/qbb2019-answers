xblastn -query week5_query.fa -db nr -evalue 1e-4 -out week5_sequence -outfmt 6 -max_target_seqs 1000 -remote 

xblastn -query week5_query.fa -db nr -evalue 1e-4 -out week5_sequences.fa -ungapped -outfmt 6 -num_alignments 1000 -remote

xblastn -query week5_query.fa -db nr -out week5_blast.out -evalue 0.0001 -ungapped -num_alignments 1000 -outfmt 6 -remote

blastn -query week5_query.fa -db nr -out week5_blast.out -evalue 0.0001 -ungapped -num_alignments 1000 -outfmt "6 sseqid sseq" -remote

sed ‘s/-//g’ blast_out.tab > query.out
sed "s/^/>/" query.out > querycleaned.out
awk ‘{print $1"\n”$3}’ querycleaned.out > finalquery.out

transeq -seqeunce finalquery.out -outseq aminoacid.out
mafft aminoacid.out > alignmafft.out
