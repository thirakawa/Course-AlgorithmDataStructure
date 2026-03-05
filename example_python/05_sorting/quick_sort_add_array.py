"""quick_sort_add_array.py

-----------------------------------------------------------------------
クイックソートのサンプルプログラム。

このプログラムではランダムな配列に対してクイックソートを実行しています。

注意：
このプログラムで紹介するクイックソートは、in-place 方式の処理とは異なり、
追加の配列を使用して、左右に分割する処理を行なっています。
"""


# 左端を pivot にするクイックソート（追加配列方式）
def quick_sort_left(data):
    # 要素が1つ以下ならそのまま
    if len(data) <= 1:
        return data

    # 左端を基準 (pivot) にする
    pivot = data[0]

    left = []
    right = []

    # pivot以外を左右に分割
    # pivot以下の数を左に、pivotよりも大きな数を右に分ける
    for x in data[1:]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    # 再帰的にソート
    return quick_sort_left(left) + [pivot] + quick_sort_left(right)


# 右端を pivot にするクイックソート（追加配列方式）
def quick_sort_right(data):
    # 要素が1つ以下ならそのまま
    if len(data) <= 1:
        return data

    # 右端を基準 (pivot) にする
    pivot = data[-1]

    left = []
    right = []

    # pivot以外を左右に分割
    # pivot以下の数を左に、pivotよりも大きな数を右に分ける
    for x in data[:-1]:
        if x <= pivot:
            left.append(x)
        else:
            right.append(x)

    # 再帰的にソート
    return quick_sort_right(left) + [pivot] + quick_sort_right(right)


# ---------------------------------------------------------------------
# [左端 pivot クイックソート（追加配列方式）]
print("-" * 30)
print("左端をpivotとするクイックソート（追加配列方式）:")

# 配列の定義
data = [3, 5, 8, 1, 2, 9, 4, 7, 6]

# ソート前の配列の表示
print("ソート前:", data)

# クイックソート（左端pivot）の実行
print("クイックソート（左端pivot）を実行します。")
quick_sort_left(data)

# ソート後の配列の表示
print("ソート後:", data)

# ---------------------------------------------------------------------
# [右端 pivot クイックソート（追加配列方式）] 
print("-" * 30)
print("右端をpivotとするクイックソート（追加配列方式）:")

# 配列の定義
data = [3, 5, 8, 1, 2, 9, 4, 7, 6]

# ソート前の配列の表示
print("ソート前:", data)

# クイックソート（右端pivot）の実行
print("クイックソート（右端pivot）を実行します。")
quick_sort_right(data)

# ソート後の配列の表示
print("ソート後:", data)
