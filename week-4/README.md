 
plink --vcf BYxRM_segs_saccer3.bam.simplified.vcf --freq --family --allow-extra-chr

./histogram.py plink.frq.strat

plink --file BYxRM_segs_saccer3.bam.simplified.vcf --assoc

plink --allow-extra-chr --allow-no-sex --mind --vcf BYxRM_segs_saccer3.bam.simplified.vcf --pheno phenotypes.data --all-pheno  --assoc --out phenoassoc

./manhattan.py phenoassoc.*.qassoc