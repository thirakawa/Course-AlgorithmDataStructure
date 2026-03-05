"""heap_array_min.py

-----------------------------------------------------------------------
ヒープ（Heap）を扱うサンプルプログラム。

このプログラムでは配列（リスト）を使用して、
根ノードが最小値となるヒープ（Min-Heap）の構築を行なっています。

注意：
ヒープは完全二分木であり、配列を用いることで
効率的に実装できます。

親ノードと子ノードの関係は以下の式で求められます。

親: (i - 1) // 2
左の子: 2 * i + 1
右の子: 2 * i + 2
"""


# 最小ヒープを管理するクラス定義（配列版）
class MinHeapArray:
    def __init__(self):
        self.heap = []  # ヒープ本体（配列）

    # データの挿入 ----------------------------------------
    def insert(self, value):
        # 配列の末尾に追加
        self.heap.append(value)

        # 上方向にヒープ調整
        self._heapify_up(len(self.heap) - 1)

    # 上方向にヒープ調整（親より小さい間、上に上げる）
    def _heapify_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = \
                    self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    # 最小値データの取得 ----------------------------------
    def pop_min(self):
        if not self.heap:
            return None

        # 根ノードの値（最小値）を取得
        min_value = self.heap[0]

        # 最後の値を取得
        last_value = self.heap.pop()

        # 要素が残っている場合
        if self.heap:
            self.heap[0] = last_value
            self._heapify_down(0)

        return min_value

    # 下方向にヒープ調整（子より大きい間、小さい子と交換して下に下げる）
    def _heapify_down(self, index):
        size = len(self.heap)

        while True:
            smallest = index
            left = 2 * index + 1
            right = 2 * index + 2

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = \
                self.heap[smallest], self.heap[index]

            index = smallest

    # ヒープの表示 -----------------------------------------
    def print_heap(self):
        print(self.heap)


# ---------------------------------------------------------------------
# 最小ヒープの初期化（要素無し）
print("最小ヒープ（配列版）を構築します。")
heap_array = MinHeapArray()

# データの追加
print("最小ヒープにデータを追加します。")
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
# 最小値の取得
print("-" * 30)
print("最小値を取得（pop）します。")
min_value = heap_array.pop_min()
print("Min value:", min_value)

print("最小値を pop した後のヒープを表示します。")
heap_array.print_heap()
