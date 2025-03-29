## OSS-MPAW

This github repo is the artifact dataset for the manuscript "An Analysis of Malicious Packages in Open-Source Software in the Wild".

This project has built and curate the largest dataset of 24,356 malicious packages from scattered online sources. Then, the knowledge graph represents the OSS malware corpus and SSC attack campaigns behind malicious packages.

## What can you get raw data from OSS-MPAW:

1. Dataset of malicious software packages.
2. Dataset of security reports.
3. Dataset of security reports' IoC.
4. Dataset of duplicated groups.
5. Dataset of  similar groups.
6. Dataset of dependent-hidden  groups.
7. Dataset of co-existing groups.

*You can obtain full raw data by email: <wendyzhouxian@gmail.com>*

## Documentation

Our repo contains the basic information of malicious packages.

**Data collection** contains codes/scripts that download malicious packages and security reports.

- malware folder: Our dataset and the web crawler for malicious packages
  - [malware.xlsx]  - This dataset contains duplicates across different sources, primarily corresponding to the dataset studied in the paper for RQ1.
  - [malware_deduplicated.xlsx] - Fully Deduplicated dataset.
  - [demo.xlsx] - Temporary datasets are used solely for testing crawling scripts.
- Report folder: Our report dataset (1533 reports and corresponding URLs) and the codes/scripts that collect security reports.
- IoC folder: Our IoC dataset.

**Package Info** contains codes/scripts that extract basic information of malicious packages.

- **[get_evolution]** - Sort packages within each group according to their release time and obtain the evolutions
- **[active_time]** - Get the active time of each group

**KG** contains codes/scripts that generate groups of malicious packages

- [embedding_cluster] - In Similar_Edge Floder, classify similar groups based on embeddings and clustering.
- Duplicated_Edge - Store datasets of duplicated groups and provide scripts for generation and analysis for RQ1.
  - [get_delete_overallMR.py] - A utility to compute the missing rate in the dataset, identifying fields with incomplete information.
  - [occurrences] - Statistical analysis of the occurrence frequencies of three representative OSS packages.
  - [overlap_matrix] - A methodology and computed results for measuring data overlap among different online data sources.

ML contains data and scripts for training machine learning and deep learning models, with and without the help of clustering.**

- [ML_BaseVs.Cluster] - Scripts for generating training/testing sets and running training
- [legiti_embeddings_js] - A dataset containing precomputed embedding vectors representing benign (non-malicious) packages.
- [malware_clusters_results_js] - A collection of malicious packages that have been grouped into clusters using unsupervised methods.
- [mal_embeddings_js_480] - A separate dataset of 480 malicious packages that have not been assigned to any cluster.
- [test_train] - folders for generated training and testing datasets during runtime


📌 All scripts in this repository are ready to run ✅

📁 We’ve embedded relative paths in most scripts to make testing and deployment easier.
However, some scripts may require manual adjustment of absolute paths depending on your local setup.

🔍 Please double-check the paths before running. Thanks for your understanding and support!
