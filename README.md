# OSS-MPAW

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
- **[report]** - Our reports dataset

### Get_Other：Get numbers of downloads and evolutions of packages
- **[sort_evolution]** - Sort packages within each group according to their release time and obtain the evolutions
- **[get_download_num_3OSS]** - Crawl the number of downloads for packages of 3 OSS
- **[active_time]** - Get the active time of each group
- **[Sum]** - Our information dataset of DeG、SG and CG(include evolution、download nnumbers and so on)
