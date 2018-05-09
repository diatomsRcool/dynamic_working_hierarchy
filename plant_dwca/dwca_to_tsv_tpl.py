#!/usr/bin/env python
# coding: utf-8

import pickle

parent_dict = pickle.load(open('parent_dict.p', 'rb'))
genus_family_dict = pickle.load(open('genus_family_dict.p', 'rb'))
s_parent_dict = pickle.load(open('s_parent_dict.p', 'rb'))

in_file_t = open('taxa.txt', 'r')
out_file_t = open('taxonomy.tsv', 'w')
out_file_s = open('synonym.tsv', 'w')

out_file_t.write('uid	|	parent_uid	|	name	|	rank	|	sourceinfo	|	' + '\n')
out_file_t.write('9999	|		|	Archaeplastida	|	kingdom	|		|	' + '\n')
out_file_s.write('uid	|	name	|	type	|	rank	|	' + '\n')

lwf = ['Acrobolbaceae','Adelanthaceae','Allisoniaceae','Anastrophyllaceae','Aneuraceae','Antheliaceae','Anthocerotaceae','Arnelliaceae','Aytoniaceae','Balantiopsaceae','Blasiaceae','Brevianthaceae','Calypogeiaceae','Cephaloziaceae','Cephaloziellaceae','Chaetophyllopsaceae','Chonecoleaceae','Cleveaceae','Conocephalaceae','Corsiniaceae','Dendrocerotaceae','Exormothecaceae','Fossombroniaceae','Geocalycaceae','Goebeliellaceae','Gymnomitriaceae','Gyrothyraceae','Haplomitriaceae','Herbertaceae','Hymenophytaceae','Jackiellaceae','Jubulaceae','Jungermanniaceae','Lejeuneaceae','Lepicoleaceae','Lepidolaenaceae','Lepidoziaceae','Lophocoleaceae','Lophoziaceae','Lunulariaceae','Makinoaceae','Marchantiaceae','Mastigophoraceae','Mesoptychiaceae','Metzgeriaceae','Mizutaniaceae','Monocarpaceae','Monocleaceae','Monosoleniaceae','Neotrichocoleaceae','Notothyladaceae','Oxymitraceae','Pallaviciniaceae','Pelliaceae','Plagiochilaceae','Pleuroziaceae','Porellaceae','Pseudolepicoleaceae','Ptilidiaceae','Radulaceae','Ricciaceae','Riellaceae','Scapaniaceae','Schistochilaceae','Sphaerocarpaceae','Targioniaceae','Treubiaceae','Trichocoleaceae','Trichotemnomataceae','Vandiemeniaceae','Vetaformaceae','Wiesnerellaceae']

next(in_file_t)
for line in in_file_t:
	line = line.strip('\n')
	row = line.split('\t')
	genus = row[4]
	name = row[7]
	taxon_id = row[0]
	accepted_id = row[1]
	rank = row[8]
	status = row[2]
	family = row[3]
	source = ''
	print(name)
	if family == '' or family in lwf:
		continue
	if status == 'synonym':
		out_file_s.write(accepted_id + '\t|\t' + name + '\t|\t' + 'synonym' + '\t|\t' + '\t|\t' + '\n')
	elif status == 'accepted':
		if rank == 'subspecies' or rank == 'variety' or rank == 'f.':
			parent_id = s_parent_dict[name]
		else:
			parent_id = parent_dict[genus]
		out_file_t.write(taxon_id + '\t|\t' + parent_id + '\t|\t' + name + '\t|\t' + rank + '\t|\t' + source + '\t|\t' + '\n')
	elif status == 'misapplied' or status == 'doubtful':
		continue
	else:
		print('error in status')
		print(status)
for k,v in parent_dict.items():
	if k in genus_family_dict:
		rank = 'genus'
		parent = genus_family_dict[k]
		parent_id = parent_dict[parent]
	else:
		rank = 'family'
		parent_id = '9999'
	name = k
	taxon_id = v
	source = ''
	out_file_t.write(taxon_id + '\t|\t' + parent_id + '\t|\t' + name + '\t|\t' + rank + '\t|\t' + source + '\t|\t' + '\n')
