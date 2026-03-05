"""linear_search.py

-----------------------------------------------------------------------
線形探索のサンプルプログラム。

このプログラムでは、探索する対象の値が存在する場所（配列のイン
デックス）を線形探索しています。
"""


# 線形探索の関数を定義
def linear_search(data, target):
    # 配列を先頭から順番に調べる
    for i in range(len(data)):
        # 見つかった位置（インデックス）を返す
        if data[i] == target:
            return i

    # 見つからなかった場合
    return None


# ---------------------------------------------------------------------
# 配列と探索対象の定義
data = [41, 7, 12, 1, 25, 19, 42, 52, 8, 10]
target = 25

print(f"探索対象 {target} の位置を線形探索します。")
print(f"探索する配列: {data}")

# 線形探索の実行
result = linear_search(data, target)

# 探索結果の表示
if result is not None:
    print("見つかりました。位置:", result)
else:
    print("見つかりませんでした。")
