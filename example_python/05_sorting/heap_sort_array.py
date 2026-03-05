"""heap_sort_array.py

-----------------------------------------------------------------------
ヒープソートのサンプルプログラム。

このプログラムでは自分で定義した配列版最大ヒープ（MaxHeapArray）
を使用してヒープソートを実行します。

注意：
このプログラムでは、配列版最大ヒープを活用します。
配列版（最大・最小）ヒープの動作については、
03_data_structにあるヒープのプログラムや講義を参照してください。
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


# ヒープソート（配列版）の関数
def heap_sort_array(data):

    heap = MaxHeapArray()

    # ① ヒープ構築
    for value in data:
        heap.insert(value)

    # ② 最大値を順に取り出す
    sorted_list = []

    while True:
        value = heap.pop_max()

        if value is None:
            break

        sorted_list.append(value)

    # ③ 昇順にする
    sorted_list.reverse()

    return sorted_list


# ---------------------------------------------------------------------
# 配列の定義
data = [15, 27, 3, 9, 30, 21, 6, 14, 33, 18]

# ソート前の配列の表示
print("ソート前:", data)

# ヒープソート（配列版）の実行
print("ヒープソート（配列版）を実行します。")
heap_sort_array(data)

# ソート後の配列の表示
print("ソート後:", data)
