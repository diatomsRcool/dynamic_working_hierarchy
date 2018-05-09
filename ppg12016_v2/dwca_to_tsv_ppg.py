#!/usr/bin/env python
# coding: utf-8

# Use the file 'gnparser_python.py" To make the files you need for input

in_file = open('ferntaxa_3.txt', 'r')
out_file_t = open('taxonomy.tsv', 'w')

out_file_t.write('uid	|	parent_uid	|	name	|	rank	|	sourceinfo	|	' + '\n')

for line in in_file:
	line = line.strip('\n')
	row = line.split('\t')
	parent_id = row[3]
	name = row[4]
	taxon_id = row[1]
	rank = row[5]
	source = ''
	out_file_t.write(taxon_id + '\t|\t' + parent_id + '\t|\t' + name + '\t|\t' + rank + '\t|\t' + source + '\t|\t' + '\n')
