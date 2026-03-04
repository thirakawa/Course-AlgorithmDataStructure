"""binary_search_tree.py

-----------------------------------------------------------------------
二分探索木（Binary search tree）を扱うサンプルプログラム。

このプログラムでは自分で定義したBSTNodeクラスと
BinarySearchTreeクラスを使用して、二分探索木の構築を行なっ
ています。

注意：
二分探索木の表示には、再帰呼び出しのアルゴリズムを使用
しています。再帰呼び出しについては12_recursive_algのプログラ
ムや講義を参照してください。
"""


# 二分探索木の単一ノードクラス定義
class BSTNode:
    def __init__(self, value):
        self.value = value # ノードの持つ値（名前や数値など）
        self.right = None  # 右側の子ノード
        self.left = None   # 左側の小ノード


# 二分探索木全体を管理するクラス定義
class BinarySearchTree:
    def __init__(self):
        self.root = None  # 根ノード

    # データの挿入 ----------------------------------------
    def insert(self, value):
        if self.root is None:
            self.root = BSTNode(value)
        else:
            self._insert(self.root, value)

    # 根ノード以外の場合のデータの追加（再起呼び出しを使用）
    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = BSTNode(value)
            else:
                self._insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = BSTNode(value)
            else:
                self._insert(current_node.right, value)

    # データの探索 ----------------------------------------
    def search(self, value):
        # 根ノードから value を探索を開始
        return self._search(self.root, value)

    # 実質的な探索の処理（再帰呼び出しを使用）
    def _search(self, current_node, value):
        if current_node is None:
            return None

        if value == current_node.value:
            return current_node
        elif value < current_node.value:
            return self._search(current_node.left, value)
        else:
            return self._search(current_node.right, value)

    # データの削除 ----------------------------------------
    def delete(self, value):
        # 根ノードから value の探索と削除を開始
        self.root = self._delete(self.root, value)

    # 実質的な削除の処理（再帰呼び出しを使用）
    def _delete(self, current_node, value):
        # 次に行くべき子ノードがない（一つ手前が葉ノード）場合
        if current_node is None:
            return None

        # value が現在のノードよりも小さい場合（左に進む）
        if value < current_node.value:
            current_node.left = self._delete(current_node.left, value)

        # value が現在のノードよりも大きい場合（右に進む）
        elif value > current_node.value:
            current_node.right = self._delete(current_node.right, value)

        # 現在のノードと value が同じ値の場合（削除対象を発見）
        else:
            # 1. 子ノードがない場合（Noneを返して親ノードから見た子ノードの情報をNoneにする）
            if current_node.left is None and current_node.right is None:
                return None

            # 2. 子ノードが1つの場合（現在のノードの子ノードを親ノードに対する子ノードにする）
            if current_node.left is None:
                return current_node.right
            if current_node.right is None:
                return current_node.left

            # 3. 子ノードが2つある場合
            # （左側のノード以下で最大値のノードを探して親ノードに対する子ノードにする）
            max_node = self._find_max(current_node.left)
            current_node.value = max_node.value
            current_node.left = self._delete(current_node.left, max_node.value)

        return current_node

    # node 以下の部分木で最大の値のノードを探索
    def _find_max(self, node):
        while node.right is not None:
            node = node.right
        return node

    # 二分探索木の表示-------------------------------------
    def print_tree(self, node=None, level=0, prefix="-"):
        if node is None:
            node = self.root

        # 現在のノードの表示
        print("  " * level + f"{prefix} {node.value}")

        # 子ノードの表示（再帰呼び出しを使用）
        if node.right:
            self.print_tree(node.right, level + 1, prefix="r:")
        if node.left:
            self.print_tree(node.left, level + 1, prefix="l:")


# ---------------------------------------------------------------------
# 二分探索木の初期化（ノード無し）
print("二分探索木を構築します。")
bst = BinarySearchTree()

# データの追加
print("二分探索木にデータを追加します。")  
bst.insert(15)
bst.insert(3)
bst.insert(12)
bst.insert(8)
bst.insert(17)
bst.insert(28)
bst.insert(9)
bst.insert(23)

print("初期状態の二分探索木を表示します。（rが右側、lが左側を示しています）")
bst.print_tree()

# ----------------------------------------------------------------
# データの新規追加
print("-" * 30)
print("11のデータを追加します。")
bst.insert(4)

print("11を追加した二分探索木を表示します。（rが右側、lが左側を示しています）")
bst.print_tree()

# ----------------------------------------------------------------
# データの探索
print("-" * 30)
print("23のデータがあるか探索します。")
node = bst.search(23)
print(f"Found: {node.value}" if node else "Not Found")

print("次に、7のデータがあるか探索します。")
node = bst.search(7)
print(f"Found: {node.value}" if node else "Not Found")

# ----------------------------------------------------------------
# データの新規追加
print("-" * 30)
print("8のデータを削除します。")
bst.delete(8)

print("8を削除した二分探索木を表示します。（rが右側、lが左側を示しています）")
bst.print_tree()
