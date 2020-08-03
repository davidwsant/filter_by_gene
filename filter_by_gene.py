#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import glob

from argparse import ArgumentParser
from os.path import splitext

args = ArgumentParser('./filter_by_gene.py', description='''This program has been designed to simplify
obtaining results pertaining to specific genes out of csv format files, including "omic" result files.
For details on preparing input files, see README.md. Example usage: python filter_by_gene.py -c Symbol -i
Cancer_Cell_Line_Results.csv -p Cancer_Cell_Lines -l Metastasis_genes.txt Apoptosis_genes.txt
-n Metastasis Apoptosis''')

args.add_argument(
	'-i',
	'--input_file',
	help="""This is an input file containing 'omics' style results with one gene per row in comma separated value
	(csv) format. For more information about formatting this csv file, see the README.md file.""",
	default=None
)

args.add_argument(
	'-c',
	'--column_label',
	help="""This is label for the column that contains information about the gene symbol. This is often
	'Symbol' or 'Gene'. Make sure there is no space in the column label because spaces will cause the program
	to mistake the column label as multiple arguments.""",
	default = None
)

args.add_argument(
	'-l',
	'--gene_lists',
	nargs='+', # This tells the program that if they specify this flag, they have to give it at least one input. If they don't specify it, then the default will go in.
	help="""\
This is a list of text files containing genes symbols. One or more text files must be provided. The text files
should each contain a list of gene symbols, one gene per line. Note that protein symbols will not work.
The name of the group will be specified by the argument --group_names. """,
)

args.add_argument(
	'-n',
	'--group_names',
	nargs='+',
	help="""This is a list of the group names to accompany the text files specified by the -l or --gene_lists
	option. If you do not use this option, the file names of the files specified in --gene_lists (without the
	extensions) will be used as the group names.""",
	default = None
)

args.add_argument(
	'-p',
	'--prefix',
	help="""This is prefix used for the output files. If you do not use this option, the file name of the
	'omics' file specified by the -i or --input_file option (without the .csv) will be used.""",
	default = ''
)


def print_help_message():
	print()
	print("""\tWelcome to filter_by_gene.py. This program has been designed to simplify obtaining results
	pertaining to specific genes out of csv format files, including RNA-seq result files. For details on
	preparing input files, see README.md.""")
	print("""\tExample usage: python filter_by_gene.py -i Cancer_Cell_Line_Results.csv
	-p Cancer_Cell_Lines -l Metastasis_genes.txt Apoptosis_genes.txt -n Metastasis Apoptosis""")
	print()

args = args.parse_args()
input_file = args.input_file
if input_file == None:
	print()
	print_help_message()
	print("\tYou have not entered a file name for an input 'omics' file. Please enter this info using the -i option.")
	list_of_files = glob.glob("*.csv")
	print("\tThe csv format files in your current working directory are:")
	print(list_of_files)
	print()
	exit(1)

input_gene_lists = []
gene_list_inputs = args.gene_lists
if gene_list_inputs == None:
	print()
	print_help_message()
	print("\tYou have not entered any lists of genes. Please enter this info using the -l and -n options.")
	list_of_files = glob.glob("*.txt")
	print("\tThe txt format files in your current working directory are:")
	print(list_of_files)
	print()
	exit(1)

for text_file in gene_list_inputs:
	input_gene_lists.append([line.rstrip('\n') for line in open(text_file)])

group_names = args.group_names
if group_names == None:
	group_names = [splitext(gene_list)[0] for gene_list in gene_list_inputs]

prefix = args.prefix

column_label = args.column_label
if not column_label:
	df = pd.read_csv(input_file)
	list_of_columns = list(df.columns)
	print()
	print_help_message()
	print("\tYou have not entered a label for a column that contains the gene symbol. Please enter this info using the -c option.")
	print()
	print("\tThe column labels from your input file are:")
	print(list_of_columns)
	print()
	exit(1)

## If it has made it to this point, they have entered all of the necessary info from the command line
### group_names, input_gene_lists, input_file, prefix, column_label
df = pd.read_csv(input_file)
for group_name, gene_list in zip(group_names, input_gene_lists):
	subset_df = df[df[column_label].isin(gene_list)]
	if len(subset_df) >= 1:
		subset_df.to_csv(prefix+'_'+group_name+'.csv')
	genes_not_found = []
	present_genes = subset_df[column_label].values
	for entry in gene_list:
		if entry not in present_genes:
			genes_not_found.append(entry)
	if len(genes_not_found) >= 1:
		not_found_output = prefix+'_'+group_name+'_missing_genes.txt'
		print()
		print("\tAt least one entry in group "+group_name+" was not found in the input file.")
		print("\tThese entries will be stored to the file "+not_found_output)
		print("\tPlease double check that these are not protein names or header lines.")
		print()
		with open(not_found_output, 'w') as file:
			file.writelines("%s\n" % entry for entry in genes_not_found)
