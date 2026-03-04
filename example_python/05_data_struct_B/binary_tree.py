"""binary_tree.py

-----------------------------------------------------------------------
二分木（Binary tree）を扱うサンプルプログラム。

このプログラムでは自分で定義したBinaryTreeNodeクラスと
BinaryTreeクラスを使用して、二分木の構築を行なっています。

注意：
木構造（二分木）の表示には、再帰呼び出しのアルゴリズムを使用
しています。再帰呼び出しについては12_recursive_algのプログラ
ムや講義を参照してください。
"""


# 二分木の単一ノードクラス定義
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value # ノードの持つ値（名前や数値など）
        self.right = None  # 右側の子ノード
        self.left = None   # 左側の小ノード


# 二分木全体を管理するクラス定義
class BinaryTree:
    def __init__(self, root_value):
        self.root = BinaryTreeNode(root_value)

    # 子ノードの追加（右側）
    def set_right(self, parent_node, value):
        if parent_node.right is not None:
            raise ValueError(f"Right child of {parent_node.value} is already defined")
        
        parent_node.right = BinaryTreeNode(value)
        return parent_node.right

    # 子ノードの追加（左側）
    def set_left(self, parent_node, value):
        if parent_node.left is not None:
            raise ValueError(f"Left child of {parent_node.value} is already defined")
        
        parent_node.left = BinaryTreeNode(value)
        return parent_node.left

    # 木構造の表示
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
# 二分木の初期化（根ノードのみ作成）
print("二分木を構築します。")
bin_tree = BinaryTree("A")

# 子ノードの追加
print("ノードを追加します。")  
node_b = bin_tree.set_right(bin_tree.root, "B")
node_c = bin_tree.set_left(bin_tree.root, "C")

node_d = bin_tree.set_right(node_b, "D")
node_e = bin_tree.set_left(node_b, "E")

node_f = bin_tree.set_right(node_c, "F")
node_g = bin_tree.set_left(node_c, "G")

node_h = bin_tree.set_right(node_d, "H")
node_i = bin_tree.set_left(node_d, "I")

# 二分木の表示
print("二分木を表示します。（rが右側、lが左側を示しています）")  
bin_tree.print_tree()
