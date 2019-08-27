#!/bin/bash

GENOME=../genomes/BDGP6

ANNOTATION=../genomes/BDGP6.Ensembl.81.gtf

THREADS=4


for SAMPLE in SRR072893	SRR072903 SRR072905 SRR072915

do
	echo "*** Processing $SAMPLE"
	cp /Users/cmdb/qbb2019-answers/rawdata/$SAMPLE.fastq
	fastqc $SAMPLE.fastq > $SAMPLE.html
  	hisat2 -p $THREADS -x $GENOME -U $SAMPLE.fastq -S $SAMPLE.sam
	samtools sort -o $SAMPLE.bam $SAMPLE.sam
  	samtools index $SAMPLE.bam
    stringtie $SAMPLE.bam -G $ANNOTATION -o $SAMPLE.gtf -p $THREADS -e -B
done


