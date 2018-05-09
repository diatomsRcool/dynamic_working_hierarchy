import json
"""
#This code block prepares a list of names for gnparser from a dwc taxon file.
in_file = open('spiders.txt', 'r')
out_file = open('spiders_1.txt', 'w')

for line in in_file:
	row = line.split('\t')
	name = row[4]
	out_file.write(name + '\n')
"""
#Use this line in bash to actually use parser: gnparse file --input spiders_1.txt --output spiders_2.txt
#This line can be run regardless of what directory you are in.

#YOU WILL HAVE TO FIX TORTOLENA DELA, ZODARION VAN, EULAIRA DELA, AND SELENOPS AB UNTIL
#GNPARSER ISSUE https://github.com/GlobalNamesArchitecture/gnparser/issues/363 IS FIXED

#This code block takes the json output from gnparser and reinserts it back into the dwca
out_file = open('spiders_3.txt','w')

with open("spiders.txt") as textfile1, open("spiders_2.txt") as textfile2:
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
