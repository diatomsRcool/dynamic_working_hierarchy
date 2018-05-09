in_file = open('taxonomy.tsv', 'r')

genera = []

for line in in_file:
	row = line.split('	|	')
	name = row[2]
	id = row[0]
	parent_id = row[1]
	if name == '':
		print id
"""
	if parent_id == 'T205':
		n = name.split(' ')
		genus = n[0]
		if genus in genera:
			pass
		else:
			genera.append(genus)
print len(genera)
print genera
"""