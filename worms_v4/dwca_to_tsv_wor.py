#!/usr/bin/env python
# coding: utf-8

in_file_t = open('taxon_3.tab', 'r')
out_file_t = open('taxonomy.tsv', 'w')
out_file_s = open('synonym.tsv', 'w')

out_file_t.write('uid	|	parent_uid	|	name	|	rank	|	sourceinfo	|	' + '\n')
out_file_s.write('uid	|	name	|	type	|	rank	|	' + '\n')

next(in_file_t)
for line in in_file_t:
	line = line.strip('\n')
	row = line.split('\t')
	name = row[5]
	taxon_id = row[0]
	rank = row[8].lower()
	status = row[9]
	parent_id = row[4]
	accepted_id = row[3]
	source = ''
	if status == 'synonym':
		out_file_s.write(accepted_id + '\t|\t' + name + '\t|\t' + 'synonym' + '\t|\t' + '\t|\t' + '\n')
	elif status == 'accepted':
		out_file_t.write(taxon_id + '\t|\t' + parent_id + '\t|\t' + name + '\t|\t' + rank + '\t|\t' + source + '\t|\t' + '\n')
	else:
		print('Not accepted name')