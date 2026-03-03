"""queue_naive_linear.py

-----------------------------------------------------------------------
キュー（Queue）のサンプルプログラム。

Python標準の機能を使用せずにナイーブに実装した例を
示しています。

このプログラムでは、LinearQueueクラスを自分で定義して、
要素の追加（Enqueue）と取り出し（Dequeue）を行なっていま
す。また、先頭の要素を取り出さずに参照するPeek / Topに
ついても実装を行なっています。

このプログラムでは、いわゆる線形キュー（Linear queue）
と呼ばれるもっともシンプルなキューを実装します。この際、
要素の取り出しを行うと先頭の配列要素が使用できなくなり、
メモリに無駄が生まれやすい構造となっています。
"""


class LinearQueue:
    def __init__(self, capacity):
        self.capacity = capacity       # 最大要素数
        self.data = [None] * capacity  # 固定長配列
        self.front = 0                 # 取り出し位置
        self.rear = 0                  # 追加位置

    # キューが空かどうかを判定
    def is_empty(self):
        return self.front == self.rear

    # キューがいっぱいか（capacityの数だけ要素が埋まっているか）を判定
    def is_full(self):
        return self.rear == self.capacity

    # Enqueue（キューの後方に要素を追加）
    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")

        self.data[self.rear] = value
        self.rear += 1

    # Dequeue（キューの前方から要素を取り出す）
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        value = self.data[self.front]
        self.data[self.front] = None
        self.front += 1
        return value

    # Peek / Top（キューの先頭の要素）
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data[self.front]

    # 現在キューに格納されている要素のみを文字列として返す
    def __str__(self):
        return str(self.data)


# ---------------------------------------------------------------------
# キューの初期化
q = LinearQueue(5)

q.enqueue("Blue")
q.enqueue("Red")
q.enqueue("Yellow")

# キュー全体を表示（本来は全体を表示できないことに注意）
print(f"キュー全体: {q}")

# ---------------------------------------------------------------------
# [Enqueue] キューに Green を追加
print("-" * 10)
print("キューにGreenをEnqueueします。")

q.enqueue("Green")  # 追加

# キュー全体を表示（本来は全体を表示できないことに注意）
print(f"キュー全体: {q}")

# ---------------------------------------------------------------------
# [Dequeue] 先頭のデータの取り出し
print("-" * 10)
print("キューからデータをEnqueueします。")

data = q.dequeue()  # 取り出し

# 取り出したデータを表示
print(f"Enqueueしたデータ: {data}")

# スタック全体を表示（本来は全体を表示できないことに注意）
print(f"スタック全体: {q}")

# ---------------------------------------------------------------------
# [Peek] 先頭のデータを参照（取り出さない）
print("-" * 10)
print("キューの先頭データを参照します。")

peek_data = q.peek()

# 取り出したデータを表示
print(f"参照した先頭データ: {peek_data}")

# キュー全体を表示（本来は全体を表示できないことに注意）
print(f"キュー全体: {q}")
