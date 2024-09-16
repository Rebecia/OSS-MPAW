## OSS-MPAW 

This github repo is the artifact dataset for the manuscript "An Analysis of Malicious Packages in Open-Source Software in the Wild".

This project has built and curate the largest dataset of 24,357 malicious packages from scattered online sources. Then, the knowledge graph represents the OSS malware corpus and SSC attack campaigns behind malicious packages.

## What can you get raw data from OSS-MPAW:

1. Dataset of malicious software packages.
2. Dataset of security reports.
3. Dataset of security reports' IoC.
3. Dataset of duplicated groups.
4. Dataset of repeated attack package groups.
5. Dataset of dependent-hidden attack package groups.
6. Dataset of report attack package groups. 

*You can obtain full raw data by email: <wendyzhouxian@gmail.com>*


## Documentation

Our repo contains the basic information of malicious packages. 

**Data collection** contains codes/scripts that download malicious packages and security reports.

- malware folder: Our dataset and the web crawler for malicious packages
- Report folder: Our report dataset (1533 reports and corresponding URLs) and the codes/scripts that collect security reports.
- IoC folder: Our IoC dataset.

**Package Info** contains codes/scripts that extract basic information of malicious packages, including release time, metadata and AST. 

- Obtain the information of malicious packages
- AST_API_Cluster：Extract source code APIs through AST、 Embed and Cluster
 **[sourcecode_cluster]** - Get APIs、Pretrain model and Cluster
 **[get_ruby]** - Get .rb APIs(Python doesn‘t include libraries that can directly process Ruby files)
- **[sort_evolution]** - Sort packages within each group according to their release time and obtain the evolutions
- **[active_time]** - Get the active time of each group
- **[get_release_time]** - Get the release time of each package


**KG** contains codes/scripts that generate groups of malicious packages

- **[duplicate]** -  Generate knowledge graph subgraphs of duplicated packages
- **[attack_campagin]** -  Generate knowledge graph subgraphs of 3 kinds of attack campagin