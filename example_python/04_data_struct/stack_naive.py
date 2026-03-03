"""stack_naive.py

-----------------------------------------------------------------------
スタック（Stack）のサンプルプログラム。

Python標準の機能を使用せずにナイーブに実装した例を
示しています。

このプログラムでは、自分で定義したStackクラスを使用して、
要素の追加（Push）と取り出し（Pop）を行なっています。

PushとPopに追加して、先頭の要素を取り出さずに参照する
Peek / Topについても実装を行なっています。
"""


class Stack:
    def __init__(self, capacity):
        self.capacity = capacity       # 最大要素数
        self.data = [None] * capacity  # 固定長配列
        self.top = -1                  # スタックの先頭位置(-1の場合は要素なし)

    # スタックが空かどうかを判定
    def is_empty(self):
        return self.top == -1

    # スタックがいっぱいか（capacityの数だけ要素が埋まっているか）を判定
    def is_full(self):
        return self.top == self.capacity - 1

    # Push（スタックの先頭に要素を追加）
    def push(self, value):
        if self.is_full():
            raise OverflowError("Stack is full")
        self.top += 1
        self.data[self.top] = value

    # Pop（スタックの先頭の要素を取り出す）
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        value = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return value

    # Peek / Top（スタックの先頭の要素を取り出さずに参照）
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.data[self.top]

    # 現在スタックに格納されている要素のみを文字列として返す
    def __str__(self):
        return str(self.data[:self.top + 1])


# ---------------------------------------------------------------------
# スタックの初期化
stack = Stack(5)
stack.push("Blue")
stack.push("Red")
stack.push("Yellow")

# スタック全体を表示（本来は全体を表示できないことに注意）
print(f"スタック全体: {stack}")

# ---------------------------------------------------------------------
# [Push] 先頭に Green を追加
print("-" * 10)
print("GreenをPushします。")

stack.push("Green")  # 追加

# スタック全体を表示（本来は全体を表示できないことに注意）
print(f"スタック全体: {stack}")

# ---------------------------------------------------------------------
# [Pop] 先頭のデータの取り出し
print("-" * 10)
print("スタックからデータをPopします。")

pop_data = stack.pop()

# 取り出したデータを表示
print(f"Popしたデータ: {pop_data}")

# スタック全体を表示（本来は全体を表示できないことに注意）
print(f"スタック全体: {stack}")

# ---------------------------------------------------------------------
# [Peek] 先頭のデータを参照（取り出さない）
print("-" * 10)
print("スタックの先頭データを参照します。")

peek_data = stack.peek()

# 取り出したデータを表示
print(f"参照した先頭データ: {peek_data}")

# スタック全体を表示（本来は全体を表示できないことに注意）
print(f"スタック全体: {stack}")
