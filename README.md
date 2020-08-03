# Filtering 'omics' style data by gene

This program has been designed to simplify subsetting 'omics' data results by gene. This is often used when filtering results from RNA-seq, ChIP-seq, and even variant information (for example from whole exome or whole genome sequencing). This program works by taking a list (or multiple lists) of gene symbols and retaining only the rows pertaining to the genes of interest from an entire results file.

Example Usage: python filter_by_gene.py -c Symbol -i Cancer_Cell_Line_Results.csv -p
Cancer_Cell_Lines -l Metastasis_genes.txt Apoptosis_genes.txt -n Metastasis
Apoptosis

Optional Arguments:

  -h, --help            
                        show this help message and exit

  -i INPUT_FILE, --input_file INPUT_FILE

                        This is an input file containing 'omics' style results
                        with one gene per row in comma separated value (csv)
                        format. For more information about formatting this csv
                        file, see the [Example](Example) folder.

  -c COLUMN_LABEL, --column_label COLUMN_LABEL

                        This is label for the column that contains information
                        about the gene symbol. This is often 'Symbol' or
                        'Gene'. Make sure there is no space in the column
                        label because spaces will cause the program to mistake
                        the column label as multiple arguments.

  -l GENE_LISTS [GENE_LISTS ...], --gene_lists GENE_LISTS [GENE_LISTS ...]

                        This is a list of text files containing genes symbols.
                        One or more text files must be provided. The text
                        files should each contain a list of gene symbols, one
                        gene per line. Note that protein symbols will not
                        work. The name of the group will be specified by the
                        argument --group_names.

  -n GROUP_NAMES [GROUP_NAMES ...], --group_names GROUP_NAMES [GROUP_NAMES ...]

                        This is a list of the group names to accompany the
                        text files specified by the -l or --gene_lists option.
                        If you do not use this option, the file names of the
                        files specified in --gene_lists (without the
                        extensions) will be used as the group names.

  -p PREFIX, --prefix PREFIX

                        This is prefix used for the output files. If you do
                        not use this option, the file name of the RNAseq
                        results file specified by the -i or --input_file
                        option (without the .csv) will be used.

## Preparing input files

### Omics data file

The omics data file must be saved in comma separated value (csv) format. The first row in the csv file is taken as the header. The gene symbol must be saved in the same column for every row. The label for the column containing the gene symbol is specified by the -c coption. For an example see the [Example](Example) folder.

### Gene list files

Multiple gene list files can be used at one time, as in the example. Each list of genes should be saved in a separate text file. Each line in the text files should contain the a gene symbol. Note that the program is case sensitive, so please ensure that your input gene list files have the same case as your 'omics' data file. For examples of formatting see the [Example](Example) folder.

### Output files

This program will return one csv file for each input gene list. The output files will be the same format as the input omics file, just filtered to only contain lines with information about genes contained in the input gene lists. For each list of genes, a single text file may be created containing lines that did not match a gene symbol in the 'omics' input file. These are frequently protein symbols instead of gene symbols. These could also be misspellings or symbols with the incorrect case. Additionally, if a header line was included in the input gene file, it will be added to this file. For more information about the output from this program, see the [Example](Example) folder.
