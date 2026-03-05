"""str_matching_naive.py

-----------------------------------------------------------------------
素朴な方法による文字列パターン照合のサンプルプログラム。

このプログラムではテキスト中にパターンの文字列が現れるかどうか
を素朴な方法で探索するプログラムを実装しています。
"""


# 素朴な文字列パターン照合
def naive_search(text, pattern):
    n = len(text)     # テキストの文字数
    m = len(pattern)  # パータンの文字数

    # パターンに合致した先頭のインデックスを保存
    result = []

    # 先頭から一文字ずつずらしながら文字列を比較
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            # 比較結果が異なっていた場合は照合をやめて次にずらす
            if text[i + j] != pattern[j]:
                match = False
                break
        
        # パターンに合致した場合はその先頭のインデックスを追加
        if match:
            result.append(i)

    return result


# ---------------------------------------------------------------------
# テキストとパターンの定義
text = "ababcabcabababdabababcabababdababd"
pattern = "ababd"
print(f"text   : {text}")
print(f"pattern: {pattern}")

# 文字列の探索
print("素朴な方法で文字列を探索します。")
search_result = naive_search(text, pattern)

# 結果の表示
if len(search_result) > 0:
    for sr in search_result:
        print(f"該当箇所: {sr} 文字目")
else:
    print("該当なし")
