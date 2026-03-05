"""selection_sort.py

-----------------------------------------------------------------------
選択ソートのサンプルプログラム。

このプログラムではランダムな配列に対して選択ソートを実行しています。
"""


# 選択ソート
def selection_sort(data):
    # 配列の長さ（データの数）を取得
    n = len(data)

    for i in range(n - 1):
         # 最小値の位置（配列のインデックス）
        min_index = i

        # 未整列部分から最小値を探す
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j

        # 見つかった最小値と i 番目の要素を入れ替え
        data[i], data[min_index] = data[min_index], data[i]

    return data


# ---------------------------------------------------------------------
# 配列の定義
data = [15, 27, 3, 9, 30, 21, 6, 14, 33, 18]

# ソート前の配列の表示
print("ソート前:", data)

# 選択ソートの実行
print("選択ソートを実行します。")
selection_sort(data)

# ソート後の配列の表示
print("ソート後:", data)
