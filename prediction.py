import json

periodic_table = {}


# #################################LOAD DATA##################################

with open('data/tp.json') as json_data:
	d = json.load(json_data)
	for i in d['table']:
		periodic_table[i['small']] = i['name'], i['small'], i['position'], i['molar'], i['number'], i[
			'electronegativity'], i['electrons']
	json_data.close()

# ############################################################################

print(periodic_table['He'])
