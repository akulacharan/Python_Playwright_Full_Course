import csv

#Read json file
csvfile = open("testdata/data.csv",newline='',encoding="utf-8")
reader = csv.DictReader(csvfile)
print()
