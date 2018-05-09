#!/usr/bin/env python
# coding: utf-8

import re
import csv
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
out_file = open('ott.txt', 'w')
#out_file_i = open('id_dict.txt', 'w')
#out_file_p = open('parent_dict.txt', 'w')

#parent_ids = []
#ids = []
#names = []
#ranks = []

#out_file_i.write('{')
#out_file_p.write('{')

next(in_file)
for line in in_file:
	family = line.strip()
	row = line.split('\t|\t')
	uid = row[0]
	print uid
	parent_uid = row[1]
	name = row[2]
	rank = row[3]
	flag = row[6]
	if rank == 'species' or rank == 'no rank - terminal' or rank == 'genus' or rank == 'subspecies' or rank == 'subgenus' or rank == 'species group' or rank == 'species subgroup' or rank == 'varietas' or rank == 'forma' or rank == 'infraspecificname' or rank == 'subform' or rank == 'subvariety':
		pass
	else:
		m = re.search(r'\d', name)
		if m != None:
			pass
		else:
			m = re.search('Plasmid|viroid|Viroid|homologous|promoter|sp.|sequence|vector|Vector|recombinant|synthetic|1|2|3|4|5|6|7|8|9|Incertae Sedis|uncultured|group', name)
			if m != None:
				pass
			else:
				m = re.search('hidden', flag)
				if m != None:
					pass
				else:
					print name
					#parent_ids.append(parent_uid)
					#ids.append(uid)
					#names.append(name)
					#ranks.append(rank)
					out_file.write(uid + '\t' + name + '\t' + parent_uid + '\t' + rank + '\t' + '' + '\t' + '' + '\t' + '' + '\t' + '' + '\t' + '' + '\t' + '' + '\n')
					
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
