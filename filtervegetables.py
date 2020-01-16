#koshi and hana
import csv
import json
from pprint import pprint

#Read vegetables.csv into a variable called vegetables.
with open('vegetables.csv') as f:
	reader = csv.DictReader(f)
	rows = list(reader)
	vegetables = [dict(row) for row in rows]

#Loop through vegetables and filter down to only green vegtables using a whitelist.
greenveggies = []
for row in rows:
    if row['color'] == 'green':
        greenveggies.append(row)

#Print veggies to the terminal
pprint(greenveggies)

#Write the veggies to a json file called greenveggies.json
with open('greenveggies.json', 'w') as f:
	json.dump(greenveggies, f, indent=2)
