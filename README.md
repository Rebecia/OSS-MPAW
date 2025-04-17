## OSS-MPAW

This github repo is the artifact dataset for the manuscript "An Analysis of Malicious Packages in Open-Source Software in the Wild".

This project has built and curate the largest dataset of 24,356 malicious packages from scattered online sources. Then, the knowledge graph represents the OSS malware corpus and SSC attack campaigns behind malicious packages.

You can cite it using:

```
@INPROCEEDINGS{dsn-2025,
author={Xiaoyan Zhou and Ying Zhang and Wenjia Niu and Jiqiang Liu  and Haining Wang  and Qiang Li },
booktitle={2025 55th Annual IEEE/IFIP International Conference on Dependable Systems and Networks (DSN)},
title={An Analysis of Malicious Packages in Open-Source Software in the Wild},
year={2025},
}
```

## What can you get raw data from OSS-MPAW:

1. Dataset of malicious software packages.
2. Dataset of security reports.
3. Dataset of security reports' IoC.
4. Dataset of duplicated groups.
5. Dataset of  similar groups.
6. Dataset of dependent-hidden  groups.
7. Dataset of co-existing groups.

*You can obtain full raw data by email: <xiaoyanzwendy@gmail.com>*

## 📚 Documentation

This repository provides data, code, and experimental workflows supporting the paper.

### 🐛 Data Collection

This folder contains scripts and datasets related to collecting malicious packages and associated security reports:

- `malware.xlsx`: Full dataset (with duplicates), used for overlap analysis (**RQ1**).
- `malware_deduplicated.xlsx`: Deduplicated dataset for analysis.
- `get_npm/pypi/ruby_list_inmirror.py`: A script that fetches packages from mirror repositories to validate the correctness of our dataset collection. This corresponds to the section II (OSS malware collection) in the paper. A `demo.xlsx` file is provided for testing, which can be directly run.
- `Report/`:

  - 1,533 security reports and the corresponding collection scripts.
- `IoC/`:

  - Extracted Indicators of Compromise (IPs, URLs, PowerShell commands) used in **RQ4**.

### 🧠 Knowledge Graph (KG) Analysis

Scripts and data used to construct and analyze the knowledge graph (MALGRAPH):

- `Duplicated_Edge/` – for **RQ1**

  - `npm/pypi/ruby_graph.json`: Duplicated graphs dataset.
  - `get_delete_overallMR.py`: Computes missing rate (Table V).
  - `occurrences/`: Statistical analysis of duplicate appearances (Fig 6).
  - `overlap_matrix/`: Source overlap analysis (Table IV).
- `Similar_Edge/` – for **RQ2**

  - `npm/pypi/ruby_end.xlsx`: Similar graphs dataset.
  - `embedding_cluster/`: Clustering script for similar packages.
- `Dependency_Edge/` – for **RQ3**

  - Dependent-hidden graphs dataset.
- `Co-existing_Edge/` – for **RQ4**

  - Co-existing graphs dataset.

### 📦 Package Info Scripts

These scripts are used to extract and process time-based statistics of malicious package groups. These are general scripts in the paper, and the corresponding figures in **RQ2**, **RQ3**, and **RQ4** are plotted by these scripts. We have included input prompts in the code for each specific RQ:

- `get_evolution/`: Sorts package groups by release time and computes operation changes (e.g., name, version, source code changes). Corresponds to Figures 9 and 12 in the paper.
- `active_time/`: Computes the active period of each group (used in Figures 10, 11, and 13).

### 🤖 ML Models (For Section VI Security Implication and Application)

This folder supports machine learning experiments:

- `legiti_embeddings_js/`: Embeddings of benign (non-malicious) packages.
- `malware_clusters_results_js/`: Clustered malicious samples.
- `mal_embeddings_js_480/`: 480 unclustered malicious packages for generalization tests.
- `ML_BaseVs.Cluster.ipynb`: ML training script, with results corresponding to Table X in the paper.

### ✅ Notes

- All scripts are runnable and tested in Python 3.
- Most scripts use **relative paths** for portability. A few may require path adjustments depending on your environment. For this, we have provided input demos.
- **Regarding the order in which these scripts should be run to reproduce the work: Our suggestion is to follow the order outlined in the documentation. However, the scripts can be run independently as each one is mostly self-contained.**
- Please note that our paper is empirical in nature and involves a certain amount of manual effort. As such, the code provided does not cover all aspects of the work presented in the paper.
