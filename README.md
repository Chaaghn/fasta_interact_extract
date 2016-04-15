# fasta_interact_extract
Interactive attribute-driven multiple contig extractor

The aim here is to use object attributes to interactively navigate through a '.fa' file which contains multiple contigs with fasta format structures. Then, attributes will be chosen according to the mode selected. This script has two modes named 'single' and 'multi'. After a final initiation, multiple text files end up being created and named by using the strings found within the first line of each contig's fasta format.

single: Gives options to create a text files for all contigs and places individual attributes of contigs within these files

multi:  Does the same as the 'single' mode except by instigating a repeatable loop to create a desired list of any chosen attribute, then to created text files containing these attributes for each individual contig.

Requirements:

-python2.7
-Packages:  Biopython1.66
-random '.fa' file containing at least two contigs in fasta format and seperated by a single line
