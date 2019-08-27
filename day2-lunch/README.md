
head -n 40000 SRR072893.fastq > SRR072893.10K.fastq

fastqc SRR072893.fastq > 893.html

hisat2 -p 4 -x ../genomes/BDGP6 -U SRR072893.10k.fastq -S SRR072893hisat2.sam

samtools sort -o SRR072893.bam SRR072893hisat2.sam 

samtools index SRR072893.bam SRR072893bam.index

(samtools index SRR072893.bam)

stringtie SRR072893.bam -G ../genomes/BDGP6.Ensembl.81.gtf  -o SRR072893.gtf -p 4 -e -B
