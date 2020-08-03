## Example for filter_by_gene.py

Run this example using this command:

```
python filter_by_gene.py -i Kemper_BRAF_FFPE_results.csv -p Kemper_FFPE -l Cell_cycle.txt DNA_damage_apoptosis.txt -n Cycle Apoptosis -c Symbol
```

This folder contains example files for use by the filter_by_gene.py script. The data contained here are from the manuscript [Kemper K *et al.*,](https://pubmed.ncbi.nlm.nih.gov/27320919/) "BRAF(V600E) Kinase Domain Duplication Identified in Therapy-Refractory Melanoma Patient-Derived Xenografts.", *Cell Rep*, 2016 Jun 28;16(1):263-277. Differential expression was run between the pre-metastatic and post-metastatic FFPE derived samples. The raw files for this project can be obtained from [Gene Expression Omnibus](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA297786).

### Input 'omics' file

Note that the file Kemper_BRAF_FFPE_results.csv file contains results of the differential expression. Each row contains information for a separate gene. The information contained in the columns will change between experiments, but for this experiment information about fragments per kilobase per million mapped reads (FPKM), as well as differential analysis adjusted P-values are included. Only results pertaining to genes within the provided gene lists have been included in this file for the sake of space. Interpretation of the differential analysis is not included with this project as this is simply an example used for users to test filter_by_gene.py. This data is of no importance to the program, but was simply of interest to the authors of the program. If the user desires to obtain more information about the results, we recommend reading the publication. [Kemper K *et al.*,](https://pubmed.ncbi.nlm.nih.gov/27320919/) "BRAF(V600E) Kinase Domain Duplication Identified in Therapy-Refractory Melanoma Patient-Derived Xenografts.", *Cell Rep*, 2016 Jun 28;16(1):263-277.

### Gene list files

Two example input lists have been prepared, both obtained from [Gene Ontology](http://geneontology.org/). The two pathways chosen were [regulation of cell cycle process (GO:0010564)](http://amigo.geneontology.org/amigo/term/GO:0010564) and [regulation of intrinsic apoptotic signaling pathway in response to DNA damage (GO:1902229)](http://amigo.geneontology.org/amigo/term/GO:1902229). These pathways were not found to be overenriched in the dataset from Kemper *et al.* publication, but were simply selected as an example. Both files contain a gene symbol that is not present in the Kemper_BRAF_FFPE_results.csv so that the users can see an example of the output that is obtained when at least one gene is missing from the data. Additionally, both of these text files contain a title line. This line should normally be removed from the input gene lists, but was kept to show users and the consequence. Note that these files are text files with one gene name per line.

### Output Results

Notice how two separate lists were used at the same time. Each list will give two separate output files, one containing the subsetted data and one containing a list of lines in the input gene lists that were not found in the file Kemper_BRAF_FFPE_results.csv.

All output file names will begin with 'Kemper_FFPE' as this was the specified prefix from the -p option. Each file name is then followed by the name specified for the gene lists using the -n option. Note that if the -n option is not used, the names of the input gene lists are used instead. In this case, 'Cycle' would be replaced with 'Cell_cycle' and 'Apoptosis' would be replaced with 'DNA_damage_apoptosis'.

Each input gene list gives one result csv file ('Kemper_FFPE_Apoptosis.csv' and 'Kemper_FFPE_Cycle.csv'). These files will contain the same header as the Kemper_BRAF_FFPE_results.csv file. They are simply subset by the lists of genes specified.

Each input gene list will also give a text file ('Kemper_FFPE_Cycle_missing_genes.txt' and 'Kemper_FFPE_Apoptosis_missing_genes.txt'). Each line of the text files contain the lines that did not contain a gene that was present within the Kemper_BRAF_FFPE_results.csv file. This is to help the user determine if any errors were made in preparing the input gene lists. For the present example, 'Kemper_FFPE_Cycle_missing_genes.txt' should contain two lines. One should be the title ("regulation of cell cycle process (GO:0010564)") and the other should be "SDCCAG3", a gene not present in Kemper_BRAF_FFPE_results.csv.  'Kemper_FFPE_Apoptosis_missing_genes.txt' likewise should contain one line with the title ("regulation of intrinsic apoptotic signaling pathway in response to DNA damage (GO:1902229)") and one line with a gene not present in Kemper_BRAF_FFPE_results.csv ("FBXO18"). 
