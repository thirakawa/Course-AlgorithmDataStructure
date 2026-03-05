"""binary_search.py

-----------------------------------------------------------------------
二分探索のサンプルプログラム。

このプログラムでは、探索する対象の値が存在する場所（配列のイン
デックス）を二分探索しています。
"""


# 二分探索の関数を定義
def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        # 中央の位置（インデックス）
        mid = (left + right) // 2

        # 見つかった場合
        if data[mid] == target:
            return mid      # インデックスを返す
        
        # 探索対象よりも値が小さい場合
        elif data[mid] < target:
            left = mid + 1  # 右半分を探索
        
        # 探索対象よりも値が大きい場合
        else:
            right = mid - 1  # 左半分を探索

    # 見つからなかった場合
    return None


# ---------------------------------------------------------------------
# 配列（集合）と探索対象の定義
# 注意：二分探索では必ずソートされた配列を使用
data = [1, 4, 8, 12, 17, 21, 26, 30, 35, 42]
target = 30

print(f"探索対象 {target} の位置を二分探索します。")
print(f"探索する配列（集合）: {data}")

# 線形探索の実行
result = binary_search(data, target)

# 探索結果の表示
if result is not None:
    print("見つかりました。位置:", result)
else:
    print("見つかりませんでした。")
