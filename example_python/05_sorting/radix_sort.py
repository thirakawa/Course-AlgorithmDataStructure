"""radix_sort.py

-----------------------------------------------------------------------
基数ソートのサンプルプログラム。

このプログラムではランダムな配列に対して基数ソートを
実行しています。

注意：
このプログラムでは、非負の整数を対象とした基数ソートを
実装しています。
"""


from collections import deque


# 基数
def radix_sort(data):
    if len(data) <= 1:
        return data

    # 最大値（何桁処理するかを求めるため）
    max_value = max(data)

    exp = 1  # 1の位から開始

    # 各桁ごとに基数ソートを適用
    while max_value // exp > 0:
        bucket_sort_by_digit(data, exp)
        exp *= 10  # 1 --> 10 --> 100


# 指定した桁の数値 (0 ~ 9) で基数ソート（バケットソート）
def bucket_sort_by_digit(data, exp):
    # キューの配列を用意
    queue_list = list([deque() for _ in range(10)])

    # 対応する場所のキューにデータを追加 (enqueue)
    for num in data:
        digit = (num // exp) % 10
        queue_list[digit].append(num)

    # 元の配列へ先頭から順番に戻す (dequeue)
    index = 0
    for q in queue_list:
        while q:
            data[index] = q.popleft()
            index += 1


# ---------------------------------------------------------------------
# [基数ソート]
print("-" * 30)
print("基数ソート")

# 配列の定義
data = [170, 45, 75, 90, 802, 24, 2, 66]

# ソート前の配列の表示
print("ソート前:", data)

# 単純な基数ソートの実行
print("基数ソートを実行します。")
radix_sort(data)

# ソート後の配列の表示
print("ソート後:", data)
