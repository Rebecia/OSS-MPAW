<!-- # OSS-MPAW
## What can you get from OSS-MPAW:
1. Dataset of malicious software packages that we have collected and processed(in Excels).
2. The scripts of trying downloading packages, processing them, and establishing their knowledge graphs.

## Get_KG：Build Knowledge Graphs and Generate four kinds of Subgrah
- **[Data]** - Our dataset
- **[KG]** - Knowledge Graph
- **[SubGraph]** - All Subgraphs(unclassified) and Four Subgraphs
- **[Build_KG、Update_KG]** - Build and Update knowledge graphs
- **[Generate_SubGragh、Classify_SubGraph]** - Generate and Classifiy knowledge graph subgraphs

## Get_KG_Need: Obtain the information required to establish KGs

### AST_API_Cluster：Extract source code APIs through AST、 Embed and Cluster
- **[sourcecode_cluster]** - Get APIs、Embed and CLuster
- **[get_ruby]** - Get .rb APIs(Python doesn‘t include libraries that can directly process Ruby files)

### Get_Report：Get the report that the package to appear in it
- **[get_report_name]** - Crawl URLs in 'report.xlsx' and determine if the package appears within it
- **[report]** - Our report dataset

### Get_Other：Get numbers of downloads and evolutions of packages
- **[sort_evolution]** - Sort packages within each group according to their release time and obtain the evolutions
- **[get_download_num_3OSS]** - Crawl the number of downloads for packages of 3 OSS
- **[active_time]** - Get the active time of each group
- **[Sum]** - Our information dataset of DeG、SG and CG(include evolution、download nnumbers and so on)

## Get_Malicious_Package：Traverse the Excel and try to download packages from mirrors
- **[malicious_packages]** - Our dataset
- **[get_npm_list_inmirror/get_pypi_list_inmirror/get_ruby_list_inmirror]** - Download the packages of the corresponding ecosystem

=================================================================== -->

## OSS-MPAW 

This github repo is the artifact dataset for the manuscript "OSS Malicious Package Analysis in the Wild".

This project has built and curate the largest dataset of 23,425 malicious packages from scattered online sources. Then, a knowledge graph represents the OSS malware corpus and SSC attack campaigns behind malicious packages.

## What can you get raw data from OSS-MPAW:

1. Dataset of malicious software packages.
2. Dataset of security reports.
3. Dataset of duplicated groups.
4. Dataset of similar malcious package groups.
5. Dataset of dependency malware groups.
6. Dataset of co-existing malware groups. 

*You can obtain full raw data by email: <fake@example.com>*


## Documentation

Our repo contains the basic information of malicious packages. 

**Data collection** contains codes/scripts that download malicious packages and security reports.

- malware folder: Our dataset and the web crawler for malicious packages
- Report folder: Our report dataset (1533 reports and corresponding URLs) and the codes/scripts that collect security reports.


**Package Info** contains codes/scripts that extract basic information of malicious packages, including release time, download number, metadata, and AST. 

- Obtain the information of malicious packages
- AST_API_Cluster：Extract source code APIs through AST、 Embed and Cluster
 **[sourcecode_cluster]** - Get APIs、Pretrain model and Cluster
 **[get_ruby]** - Get .rb APIs(Python doesn‘t include libraries that can directly process Ruby files)
- **[sort_evolution]** - Sort packages within each group according to their release time and obtain the evolutions
- **[get_download_num_3OSS]** - Crawl the number of downloads for packages of 3 OSS
- **[active_time]** - Get the active time of each group
- **[Sum]** - Our information dataset of DeG、SG and CG(include evolution、download nnumbers and so on)


**KG** contains codes/scripts that generate groups of malicious packages, including DG, DeG, CG, and SG. 

- **[Data]** - Our dataset
- **[KG]** - Knowledge Graph
- **[SubGraph]** - All Subgraphs(unclassified) and Four Subgraphs
- **[Build_KG、Update_KG]** - Build and Update knowledge graphs
- **[Generate_SubGragh、Classify_SubGraph]** - Generate and Classifiy knowledge graph subgraphs

