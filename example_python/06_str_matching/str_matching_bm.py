"""str_matching_bm.py

-----------------------------------------------------------------------
BM法による文字列パターン照合のサンプルプログラム。

このプログラムではテキスト中にパターンの文字列が現れるかどうか
をBM法で探索するプログラムを実装しています。
"""


# ずらし表を作成する関数
def build_bad_character_table(pattern):
    m = len(pattern)
    table = {}

    for i in range(m - 1):
        table[pattern[i]] = m - 1 - i

    return table


# KMP法による文字列パターン照合
def bm_search(text, pattern):
    n = len(text)
    m = len(pattern)

    if m == 0:
        return []

    bad_char = build_bad_character_table(pattern)
    result = []

    i = 0  # textの開始位置

    while i <= n - m:
        j = m - 1

        # 右から比較
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1

        if j < 0:
            # 完全一致
            result.append(i)
            i += m
        else:
            # 不一致時のシフト
            shift = bad_char.get(text[i + j], m)
            i += max(1, shift - (m - 1 - j))

    return result


# ---------------------------------------------------------------------
# テキストとパターンの定義
text = "ababcabcabababdabababcabababdababd"
pattern = "ababd"
print(f"text   : {text}")
print(f"pattern: {pattern}")

# 文字列の探索
print("BM法で文字列を探索します。")
search_result = bm_search(text, pattern)

# 結果の表示
if len(search_result) > 0:
    for sr in search_result:
        print(f"該当箇所: {sr} 文字目")
else:
    print("該当なし")
