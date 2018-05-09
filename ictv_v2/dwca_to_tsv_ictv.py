#!/usr/bin/env python
# coding: utf-8


in_file = open('taxon.tab', 'r')
out_file = open('taxonomy.tsv', 'w')

out_file.write('uid	|	parent_uid	|	name	|	rank	|	sourceinfo	|	' + '\n')

next(in_file)
for line in in_file:
	line = line.strip('\n')
	row = line.split('\t')
	parent_id = row[2]
	name = row[3]
	taxon_id = row[0]
	rank = row[5].lower()
	source = ''
	out_file.write(taxon_id + '\t|\t' + parent_id + '\t|\t' + name + '\t|\t' + rank + '\t|\t' + source + '\t|\t' + '\n')
