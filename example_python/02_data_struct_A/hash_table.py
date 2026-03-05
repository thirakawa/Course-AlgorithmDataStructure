"""hash_table.py

-----------------------------------------------------------------------
ハッシュテーブル（Hash table）のサンプルプログラム。

このプログラムでは hash_function.py で使用したhash_simple関数
を使用して、人物の名前と性別のデータを登録するハッシュテーブル
を実装します。
"""


# シンプルなハッシュ関数（ASCIIの合計値）
def hash_simple(key):
    total = 0
    for char in key:
        total += ord(char)
    return total


# ハッシュテーブルのクラス定義
class HashTable:
    def __init__(self, size):
        # 配列のサイズを指定
        self.size = size
        # データを格納する配列（リスト）を用意
        self.table = []
        # size 分の配列を self.table 内に用意
        for _ in range(self.size):
            self.table.append([])

    # データを追加
    def put(self, key, value):
        # データを格納する場所（インデックス）を計算
        hash_value = hash_simple(key)   # ハッシュ値の計算
        index = hash_value % self.size  # ハッシュ値と self.size から剰余を計算

        # 計算したハッシュ値とインデックスの表示
        print(f"Key: {key}, Value: {value} を次の場所に追加します: Index: {index} (Hash Value: {hash_value})")

        # 指定したインデックスの配列を選択
        bucket = self.table[index]

        # 既存キーがあれば更新
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return

        # なければ最後尾に追加
        bucket.append((key, value))

    # key で指定したデータの情報を参照
    def get(self, key):
        # key が格納されている場所（インデックス）を計算
        hash_value = hash_simple(key)
        index = hash_value % self.size

        # 計算したハッシュ値とインデックスの表示
        print(f"Key: {key} は次の場所を参照します: Index: {index} (Hash Value: {hash_value})")

        # 指定したインデックスの配列を選択
        bucket = self.table[index]

        # bucket 内のデータを先頭から一つずつ確認
        for k, v in bucket:
            if k == key:
                return v

        # 指定した key のデータがなかった場合
        return None

    def __str__(self):
        return str(self.table)


# ---------------------------------------------------------------------
# ハッシュテーブルの初期化
ht = HashTable(5)

# ---------------------------------------------------------------------
# データの追加
print("ハッシュテーブルにデータを追加します。")
ht.put("Joe", "Male")
ht.put("Sue", "Female")
ht.put("Dan", "Male")
ht.put("Nell", "Female")
ht.put("Ally", "Female")
ht.put("Bob", "Male")

# スタック全体を表示（本来は全体を表示できないことに注意）
print("-" * 10)
print(f"ハッシュテーブル全体: {ht}")

# ハッシュテーブルの各要素を一つずつ表示
print(f"ハッシュテーブル 0 番目: {ht.table[0]}")
print(f"ハッシュテーブル 1 番目: {ht.table[1]}")
print(f"ハッシュテーブル 2 番目: {ht.table[2]}")
print(f"ハッシュテーブル 3 番目: {ht.table[3]}")
print(f"ハッシュテーブル 4 番目: {ht.table[4]}")

# ---------------------------------------------------------------------
# データの参照（target で指定した名前の人物の性別を参照）
target = "Ally"

print("-" * 10)
print(f"{target} の性別情報を参照します。")
gender = ht.get(target)

# 結果の表示
if gender is not None:
    print(f"{target} の性別は {gender} です。")
else:
    print(f"{target} は見つかりませんでした。")
