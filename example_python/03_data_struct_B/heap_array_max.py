"""heap_array_max.py

-----------------------------------------------------------------------
ヒープ（Heap）を扱うサンプルプログラム。

このプログラムでは配列（リスト）を使用して、
根ノードが最大値となるヒープ（Max-Heap）の構築を行なっています。

注意：
ヒープは完全二分木であり、配列を用いることで
効率的に実装できます。

親ノードと子ノードの関係は以下の式で求められます。

親: (i - 1) // 2
左の子: 2 * i + 1
右の子: 2 * i + 2
"""


# 最大ヒープを管理するクラス定義（配列版）
class MaxHeapArray:
    def __init__(self):
        self.heap = []  # ヒープ本体（配列）

    # データの挿入 ----------------------------------------
    def insert(self, value):
        # 配列の末尾に追加
        self.heap.append(value)

        # 上方向にヒープ調整
        self._heapify_up(len(self.heap) - 1)

    # 上方向にヒープ調整（親より大きい間、上に上げる）
    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] > self.heap[parent]:
                self.heap[index], self.heap[parent] = \
                    self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    # 最大値データの取得 ----------------------------------
    def pop_max(self):
        if not self.heap:
            return None

        # 根ノードの値（最大値）を取得
        max_value = self.heap[0]

        # 最後の値を取得
        last_value = self.heap.pop()

        # 要素が残っている場合
        if self.heap:
            self.heap[0] = last_value
            self._heapify_down(0)

        return max_value

    # 下方向にヒープ調整（子より小さい間、大きい子と交換して下に下げる）
    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            largest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] > self.heap[largest]:
                largest = left

            if right < size and self.heap[right] > self.heap[largest]:
                largest = right

            if largest == index:
                break

            self.heap[index], self.heap[largest] = \
                self.heap[largest], self.heap[index]

            index = largest

    # ヒープの表示 -----------------------------------------
    def print_heap(self):
        print(self.heap)


# ---------------------------------------------------------------------
# 最大ヒープの初期化（要素無し）
print("最大ヒープ（配列版）を構築します。")
heap_array = MaxHeapArray()

# データの追加
print("最大ヒープにデータを追加します。")
heap_array.insert(10)
heap_array.insert(4)
heap_array.insert(15)
heap_array.insert(20)
heap_array.insert(0)
heap_array.insert(8)

print("初期状態のヒープを表示します。")
heap_array.print_heap()

# ----------------------------------------------------------------
# データの新規追加
print("-" * 30)
print("6のデータを追加します。")
heap_array.insert(6)

print("6を追加したヒープを表示します。")
heap_array.print_heap()

# ----------------------------------------------------------------
# 最大値の取得
print("-" * 30)
print("最大値を取得（pop）します。")
max_value = heap_array.pop_max()
print("Max value:", max_value)

print("最大値を pop した後のヒープを表示します。")
heap_array.print_heap()
