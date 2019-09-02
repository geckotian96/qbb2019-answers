
head -n 40000 SRR072893.fastq > SRR072893.10K.fastq

fastqc SRR072893.fastq > 893.html

hisat2 -p 4 -x ../genomes/BDGP6 -U SRR072893.10k.fastq -S SRR072893hisat2.sam

samtools sort -o SRR072893.bam SRR072893hisat2.sam 

samtools index SRR072893.bam SRR072893bam.index

(samtools index SRR072893.bam)

stringtie SRR072893.bam -G ../genomes/BDGP6.Ensembl.81.gtf  -o SRR072893.gtf -p 4 -e -B


Q3: the presenter's code is: grep "SRR072893" SRR072893.sam | cut -f 3 | sort | uniq -c > sorted.SRR072893.sam 

grep "SRR072893" means extracting out the lines contains SRR072893. This indicate successful alignment.

cut -f 3 means take out the column #3 which is the chromosome column (2L, 2R, ...)

sort can make the chromosomes with the same name gather together 

uniq -c can count how many repeats of each chromosome. 


Q4: sam file has 11 mandartory fields(columns) therefore, the number of columns in each line in the same files should be at least 11. After the 11th columns, optional fields will come
 in which the format will be TAG:TYPE:VALUE. 

For example, if NF (the total number of columns in a line) is 12, the optional column is Y? is reserved for end users.

Compared to NF = 20, NF = 21 has the entra column of ZS which is also reserved for end users. 

The exact meanings of TAG can be found in the Optional Field Manual from Day1-Homework link. 


 
