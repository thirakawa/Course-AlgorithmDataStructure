"""sieve_of_eratosthenes.py

-----------------------------------------------------------------------
エラトステネスのふるいで素数を求めるサンプルプログラム。

このプログラムでは事前に定義した n 以下の素数を
エラトステネスのふるいで求めるアルゴリズムを実装しています。
"""


# エラトステネスのふるいの関数
def sieve_of_eratosthenes(n):
    # 0〜n までの「素数かどうか」を管理
    is_prime = [True] * (n + 1)

    # 0 と 1 は素数ではない
    is_prime[0] = is_prime[1] = False

    # 2 から √n まで調べる
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            # i の倍数をすべて False にする
            for multiple in range(i * i, n + 1, i):
                is_prime[multiple] = False

    # 素数の一覧を作る
    primes = [i for i in range(n + 1) if is_prime[i]]
    return primes


# ---------------------------------------------------------------------
# 求めたい素数の最大値を定義
n = 100

# エラトステネスのふるいで素数を計算
print(f"{n} 以下の素数をエラトステネスのふるいで計算します。")
result = sieve_of_eratosthenes(n)

# 結果の表示
print(f"{n} 以下の素数は次のとおりです: {result}")
