import csv
import sys
import random

try:
    number_of_rows = int(sys.argv[1])
except (IndexError, ValueError):
    number_of_rows = 100000

product_categories = [
    ("PC0001", "computers"),
    ("PC0002", "laptops"),
    ("PC0003", "games"),
    ("PC0004", "displays"),
    ("PC0005", "smartphones"),
    ("PC0006", "hifi"),
    ("PC0007", "cameras"),
    ("PC0008", "game consoles"),
    ("PC0009", "coffee machines"),
    ("PC0010", "keyboards"),
]

data = []
name_format = "NAME{i}"
code_format = "PCODE{i:020d}"

for i in range(number_of_rows):
    category = random.choice(product_categories)
    data.append([
        name_format.format(i=i),
        code_format.format(i=i),
        random.randint(10, 20000),
        category[1],  # category name
        category[0],  # category code
    ])

with open(f'test-data-set-{number_of_rows}.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='"')
    filewriter.writerows(data)