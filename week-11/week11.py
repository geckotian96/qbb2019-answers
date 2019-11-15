#!/usr/bin/env python3

import sys 
#import numpy as np
import scanpy.api as sc 
#import scipy.stats as stats


sc.set_figure_params(dpi=80, color_map='viridis')
sc.settings.verbosity = 2
sc.logging.print_versions()

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

sc.pp.filter_genes(adata, min_counts=1)  # only consider genes with more than 1 count
sc.pp.normalize_per_cell(adata)


# sc.tl.pca(adata,n_comps=50, zero_center=True,
# svd_solver='auto', random_state=0, return_info=False,
# use_highly_variable=None, dtype='float32', copy=False,
# chunked=False, chunk_size=None)
#
# sc.pl.pca(adata,edges_color='grey', projection='2d',legend_fontweight='bold',
# legend_loc='right margin', title='PCA wo. filter')
#
# sc.pl.pca_loadings(adata)

sc.pp.neighbors(adata)
sc.tl.umap(adata)
sc.tl.louvain(adata)
sc.pl.umap(adata, color=["louvain", "Hbb-bs"])


#sc.tl.tsne(adata)
#sc.pl.tsne(adata,color=["louvain", "Rps9"]) 

#sc.tl.rank_genes_groups(adata,"louvain", groups=["1","6", "9", "7"], method="logreg")
#sc.pl.rank_genes_groups(adata, n_genes=10)

#sc.tl.rank_genes_groups(adata,"louvain", groups=["13"], method="t-test")
#sc.pl.rank_genes_groups(adata, n_genes=10) #Hbb-bs

