#!/usr/bin/env python
# coding: utf-8

in_file = open('gbif_3.tsv', 'r')
out_file_t = open('taxonomy.tsv', 'w')
out_file_s = open('synonym.tsv', 'w')

out_file_t.write('uid	|	parent_uid	|	name	|	rank	|	sourceinfo	|	' + '\n')
out_file_s.write('uid	|	name	|	type	|	rank	|	' + '\n')

stati = []

next(in_file)
for line in in_file:
	line = line.strip('\n')
	row = line.split('\t')
	name = row[3]
	taxon_id = row[0]
	accepted_id = row[2]
	rank = row[4]
	parent_id = row[1]
	status = row[5]
	if status in stati: #This if statement collects all the taxonomic statuses. They get printed at the end
		pass
	else:
		stati.append(status)
	source = ''
	if accepted_id != '':
		print('synonym')
		print(taxon_id)
		out_file_s.write(accepted_id + '\t|\t' + name + '\t|\t' + 'synonym' + '\t|\t' + '\t|\t' + '\n')
	else:
		out_file_t.write(taxon_id + '\t|\t' + parent_id + '\t|\t' + name + '\t|\t' + rank + '\t|\t' + source + '\t|\t' + '\n')
print(stati)