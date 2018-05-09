import json
from itertools import izip
"""
#This code block prepares a list of names for gnparser from a dwc taxon file.
in_file = open('taxon.tab', 'r')
out_file = open('taxon_1.tab', 'w')

next(in_file)
for line in in_file:
	row = line.split('\t')
	name = row[3]
	out_file.write(name + '\n')
"""
#Use this line in bash to actually use parser: gnparse file --input taxa_1.txt --output taxa_2.txt
#This line can be run regardless of what directory you are in.

#This code block takes the json output from gnparser and reinserts it back into the dwca
out_file = open('taxon_3.tab','w')

with open("taxon.tab") as textfile1, open("taxon_2.tab") as textfile2:
	for x, y in izip(textfile1, textfile2):
		x = x.decode('utf-8')
		row = x.split('\t')
		name = row[3]
		print name
		p_names = json.loads(y)
		v = p_names['parsed']
		if v == False:
			out_file.write('\t'.join(row).encode('utf-8'))
		else:
			p_name = p_names['canonical_name']['value']
			row[3] = p_name
			out_file.write('\t'.join(row).encode('utf-8'))
