#!/usr/bin/env python
# coding: utf-8

in_file_t = open('taxon.txt', 'r')
out_file_t = open('taxonomy.tsv', 'w')
out_file_s = open('synonym.tsv', 'w')

out_file_t.write('uid	|	parent_uid	|	name	|	rank	|	sourceinfo	|	' + '\n')
out_file_s.write('uid	|	name	|	type	|	rank	|	' + '\n')

stati = []

next(in_file_t)
for line in in_file_t:
	line = line.strip('\n')
	row = line.split('\t')
	name = row[5]
	taxon_id = row[1]
	rank = row[7]
	status = row[9]
	parent_id = row[4]
	accepted_id = row[3]
	source = ''
	if status in stati:
		pass
	else:
		stati.append(status)
	if status == 'invalid':
		continue
	if taxon_id != accepted_id:
		print('synonym detected')
		out_file_s.write(accepted_id + '\t|\t' + name + '\t|\t' + 'synonym' + '\t|\t' + '\t|\t' + '\n')
	else:
		out_file_t.write(taxon_id + '\t|\t' + parent_id + '\t|\t' + name + '\t|\t' + rank + '\t|\t' + source + '\t|\t' + '\n')
print(stati)