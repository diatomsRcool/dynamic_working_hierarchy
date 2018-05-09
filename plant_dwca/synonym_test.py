#!/usr/bin/env python
# coding: utf-8

in_file_t = open('taxa.txt', 'r')

next(in_file_t)
for line in in_file_t:
	line = line.strip('\n')
	row = line.split('\t')
	name = row[7]
	taxon_id = row[0]
	rank = row[8]
	status = row[2]
	if rank == 'family' and status == 'synonym':
		print taxon_id
	if rank == 'genus' and status == 'synonym':
		print taxon_id
