"""merge_sort.py

-----------------------------------------------------------------------
マージソートのサンプルプログラム。

このプログラムではランダムな配列に対してマージソートを実行しています。
"""


# マージソート
def merge_sort(data):
    # 要素が1つ以下ならそのまま
    if len(data) <= 1:
        return data

    # 真ん中で分割（真ん中のインデックスを計算）
    mid = len(data) // 2

    # midよりも左側の配列をマージソート
    left = merge_sort(data[:mid])
    # midよりも右側の配列をマージソート
    right = merge_sort(data[mid:])

    # 再帰的にマージ（統合）
    return merge(left, right)


# ソート済みの left と right の配列を
# 正しい順序で一つにマージ（統合）
def merge(left, right):
    result = []
    i = 0
    j = 0

    # 小さい方を順番に追加
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 残りを追加
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# ---------------------------------------------------------------------
# 配列の定義
data = [15, 27, 3, 9, 30, 21, 6, 14, 33, 18]

# ソート前の配列の表示
print("ソート前:", data)

# マージソートの実行
print("マージソートを実行します。")
merge_sort(data)

# ソート後の配列の表示
print("ソート後:", data)
