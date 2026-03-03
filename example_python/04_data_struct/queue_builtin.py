"""queue_builtin.py

-----------------------------------------------------------------------
キュー（Queue）のサンプルプログラム。

Python標準の機能（collections.deque）を使用した例を
示しています。

Pythonには「deque」というキュー（両端キュー）が標準で
用意されています。ここでは、dequeを使用してキューの
使用例を紹介します。

注意1：
dequeは "double-ended queue" の略で、両端キューという
データ構造です。両端キューは前後どちらからも要素を
追加（enqueue）・削除（dequeue）できるデータ構造です。

注意2：
Python のdequeは、両端キューですが、本講義では通常の
FIFOキューとして使用します。
"""

from collections import deque


# ---------------------------------------------------------------------
# キューの初期化
# append がスタックにおける push の役割を果たす
q = deque()
q.append("Blue")
q.append("Red")
q.append("Yellow")

# キュー全体を表示（本来は全体を表示できないことに注意）
print(f"キュー全体: {q}")

# ---------------------------------------------------------------------
# [Enqueue] キューに Green を追加
# Python標準の deque では append で要素を追加
print("-" * 10)
print("キューにGreenをEnqueueします。")

q.append("Green")  # 追加

# キュー全体を表示（本来は全体を表示できないことに注意）
print(f"キュー全体: {q}")

# ---------------------------------------------------------------------
# [Dequeue] 先頭のデータの取り出し
# Python標準の deque では popleft で要素を追加
print("-" * 10)
print("キューからデータをEnqueueします。")

data = q.popleft()  # 取り出し

# 取り出したデータを表示
print(f"Enqueueしたデータ: {data}")

# スタック全体を表示（本来は全体を表示できないことに注意）
print(f"スタック全体: {q}")
