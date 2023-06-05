import csv

with open("./sample-13.1.csv", mode="r", encoding="utf-8") as f:
    # readerのかわりにDictReaderを使う
    for row in csv.DictReader(f):
        print(row)
