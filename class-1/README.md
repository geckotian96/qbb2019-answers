 

 
###Part 1:
 
 time velveth velvet_class_1 15 -fastq -shortPaired reads_low_1.fastq reads_low_2.fastq
 
 real	0m0.327s
 user	0m0.482s
 sys	0m0.433s
 
 time velvetg velvet_class_1 
 
 real	0m0.154s
 user	0m0.148s
 sys	0m0.027s
 
lastz reference.fasta contigs.fa --chain --format=general > vh.out 

 
time spades.py --only-assembler -s reads_low_1.fastq -s reads_low_2.fastq -o spades_class_1 
 
 real	0m2.900s
 user	0m1.516s
 sys	0m0.870s
 
lastz reference.fasta contigs.fasta --chain --format=general > spades.out
 
 
 
###Part 2: MAP006
 I dont know how to use Spades to assemble it. Here is my log: 
 
 === Error correction and assembling warnings:
  * 0:00:09.410    80M / 3G    WARN    General                 (kmer_coverage_model.cpp   : 327)   Valley value was estimated improperly, reset to 2
  * 0:00:09.410    80M / 3G    WARN    General                 (kmer_coverage_model.cpp   : 366)   Failed to determine erroneous kmer threshold. Threshold set to: 2
  * 0:00:15.492    16M / 3G    WARN    General                 (simplification.cpp        : 479)   The determined erroneous connection coverage threshold may be determined improperly
  * 0:00:07.562    28M / 3G    WARN    General                 (kmer_coverage_model.cpp   : 327)   Valley value was estimated improperly, reset to 3
  * 0:00:07.562    28M / 3G    WARN    General                 (kmer_coverage_model.cpp   : 366)   Failed to determine erroneous kmer threshold. Threshold set to: 3
  * 0:00:08.469    16M / 3G    WARN    General                 (kmer_coverage_model.cpp   : 366)   Failed to determine erroneous kmer threshold. Threshold set to: 8
 ======= Warnings saved to /Users/cmdb/qbb2019-answers/class-1/MAP006_1/warnings.log
 
 
 but, if I do the velvet:
 
 time velveth MAP006_contig 15 -fasta -shortPaired MAP006.subset.fa 

 real	0m1.887s
 user	0m5.730s
 sys	0m0.611s
 
 time velvetg MAP006_contig
 real	0m16.156s
 user	0m21.109s
 sys	0m0.539s
 
 
 
 
###Part 3: Better Converage

 time velveth velvet_class_1_better_coverage 15 -fastq -shortPaired reads_1.fastq reads_2.fastq
 real	0m7.303s
 user	0m19.997s
 sys	0m0.843s
 
 time velvetg velvet_class_1_better_coverage
 real	0m10.951s
 user	0m26.196s
 sys	0m0.975s
 
lastz reference.fasta contigs.fa --chain --format=general > vh_better_coverage.out  
 
time spades.py --only-assembler -s reads_1.fastq -s reads_2.fastq -o spades_class_1_better_coverage

real	0m41.769s
user	1m17.237s
sys	0m2.478s 

lastz reference.fasta contigs.fasta --chain --format=general > spades_better_coverage.out  

 
 
 

 