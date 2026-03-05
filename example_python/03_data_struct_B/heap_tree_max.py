"""heap_tree_max.py

-----------------------------------------------------------------------
ヒープ（Heap）を扱うサンプルプログラム。

このプログラムでは自分で定義したHeapNodeクラスと
MinHeapTreeクラスを使用して、根ノードが最大値となるヒープ
（Max-Heap）の構築を行なっています。

注意1：
このプログラムでは、データ構造の一つであるキュー（Queue）を
内部で使用します。キューの動作については、04_data_structに
あるキューのプログラムや講義を参照してください。

注意2：
二分探索木の表示には、再帰呼び出しのアルゴリズムを使用
しています。再帰呼び出しについては12_recursive_algのプログラ
ムや講義を参照してください。
"""


from collections import deque


# ヒープのノードクラス
class HeapNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


# 最小ヒープを管理するクラス定義
class MaxHeapTree:
    def __init__(self):
        self.root = None  # 根ノード

    # データの挿入 ----------------------------------------
    def insert(self, value):
        new_node = HeapNode(value)

        if self.root is None:
            self.root = new_node
            return

        # 完全二分木を維持するため幅優先探索
        queue = deque([self.root])
        while queue:
            current = queue.popleft()

            if current.left is None:
                current.left = new_node
                new_node.parent = current
                break
            else:
                queue.append(current.left)

            if current.right is None:
                current.right = new_node
                new_node.parent = current
                break
            else:
                queue.append(current.right)

        self._heapify_up(new_node)

    # 上方向にヒープ調整（親より大きい間、上に上げる）
    def _heapify_up(self, node):
        while node.parent and node.value > node.parent.value:
            node.value, node.parent.value = node.parent.value, node.value
            node = node.parent

    # 最大値データの取得 ----------------------------------
    def pop_max(self):
        if self.root is None:
            return None

        # 根ノードの値（最大値）を取得
        max_value = self.root.value

        # 最後のノードを取得
        queue = deque([self.root])
        last_node = None

        while queue:
            last_node = queue.popleft()
            if last_node.left:
                queue.append(last_node.left)
            if last_node.right:
                queue.append(last_node.right)

      # 最後のノードが根ノードの場合
        if last_node == self.root:
            self.root = None
            return max_value

        # ルートに最後の値を移す
        self.root.value = last_node.value

        # 最後のノード削除
        if last_node.parent.left == last_node:
            last_node.parent.left = None
        else:
            last_node.parent.right = None

        self._heapify_down(self.root)

        return max_value

    # 下方向ヒープ調整（子より小さい間、大きい子と交換して下に下げる）
    def _heapify_down(self, node):
        while node:
            largest = node

            if node.left and node.left.value > largest.value:
                largest = node.left

            if node.right and node.right.value > largest.value:
                largest = node.right

            if largest == node:
                break

            node.value, largest.value = largest.value, node.value
            node = largest

    # ヒープ表示 ------------------------------------------
    def print_tree(self):
        self._print_tree(self.root, 0)

    # 実際の再帰処理（内部用）
    def _print_tree(self, node, level):
        if node is not None:
            self._print_tree(node.right, level + 1)
            print(" " * (2 * level) + str(node.value))
            self._print_tree(node.left, level + 1)


# ---------------------------------------------------------------------
# 最大ヒープの初期化（ノード無し）
print("最大ヒープを構築します。")
heap_tree = MaxHeapTree()

# データの追加
print("最大ヒープにデータを追加します。")  
heap_tree.insert(10)
heap_tree.insert(4)
heap_tree.insert(15)
heap_tree.insert(20)
heap_tree.insert(0)
heap_tree.insert(8)

print("初期状態のヒープを表示します。")
heap_tree.print_tree()

# ----------------------------------------------------------------
# データの新規追加
print("-" * 30)
print("6のデータを追加します。")
heap_tree.insert(6)

print("6を追加したヒープを表示します。")
heap_tree.print_tree()

# ----------------------------------------------------------------
# 最大値の取得
print("-" * 30)
print("最大値を取得（pop）します。")
max_value = heap_tree.pop_max()
print("Max value:", max_value)

print("最大値を pop した後のヒープを表示します")
heap_tree.print_tree()
