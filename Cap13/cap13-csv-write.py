import csv

with open("./sample-13.1.tsv", mode="r", encoding="utf-8") as f:
    reader_obj = csv.reader(f, delimiter="\t")

    # １行目はヘッダー行なので、next関数で1行飛ばす
    next(reader_obj)

    with open("./result_from_tsv.csv", mode="w", encoding="utf-8") as wf:
        writer_obj = csv.writer(wf)

        # まずはヘッダー行をリストで書き込む。
        writer_obj.writerow(["name", "age", "gender", "email"])

        # readerオブジェクトをぐるぐる回して、writerオブジェクトに一行ずつ追加する
        for row in reader_obj:
            writer_obj.writerow(row)
