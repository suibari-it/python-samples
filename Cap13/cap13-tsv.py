import csv

with open("./sample-13.1.tsv", mode="r", encoding="utf-8") as f:
    reader_obj = csv.reader(f, delimiter="\t")
    for row in reader_obj:
        print(row)
