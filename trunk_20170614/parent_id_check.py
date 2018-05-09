in_file = open('taxonomy.tsv', 'r')

parent_ids = []

taxon_ids = []

next(in_file)
for line in in_file:
	row = line.split('	|	')
	parent_id = row[1]
	taxon_id = row[0]
	if parent_id in parent_ids:
		pass
	else:
		parent_ids.append(parent_id)
	if taxon_id in taxon_ids:
		pass
	else:
		taxon_ids.append(taxon_id)

print(len(parent_ids))
print(len(taxon_ids))

for p in parent_ids:
	if p in taxon_ids:
		pass
	else:
		print('problem parent ' + str(p))