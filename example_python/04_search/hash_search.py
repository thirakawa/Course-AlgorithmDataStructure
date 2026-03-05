"""hash_search.py

-----------------------------------------------------------------------
ハッシュ探索のサンプルプログラム。

このプログラムではハッシュ関数・ハッシュテーブルを使用して
対象のデータを場所と情報をハッシュ探索しています。

注意1：
ハッシュ関数については 02_data_struct_A/hash_function.py を
ハッシュテーブルについては 02_data_struct_A/hash_table.py を
参照してください。

注意2：
このプログラムでは hash_table.py のプログラムを再掲しています。
以下の HashTable クラス内の get() メソッドでハッシュ探索が実装
されています。
"""


# シンプルなハッシュ関数（ASCIIの合計値）（02_data_struct_A/hash_function.py）
def hash_simple(key):
    total = 0
    for char in key:
        total += ord(char)
    return total


# ハッシュテーブルのクラス定義（02_data_struct_A/hash_function.py）
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

    # key で指定したデータの情報を参照（ハッシュ探索）
    def get(self, key):
        # key が格納されている場所（インデックス）を計算
        hash_value = hash_simple(key)
        index = hash_value % self.size

        # 計算したハッシュ値とインデックスの表示
        print(f"Key: {key} は次の場所を参照します: Index: {index} (Hash Value: {hash_value})")

        # 指定したインデックスの配列を選択（線形探索）
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
# ハッシュ探索
target = "Bob"

print("-" * 10)
print(f"{target} の性別情報をハッシュ探索します。")
gender = ht.get(target)

# 結果の表示
if gender is not None:
    print(f"{target} の性別は {gender} です。")
else:
    print(f"{target} は見つかりませんでした。")
