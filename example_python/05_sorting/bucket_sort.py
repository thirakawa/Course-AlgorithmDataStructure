"""bucket_sort.py

-----------------------------------------------------------------------
計数ソート（バケットソート）のサンプルプログラム。

このプログラムではランダムな配列に対して計数ソートを
実行しています。

注意：
下記では2種類の計数ソートの関数を実装しています。
bucket_sort() は講義で説明したアルゴリズムをシン
プルに実装した関数です。もう一つの
bucket_sort_stable() は安定性を保証した基数ソート
の関数です。bucket_sort_stable() は補足資料として
記述しておきますので、興味のある人は自身で調べてみ
てください。
"""


# 単純な計数ソート（バケットソート）
def bucket_sort(data, max_value=10):
    # 出現回数を格納する配列を初期化
    count = [0 for _ in range(max_value + 1)]

    # 各値の出現回数を数える
    for num in data:
        count[num] += 1

    # 数えた数だけ元の配列に値を戻す
    index = 0
    for i in range(len(count)):
        for _ in range(count[i]):
            data[index] = i
            index += 1


# [補足] 安定版の計数ソート
def bucket_sort_stable(data):
    if len(data) <= 1:
        return data

    # 最大値を求める
    max_value = max(data)

    # 出現回数を格納する配列（カウント配列）
    count = [0] * (max_value + 1)

    # 各値の出現回数を数える
    for num in data:
        count[num] += 1

    # 累積和を計算（安定ソートにするため）
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # 出力用配列
    output = [0] * len(data)

    # 後ろから処理して安定性を保つ
    for num in reversed(data):
        count[num] -= 1
        output[count[num]] = num

    # 元の配列へ戻す
    for i in range(len(data)):
        data[i] = output[i]


# ---------------------------------------------------------------------
# [単純な計数ソート（バケットソート）]
print("-" * 30)
print("単純な計数ソート（バケットソート）:")

# 配列の定義
data = [4, 2, 2, 8, 3, 3, 1, 5, 3, 6]

# ソート前の配列の表示
print("ソート前:", data)

# 単純な計数ソートの実行
print("計数ソートを実行します。")
bucket_sort(data, max_value=10)

# ソート後の配列の表示
print("ソート後:", data)

# ---------------------------------------------------------------------
# [補足：安定版計数ソート] 
print("-" * 30)
print("安定版計数ソート（バケットソート）:")

# 配列の定義
data = [4, 2, 2, 8, 3, 3, 1, 5, 3, 6]

# ソート前の配列の表示
print("ソート前:", data)

# 安定版計数ソートの実行
print("安定版計数ソートを実行します。")
bucket_sort_stable(data)

# ソート後の配列の表示
print("ソート後:", data)
