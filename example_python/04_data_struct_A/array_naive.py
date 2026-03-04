"""array_naive.py

-----------------------------------------------------------------------
配列（Array）のサンプルプログラム。

Python標準の機能を使用せずにナイーブに実装した例を
示しています。

このプログラムでは、自分で定義したArrayクラスを使用して、
要素の追加と削除を行なっています。
"""


# 配列を自分で定義
class Array:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    # 配列の指定した番号（インデックス）の要素を取得
    def get(self, index):
        if 0 <= index < self.size:
            return self.data[index]
        raise IndexError("Index out of range")

    # 指定した場所（インデックス）に要素を追加
    def insert(self, index, value):
        if 0 <= index < self.size:
            for i in range(self.size - 2, index -1, -1):
                self.data[i + 1] = self.data[i]
            self.data[index] = value
        else:
            raise IndexError("Index out of range")

    # 指定した場所（インデックス）の要素を削除
    def remove(self, index):
        if 0 <= index < self.size:
            self.data[index] = None
            for i in range(index + 1, self.size):
                self.data[i - 1] = self.data[i]
                self.data[i] = None
        else:
            raise IndexError("Index out of range")


# ---------------------------------------------------------------------
# 配列の初期化
arr = Array(5)
arr.insert(0, "Blue")
arr.insert(1, "Red")
arr.insert(2, "Yellow")

# 配列の表示
print("配列の 0 番目の要素:", arr.get(0))
print("配列の 1 番目の要素:", arr.get(1))
print("配列の 2 番目の要素:", arr.get(2))
print("配列の 3 番目の要素:", arr.get(3))
print("配列の 4 番目の要素:", arr.get(4))

# ---------------------------------------------------------------------
# Blue と Red の間に Green を追加
print("-" * 10)
print("Greenを0番目と1番目の間に挿入します。")

arr.insert(1, "Green")  # 追加

# 配列の表示
print("配列の 0 番目の要素:", arr.get(0))
print("配列の 1 番目の要素:", arr.get(1))
print("配列の 2 番目の要素:", arr.get(2))
print("配列の 3 番目の要素:", arr.get(3))
print("配列の 4 番目の要素:", arr.get(4))

# ---------------------------------------------------------------------
# Red （配列の 2 番目の要素）を削除
print("-" * 10)
print("配列からRedを削除します。")

arr.remove(2)  # 削除

# 配列の表示
print("配列の 0 番目の要素:", arr.get(0))
print("配列の 1 番目の要素:", arr.get(1))
print("配列の 2 番目の要素:", arr.get(2))
print("配列の 3 番目の要素:", arr.get(3))
print("配列の 4 番目の要素:", arr.get(4))
