import csv

# サンプルデータ。花の種類と属性情報
flowers = [
    {"name": "バラ", "color": "赤", "fragrance": "あり", "bloom_season": "春"},
    {"name": "ひまわり", "color": "黄色", "fragrance": "なし", "bloom_season": "夏"},
    {"name": "ユリ", "color": "白", "fragrance": "あり", "bloom_season": "春"},
    {"name": "チューリップ", "color": "さまざま", "fragrance": "あり", "bloom_season": "春"},
    {"name": "デイジー", "color": "白", "fragrance": "なし", "bloom_season": "夏"},
]

with open("result_distwriter.csv", mode="w", encoding="utf-8") as wf:
    fieldnames = ["name", "color", "fragrance", "bloom_season"]
    writer = csv.DictWriter(wf, fieldnames)

    # writerheaderメソッドを使ってヘッダー情報を書き込む
    writer.writeheader()
    writer.writerows(flowers)
