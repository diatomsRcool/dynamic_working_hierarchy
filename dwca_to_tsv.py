#!/usr/bin/env python
# coding: utf-8


in_file = open('20160203_taxon.txt', 'r')
out_file = open('20160203_taxon.tsv', 'w')

out_file.write('uid	|	parent_uid	|	name	|	rank	|	' + '\n')

for line in in_file:
	line = line.strip()
	row = line.split('\t')
	parent_id = row[5]
	name = row[6]
	taxon_id = row[8]
	rank = row[2]
	out_file.write(taxon_id + '\t|\t' + parent_id + '\t|\t' + name + '\t|\t' + rank + '\t|\t' + '\n')
