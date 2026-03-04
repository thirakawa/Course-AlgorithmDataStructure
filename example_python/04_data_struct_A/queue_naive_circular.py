"""queue_naive_circular.py

-----------------------------------------------------------------------
キュー（Queue）のサンプルプログラム。

Python標準の機能を使用せずにナイーブに実装した例を
示しています。

このプログラムでは、CircularQueueクラスを自分で定義して、
要素の追加（Enqueue）と取り出し（Dequeue）を行なっていま
す。また、先頭の要素を取り出さずに参照するPeek / Topに
ついても実装を行なっています。

このプログラムでは、いわゆる循環キュー（Circular queue）
と呼ばれるもっともキューを実装します。線形キューでは
Dequeueを行うと、先頭のメモリが使用できなくなり、メモリに
無駄が生まれやすいという問題がありました。循環キューでは、
確保した配列の最後まで使用をしたら、追加位置を指し示す情報
を先頭に戻して再度メモリを使用することができるキューとなって
おり、確保したメモリを効率的に使用することができます。
"""


# 循環キューを自分で定義
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity       # 最大要素数
        self.data = [None] * capacity  # 固定長配列
        self.front = 0                 # 取り出し位置
        self.rear = 0                  # 追加位置
        self.size = 0                  # 現在の要素数

    # キューが空かどうかを判定
    def is_empty(self):
        return self.size == 0

    # キューがいっぱいか（capacityの数だけ要素が埋まっているか）を判定
    def is_full(self):
        return self.size == self.capacity

    # Enqueue（キューの後方に要素を追加）
    def enqueue(self, value):
        if self.is_full():
            raise OverflowError("Queue is full")

        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    # Dequeue（キューの前方から要素を取り出す）
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")

        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return value

    # Peek / Top（キューの先頭の要素）
    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data[self.front]

    def __str__(self):
        return str(self.data)


# ---------------------------------------------------------------------
# キューの初期化
q = CircularQueue(5)

q.enqueue("Blue")
q.enqueue("Red")
q.enqueue("Yellow")
q.enqueue("White")

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
# [Enqueue] キューに Pink を追加
print("-" * 10)
print("キューにPinkをEnqueueします。")

q.enqueue("Pink")  # 追加

# キュー全体を表示（本来は全体を表示できないことに注意）
print(f"キュー全体: {q}")

# ---------------------------------------------------------------------
# [Peek] 先頭のデータを参照（取り出さない）
print("-" * 10)
print("キューの先頭データを参照します。")

peek_data = q.peek()

# 取り出したデータを表示
print(f"参照した先頭データ: {peek_data}")

# キュー全体を表示（本来は全体を表示できないことに注意）
print(f"キュー全体: {q}")
