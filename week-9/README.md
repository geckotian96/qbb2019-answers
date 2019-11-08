sort -rnk 5 ER4_peaks.narrowPeak | head -100 > sorted_ER4_narrowpeak

bedtools getfasta [OPTIONS] -fi <input FASTA> -bed <BED/GFF/VCF>

bedtools getfasta  -fi chr19.fa -bed sorted_ER4_narrowpeak > sorted_seq_ER4.narrowpeak 

meme-chip  -o output -meme-maxw 20 -db JASPAR_CORE_2016.meme sorted_seq_ER4.narrowpeak 

/Users/cmdb/qbb2019-answers/week-9/output/meme_out

open logo1.png

/Users/cmdb/qbb2019-answers/week-9/output/fimo_out_1/fimo.gff

bedtools intersect -wb -a fimo.gff -b ER4_narrowpeak  > regionoverlap.out


