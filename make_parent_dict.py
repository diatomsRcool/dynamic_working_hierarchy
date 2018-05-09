import pickle

in_file = open('taxonomy.tsv', 'r')

p_dict = {}

for line in in_file:
	line = line.strip('/n')
	row = line.split('\t|\t')
	uid = row[0]
	print uid
	parent_uid = row[1]
	p_dict[uid] = parent_uid

pickle.dump(p_dict open('parent_dict.p', 'wb'))