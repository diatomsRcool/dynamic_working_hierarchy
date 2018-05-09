#!/usr/bin/env python
# coding: utf-8

in_file_t = open('taxa_3.txt', 'r')
out_file_t = open('taxonomy.tsv', 'w')

out_file_t.write('uid	|	parent_uid	|	name	|	rank	|	sourceinfo	|	' + '\n')

for line in in_file_t:
	line = line.strip('\n')
	row = line.split('\t')
	name = row[5]
	taxon_id = row[1]
	rank = row[4]
	status = row[6]
	parent_id = row[3]
	accepted_id = row[2]
	out_file_t.write(taxon_id + '\t|\t' + parent_id + '\t|\t' + name + '\t|\t' + rank + '\t|\t' + '' + '\t|\t' + '\n')
