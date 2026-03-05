"""quick_sort_lomuto.py

-----------------------------------------------------------------------
クイックソートのサンプルプログラム。

このプログラムではランダムな配列に対してクイックソートを
実行しています。

注意1：
このプログラムで紹介するクイックソートでは、追加の配列を
使用せず、対象のデータが格納された配列のみを用いて処理を
行います。この方式を in-place 方式と呼びます。

注意2：
このプログラムで紹介するクイックソートの処理はpivotの反対
側からpivot方向に向かって進み、pivotより小さいものは左へ、
大きいものは右へ入れ替えていく方法で処理を行い、pivotを基
準に左右に分割（partition）して整理を行います。このように
1本の走査で処理する方式を Lomuto partition と呼びます。
"""


# 左端を pivot にする in-place クイックソート
# Lomuto partition 方式
def quick_sort_lomuto_left(data, left, right):
    if left >= right:
        return

    pivot = data[left]  # 左端を pivot にする

    i = left + 1
    j = right

    while True:
        # pivotより小さい間、右へ進む
        while i <= right and data[i] <= pivot:
            i += 1

        # pivotより大きい間、左へ進む
        while j >= left + 1 and data[j] > pivot:
            j -= 1

        if i > j:
            break

        # 逆転していたら交換
        data[i], data[j] = data[j], data[i]

    # pivot を正しい位置へ
    data[left], data[j] = data[j], data[left]

    # 再帰的に左右の配列を処理
    quick_sort_lomuto_left(data, left, j - 1)
    quick_sort_lomuto_left(data, j + 1, right)


# 右端を pivot にする in-place クイックソート
# Lomuto partition 方式
def quick_sort_lomuto_right(data, left, right):
    if left >= right:
        return

    pivot = data[right]  # 右端を pivot にする

    i = left
    j = right - 1

    while True:
        # pivotより小さい間、右へ進む
        while i <= right - 1 and data[i] <= pivot:
            i += 1

        # pivotより大きい間、左へ進む
        while j >= left and data[j] > pivot:
            j -= 1

        if i > j:
            break

        # 逆転していたら交換
        data[i], data[j] = data[j], data[i]

    # pivot を正しい位置へ
    data[right], data[i] = data[i], data[right]

    # 再帰的に左右の配列を処理
    quick_sort_lomuto_right(data, left, i - 1)
    quick_sort_lomuto_right(data, i + 1, right)


# ---------------------------------------------------------------------
# [左端 pivot クイックソート（Lomuto partition）]
print("-" * 30)
print("左端をpivotとするクイックソート（Lomuto partition）:")

# 配列の定義
data = [3, 5, 8, 1, 2, 9, 4, 7, 6]

# ソート前の配列の表示
print("ソート前:", data)

# クイックソート（左端pivot）の実行
print("クイックソート（左端pivot）を実行します。")
quick_sort_lomuto_left(data, 0, len(data) - 1)

# ソート後の配列の表示
print("ソート後:", data)

# ---------------------------------------------------------------------
# [右端 pivot クイックソート（Lomuto partition）] 
print("-" * 30)
print("右端をpivotとするクイックソート（Lomuto partition）: ")

# 配列の定義
data = [3, 5, 8, 1, 2, 9, 4, 7, 6]

# ソート前の配列の表示
print("ソート前:", data)

# クイックソート（右端pivot）の実行
print("クイックソート（右端pivot）を実行します。")
quick_sort_lomuto_right(data, 0, len(data) - 1)

# ソート後の配列の表示
print("ソート後:", data)
