import csv

with open("./sample-13.1.csv", mode="r", encoding="utf-8") as f:
    data = csv.reader(f)
    for row in data:
        print(row)
