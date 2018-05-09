#!/usr/bin/env python
# coding: utf-8

import pickle

in_file = open('taxon.tab', 'r')

genera = []

genran = []

next(in_file)
for line in in_file:
	row = line.split('\t')
	name = row[5]
	taxon_id = row[0]
	rank = row[8].lower()
	status = row[9]
	parent_id = row[4]
	accepted_id = row[3]
	x = rank + ' ' + status
	if x in genran:
		pass
	else:
		genran.append(x)
	if status == 'synonym' and (rank == 'genus' or rank == 'family' or rank == 'class' or rank == 'suborder' or rank == 'superfamily' or rank == 'order' or rank == 'phylum' or rank == 'subclass' or rank == 'subphylum' or rank == 'subgenus' or rank == 'subfamily' or rank == 'kingdom' or rank == 'infraorder'):
		genera.append(taxon_id)
		
print(genran)

pickle.dump(genera, open('synonym_parent.p', 'wb'))