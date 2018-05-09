#!/usr/bin/env python
# coding: utf-8


in_file = open('taxon_3.tab', 'r')
out_file_t = open('taxonomy.tsv', 'w')

out_file_t.write('uid	|	parent_uid	|	name	|	rank	|	sourceinfo	|	' + '\n')

next(in_file)
for line in in_file:
	line = line.strip('\n')
	row = line.split('\t')
	parent_id = row[2]
	name = row[3]
	taxon_id = row[0]
	rank = row[5]
	source = ''
	out_file_t.write(taxon_id + '\t|\t' + parent_id + '\t|\t' + name + '\t|\t' + rank + '\t|\t' + source + '\t|\t' + '\n')
