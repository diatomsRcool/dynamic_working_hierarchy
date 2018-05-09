#!/usr/bin/env python
# coding: utf-8

import pickle

in_file = open('taxa.txt', 'r')

parent_dict = {}
genus_family_dict = {}
families = []
genera = []
subspecies = []
subspecies_dict = {} #this dictionary lets me look up a species name using the subspecies
species_id_dict = {} #this dictionary lets me look up a taxon id using a species name
s_parent_dict = {} #this dictionary links subspecies to the parent (species) id

lwf = ['Acrobolbaceae','Adelanthaceae','Allisoniaceae','Anastrophyllaceae','Aneuraceae','Antheliaceae','Anthocerotaceae','Arnelliaceae','Aytoniaceae','Balantiopsaceae','Blasiaceae','Brevianthaceae','Calypogeiaceae','Cephaloziaceae','Cephaloziellaceae','Chaetophyllopsaceae','Chonecoleaceae','Cleveaceae','Conocephalaceae','Corsiniaceae','Dendrocerotaceae','Exormothecaceae','Fossombroniaceae','Geocalycaceae','Goebeliellaceae','Gymnomitriaceae','Gyrothyraceae','Haplomitriaceae','Herbertaceae','Hymenophytaceae','Jackiellaceae','Jubulaceae','Jungermanniaceae','Lejeuneaceae','Lepicoleaceae','Lepidolaenaceae','Lepidoziaceae','Lophocoleaceae','Lophoziaceae','Lunulariaceae','Makinoaceae','Marchantiaceae','Mastigophoraceae','Mesoptychiaceae','Metzgeriaceae','Mizutaniaceae','Monocarpaceae','Monocleaceae','Monosoleniaceae','Neotrichocoleaceae','Notothyladaceae','Oxymitraceae','Pallaviciniaceae','Pelliaceae','Plagiochilaceae','Pleuroziaceae','Porellaceae','Pseudolepicoleaceae','Ptilidiaceae','Radulaceae','Ricciaceae','Riellaceae','Scapaniaceae','Schistochilaceae','Sphaerocarpaceae','Targioniaceae','Treubiaceae','Trichocoleaceae','Trichotemnomataceae','Vandiemeniaceae','Vetaformaceae','Wiesnerellaceae']

next(in_file)
for line in in_file:
	row = line.split('\t')
	taxon_id = row[0]
	accepted_id = row[1]
	family = row[3]
	genus = row[4]
	status = row[2]
	rank = row[8]
	if family == '' or family in lwf:
		continue
	elif status == 'doubtful' or status == 'misapplied' or status == 'synonym':
		continue
	else:
		if rank == 'subspecies' or rank == 'variety' or rank == 'f.':
			subsp = row[7]
			sp_ep = row[5]
			species = genus + ' ' + sp_ep
			subspecies_dict[subsp] = species
			if subsp in subspecies:
				pass
			else:
				subspecies.append(subsp)
		else:
			species = genus + ' '  + row[5]
			species_id_dict[species] = taxon_id
			genus_family_dict[genus] = family
			if family in families:
				pass
			else:
				families.append(family)
			if genus in genera:
				pass
			else:
				genera.append(genus)
			
print(len(families))
print(len(genera))
print(len(subspecies))

counter = 100
for family in families:
	print(family)
	parent_dict[family] = 'T' + str(counter)
	print('T' + str(counter))
	counter = counter + 1
for genus in genera:
	print(genus)
	parent_dict[genus] = 'T' + str(counter)
	counter = counter + 1
for subsp in subspecies:
	print(subsp)
	parent_name = subspecies_dict[subsp]
	print(parent_name)
	parent_id = species_id_dict[parent_name]
	print(parent_id)
	s_parent_dict[subsp] = parent_id
pickle.dump(parent_dict, open('parent_dict.p', 'wb'))
pickle.dump(genus_family_dict, open('genus_family_dict.p', 'wb'))
pickle.dump(s_parent_dict, open('s_parent_dict.p', 'wb'))