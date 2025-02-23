import csv

csv_data = None
with open("pages\\schools\\links.csv") as csv_fp:
	csv_data = csv.reader(csv_fp)

	headers, *rows = csv_data

print(headers)
print()
print(*rows, sep="\n")












