 

 
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
 NA
 
 
 
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

 
 
 

 