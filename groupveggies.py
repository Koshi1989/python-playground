#Farhana Roslan and Koshi Murakoshi

import csv
import json
from pprint import pprint

#Read vegtables.csv into a variable called vegetables.
with open('vegetables.csv') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	vegetables = [dict(row) for row in rows]

#Group vegtables by color as a variable vegtables_by_color.
vegetables_by_color = {}
for veggies in vegetables:
	color = veggies['color']
	if color in vegetables_by_color:
		vegetables_by_color[color].append(veggies)
	else:
		vegetables_by_color[color] = [veggies]

pprint(vegetables_by_color)

#Output vegtables_by_color into a json called vegtables_by_color.json.
with open('vegetables_by_color.json', 'w') as f:
	json.dump(vegetables_by_color, f, indent=2)

