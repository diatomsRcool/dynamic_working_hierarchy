#!/usr/bin/env python
# coding: utf-8


in_file = open('taxon.txt', 'r')
out_file_t = open('taxonomy.tsv', 'w')
out_file_s = open('synonym.tsv', 'w')

out_file_t.write('uid	|	parent_uid	|	name	|	rank	|	sourceinfo	|	' + '\n')
out_file_s.write('uid	|	name	|	type	|	rank	|	' + '\n')

for line in in_file:
	line = line.strip()
	row = line.split('\t')
	parent_id = row[4]
	name = row[8]
	taxon_id = row[9]
	accepted_id = row[7]
	rank = row[2]
	source = ''
	if accepted_id != taxon_id:
		print('synonym found')
		out_file_s.write(accepted_id + '\t|\t' + name + '\t|\t' + 'synonym' + '\t|\t' + '\t|\t' + '\n')
	else:
		out_file_t.write(taxon_id + '\t|\t' + parent_id + '\t|\t' + name + '\t|\t' + rank + '\t|\t' + source + '\t|\t' + '\n')
