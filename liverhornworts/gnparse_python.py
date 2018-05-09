import json
"""
#This code block prepares a list of names for gnparser from a dwc taxon file.
in_file = open('liverhornworts.txt', 'r')
out_file = open('liverhornworts_1.txt', 'w')

for line in in_file:
	row = line.split('\t')
	name = row[4]
	out_file.write(name + '\n')
"""
#Use this line in bash to actually use parser: gnparse file --input liverhornworts_1.txt --output liverhornworts_2.txt
#This line can be run regardless of what directory you are in.

#This code block takes the json output from gnparser and reinserts it back into the dwca
out_file = open('liverhornworts_3.txt','w')

with open("liverhornworts.txt") as textfile1, open("liverhornworts_2.txt") as textfile2:
	for x, y in zip(textfile1, textfile2):
		row = x.split('\t')
		name = row[4]
		print(name)
		p_names = json.loads(y)
		v = p_names['parsed']
		if v == False:
			out_file.write('\t'.join(row))
		else:
			p_name = p_names['canonical_name']['value']
			row[4] = p_name
			out_file.write('\t'.join(row))
