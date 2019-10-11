 tar -xf g1e.tar.xz 
 
 
bowtie2-build -f chr19.fa chr19index
  

bowtie2 -x chr19index -U CTCF_ER4.fastq -S CTCF_ER4.sam 

bowtie2 -x chr19index -U CTCF_G1E.fastq -S CTCF_G1E.sam 

bowtie2 -x chr19index -U input_G1E.fastq -S input_G1E.sam 
bowtie2 -x chr19index -U input_ER4.fastq -S input_ER4.sam

samtools view -Sb  <SAMFILE>  >  <BAMFILE>
samtools view -Sb  CTCF_ER4.sam   >  CTCF_ER4.bam
samtools view -Sb  CTCF_G1E.sam   >  CTCF_G1E.bam
samtools view -Sb  input_G1E.sam  >  input_G1E.bam
samtools view -Sb  input_ER4.sam  >  input_ER4.bam


macs2 callpeak -t CTCF_ER4.bam -c input_ER4.bam -n ER4_macs2 -f BAM
macs2 callpeak -t CTCF_G1E.bam -c input_G1E.bam -n G1E_macs2 -f BAM

Each feature in A is compared to B, -v report those entries in A that have no overlap in B.
G1E: before diff; ER4: after diff
bedtools intersect -a G1E_macs2_peaks.narrowPeak -b ER4_macs2_peaks.narrowPeak -v > CTCFbinding_lost.bed (lost)
bedtools intersect -a ER4_macs2_peaks.narrowPeak -b G1E_macs2_peaks.narrowPeak -v > CTCFbinding_gain.bed (gain)

bedtools intersect -a ER4_macs2_peaks.narrowPeak -b Mus_musculus.GRCm38.94_features.bed > overlap_ER4.bed


bedtools intersect -a G1E_macs2_peaks.narrowPeak -b Mus_musculus.GRCm38.94_features.bed > overlap_G1E.bed

grep "exon"  Mus_musculus.GRCm38.94_features.bed > exon.mouse.bed


bedtools intersect -a G1E_macs2_peaks.narrowPeak -b intron.mouse.bed | wc -l  => 301
bedtools intersect -a G1E_macs2_peaks.narrowPeak -b exon.mouse.bed | wc -l     => 117
bedtools intersect -a G1E_macs2_peaks.narrowPeak -b promoter.mouse.bed | wc -l => 51

bedtools intersect -a ER4_macs2_peaks.narrowPeak -b intron.mouse.bed | wc -l =>349
bedtools intersect -a ER4_macs2_peaks.narrowPeak -b exon.mouse.bed | wc -l     => 144
bedtools intersect -a ER4_macs2_peaks.narrowPeak -b promoter.mouse.bed | wc -l => 72

wc CTCFbinding_gain.bed  => 130
wc -l CTCFbinding_lost.bed  => 56







