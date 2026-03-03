"""hash_function.py

-----------------------------------------------------------------------
ハッシュ関数のサンプルプログラム。

いくつかの文字列データをハッシュ関数にかけてハッシュ値を計算
します。

このプログラムではいくつかのハッシュ関数（ハッシュ値の計算方法）
を実装します。

MD5・SHA256（SHA-2の一種）については hashlib モジュールに実装
されている関数を使用してその結果を確認します。
"""


import hashlib


# シンプルなハッシュ関数（ASCIIの合計値）
def hash_simple(key):
    total = 0
    for char in key:
        num = ord(char)  # 一文字ずつASCIIコード（Unicode整数）に変換
        total += num     # 変換した整数を加算
    return total


# MD5形式のハッシュ関数
def hash_md5(key):
    # 16進数表現のハッシュ値
    hash_md5_hex = hashlib.md5(key.encode()).hexdigest()
    # 10進数表現のハッシュ値
    hash_md5_dec = int(hash_md5_hex, 16)
    return hash_md5_hex, hash_md5_dec


# SHA256形式（SHA-2の一種）のハッシュ関数
def hash_sha256(key):
    # 16進数表現のハッシュ値
    hash_sha256_hex = hashlib.sha256(key.encode()).hexdigest()
    # 10進数表現のハッシュ値
    hash_sha256_dec = int(hash_sha256_hex, 16)
    return hash_sha256_hex, hash_sha256_dec


# ---------------------------------------------------------------------
# キーの準備
keys = ["Joe", "Sue", "Dan", "Nell", "Ally", "Bob"]


# ---------------------------------------------------------------------
# シンプルなハッシュ関数の実行結果
print("-" * 10)
print("シンプルなハッシュ関数の実行結果")
for key in keys:
    hash_value = hash_simple(key)
    print(f"キー: {key}, ハッシュ値: {hash_value}")

# ---------------------------------------------------------------------
# MD5形式のハッシュ関数の実行結果
print("-" * 10)
print("MD5形式のハッシュ関数の実行結果")
for key in keys:
    hash_value_hex, hash_value_dec = hash_md5(key)
    print(f"キー: {key}, ハッシュ値 [16進数]: {hash_value_hex},  [10進数]: {hash_value_dec}")

# ---------------------------------------------------------------------
# SHA256形式（SHA-2の一種）のハッシュ関数の実行結果
print("-" * 10)
print("SHA256形式（SHA-2の一種）のハッシュ関数の実行結果")
for key in keys:
    hash_value_hex, hash_value_dec = hash_sha256(key)
    print(f"キー: {key}, ハッシュ値 [16進数]: {hash_value_hex},  [10進数]: {hash_value_dec}")
