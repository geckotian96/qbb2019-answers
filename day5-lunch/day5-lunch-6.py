#!/usr/bin/env python3

"""
./day5-lunch-6.py all.csv <gene of interest> K4me1.tab K4me3.tab K9me3.tab

"""
#output.tab
# # name - name field from bed, which should be unique
#    size - size of bed (sum of exon sizes
#    covered - # bases within exons covered by bigWig
#    sum - sum of values over all bases covered
#    mean0 - average over bases with non-covered bases counting as zeroes
#    mean - average over just covered bases


# use sum - sum of values over all bases covered as predictor to predict the gene expression FBtr0302347

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import scipy



df = pd.read_csv(sys.argv[1])


goi= df.loc[:, "gene_name"] == sys.argv[2]

fpkm_val=df.loc[goi,"male_10"] #print out the t_name with FPKM under same gene name
toi_name=df.loc[goi,"t_name"]

#print (toi_name)
print (fpkm_val)

fpkm_list=[]
toi_list=[]

for i, fpkm in enumerate(fpkm_val):
    fpkm_log=np.log(fpkm+1)
    fpkm_list.append(fpkm_log)

for q, toi_id in enumerate(toi_name):
    toi_list.append(toi_id)

#print (fpkm_list)
#print (toi_list)


def score_hm(name):
    cover_list=[]
    for i, line in enumerate(name):
        fields = line.rstrip("\n").split("\t")
        cover=fields[3]
        hm_toi=fields[0]
        if hm_toi in toi_list:
            cover_list.append(cover)
    return cover_list #have a list of selected transcript name


cover_list_K41m= score_hm(open(sys.argv[3]))
cover_list_K43m= score_hm(open(sys.argv[4]))
cover_list_K93m= score_hm(open(sys.argv[5]))



#print (len(fpkm_list), len(cover_list_K41m), len(cover_list_K43m), len(cover_list_K93m))
#combine all these lists into dictionary and make a new df
new_df=pd.DataFrame({"FPKM_Sxl":fpkm_list, "K4me1": cover_list_K41m, "K4me3": cover_list_K43m, "K9me3": cover_list_K93m})
#print (new_df)
model = sm.formula.ols(formula = "FPKM_Sxl ~ K4me1 + K4me3 + K9me3", data = new_df)

ols_results = model.fit()

print (ols_results.summary())

#####################################################################################

#regression for sxl is y=0.5126, no slope becuase 0 for all histome modifications 

for pos in range(len(fpkm_list)):
    ex_fpkm = 0.2690
    fpkm_list[pos] = abs(fpkm_list[pos]-0.2690)



fig, ax = plt.subplots()
ax.hist(fpkm_list, bins=5, color= "green", density=True) #bin=100 can divide the range into 100 columns, default is 10. Density??

#ax.plot(x1, y1, label="Normal distribution")
ax.set_xlabel ("log(FPKM+1) Residuals")
ax.set_ylabel ("Frequency")
fig.suptitle("Distribution of Residuals")


fig.savefig("log_residuals.png")
plt.close(fig)





