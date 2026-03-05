"""tower_of_hanoi.py

-----------------------------------------------------------------------
再帰呼び出し（再帰処理）によるハノイの塔のサンプルプログラム。

このプログラムでは再帰呼び出しを使用してハノイの塔の移動手順を
計算するプログラムを実装しています。
"""


# ハノイの塔の移動手順を計算する関数
def hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"{source} → {target}")
        return

    # 1. 上の n-1 枚を補助棒へ
    hanoi(n - 1, source, target, auxiliary)

    # 2. 一番下を目的棒へ
    print(f"{source} → {target}")

    # ③3. 補助棒の n-1 枚を目的棒へ
    hanoi(n - 1, auxiliary, source, target)


# ---------------------------------------------------------------------
# 塔の段数・柱（棒）の名前の定義
n = 4
src = "A"
trg = "C"
aux = "B"

print("ハノイの塔の設定:")
print(f"  塔の段数: {n}")
print(f"  柱（棒）の名前:")
print(f"  出発棒: {src}, 補助棒: {aux}, 目的棒: {trg}")

print(f"{src} から {trg} へハノイの塔を移動させる手順を計算します。")
hanoi(n, "A", "B", "C")
