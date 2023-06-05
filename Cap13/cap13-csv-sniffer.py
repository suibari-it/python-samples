import csv

with open("./sample-13.1.tsv", mode="r", encoding="utf-8") as f:
    # 受け取ったデータを解析し、推測したDialectサブクラスを返す
    dialect = csv.Sniffer().sniff(f.read())
    # ファイルオブジェクトの位置を先頭に戻す
    f.seek(0)
    # 推測されたdialectを使用して流し込む
    reader_obj = csv.reader(f, dialect)
    for row in reader_obj:
        print(row)
