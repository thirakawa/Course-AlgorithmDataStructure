"""03_repeating_struct.py

=======================================================================
反復構造（Repeating structure）のサンプルプログラム。

反復処理（繰り返し処理）を含む演算例を示しています。

このプログラムでは入力された正の整数（1以上の整数）をもとに、
1から入力された値（`n`）までの合計とnの階乗を計算して出力します。
"""


# 1以上の整数を入力
n = int(input("正の整数を入力してください: "))

# forループを使用してnまでの合計を計算
total = 0
for i in range(1, n + 1):
    total += i

# whileループを使用して階乗を計算
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

# 結果の表示
print(f"1 から {n} までの合計: {total}")
print(f"{n} の階乗: {factorial}")

print("プログラム終了")
