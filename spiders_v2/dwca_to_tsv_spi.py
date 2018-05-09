#!/usr/bin/env python
# coding: utf-8

in_file = open('spiders_3.txt', 'r')
out_file_t = open('taxonomy.tsv', 'w')
out_file_s = open('synonym.tsv', 'w')

out_file_t.write('uid	|	parent_uid	|	name	|	rank	|	sourceinfo	|	' + '\n')
out_file_s.write('uid	|	name	|	type	|	rank	|	' + '\n')

stati = []

for line in in_file:
	line = line.strip('\n')
	row = line.split('\t')
	name = row[4]
	taxon_id = row[1]
	accepted_id = row[2]
	rank = row[5]
	parent_id = row[3]
	source = ''
	if taxon_id != accepted_id:
		print('synonym')
		out_file_s.write(accepted_id + '\t|\t' + name + '\t|\t' + 'synonym' + '\t|\t' + '\t|\t' + '\n')
	else:
		out_file_t.write(taxon_id + '\t|\t' + parent_id + '\t|\t' + name + '\t|\t' + rank + '\t|\t' + source + '\t|\t' + '\n')

#Be sure to manually remove the authority from Sanogasta x-signata and Zygiella x-notata
#And add specific epithet to Tortolena dela, Zodarion van, Eulaira dela, Selenops ab
#until gnparser is fixed