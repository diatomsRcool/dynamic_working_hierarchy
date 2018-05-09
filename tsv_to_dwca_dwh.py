#!/usr/bin/env python
# coding: utf-8

import re
import csv
import pickle
"""
in_file = open('taxonomy.tsv', 'r')
next(in_file)
ranks = []
for line in in_file:
	family = line.strip()
	row = line.split('\t|\t')
	uid = row[0]
	print uid
	rank = row[3]
	if rank in ranks:
		pass
	else:
		ranks.append(rank)
print ranks

ranks = ['no rank', 'species', 'superkingdom', 'no rank - terminal', 'family', 'genus', 'domain', 'phylum', 'class', 'order', 'subspecies', 'subgenus', 'species group', 'species subgroup', 'suborder', 'varietas', 'subclass', 'forma', 'subfamily', 'tribe', 'subphylum', 'superphylum', 'kingdom', 'subkingdom', 'infraspecificname', 'subform', 'subvariety', 'superfamily', 'superorder', 'infraorder', 'subtribe', 'infraclass', 'superclass', 'parvorder']

"""
in_file = open('taxonomy.tsv', 'r')
in_file_s = open('synonym.tsv','r')
out_file = open('dwh_taxa.txt', 'w')

p_dict = pickle.load(open('parent_dict.p', 'rb'))

next(in_file)
for line in in_file:
	line = line.strip('/n')
	row = line.split('\t|\t')
	uid = row[0]
	print uid
	parent_uid = row[1]
	name = row[2]
	rank = row[3]
	source = row[6]
	status = 'accepted'
	out_file.write(uid + '\t' + uid + '\t' + parent_uid + '\t' + name + '\t' + rank + '\t' + source + '\t' + status + '\n')

counter = 1000
next(in_file)
for line in in_file:
	line = line.strip('/n')
	row = line.split('/t|/t')
	uid = 'T' + str(counter)
	a_uid = row[0]
	name = row[1]
	status = row[2]
	rank = row[3]
	parent_uid = p_dict[a_uid]
	out_file.write(uid + '\t' + a_uid + '\t' + parent_uid + '\t' + name + '\t' + rank + '\t' + source + '\t' + status + '\n')
					
"""
print len(ids)
print len(parent_ids)
#out_file_i.write('}')
#out_file_p.write('}')					

leaf_node_ids = []		
leaf_node_names = []
			
for id in ids:
	print id
	if id in parent_ids:
		pass
	else:
		leaf_node_ids.append(id)
		leaf_name = names[ids.index(id)]
		leaf_node_names.append(leaf_name)
print len(leaf_node_ids)

id_dict = open('id_dict.txt', 'r').read()
parent_dict = open('parent_dict.txt', 'r').read()
branches = []
check = []
for id in leaf_node_ids:
	if id in check:
		pass
	else:
		branch = []
		name_1 = id_dict(id)
		p_id = parent_dict(id)
		parent_name = '\'' + id_dict(p_id) + '\''
		indices = [i for i, x in enumerate(parent_ids) if x == p_id]
		for i in indices:
			branch.append('\'' + names[i] + '\'')
			check.append(names[i])
			branches.append('(' + ','.join(branch) + ')' + parent_name)
print branches
"""
