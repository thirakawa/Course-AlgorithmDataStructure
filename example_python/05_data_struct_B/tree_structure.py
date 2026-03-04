"""tree_structure.py

-----------------------------------------------------------------------
木構造（Tree structure）を扱うサンプルプログラム。

このプログラムでは自分で定義したTreeNodeクラスとTreeクラ
スを使用して、木構造の構築を行なっています。

注意：
木構造の表示には、再帰呼び出しのアルゴリズムを使用しています。
再帰呼び出しについては12_recursive_algのプログラムや講義を参
照してください。
"""


# 木構造の単一ノードのクラス定義
class TreeNode:
    def __init__(self, value):
        # ノードの持つ値（名前や数値など）
        self.value = value
        # 子ノードのリスト
        self.children = []

    # 小ノードの追加
    def add_child(self, child_node):
        self.children.append(child_node)


# 木構造全体を管理するクラス定義
class Tree:
    def __init__(self, root_value):
        # 根ノード（root node）の作成
        self.root = TreeNode(root_value)

    # 子ノードの追加
    def add_child(self, parent_node, value):
        new_node = TreeNode(value)
        parent_node.add_child(new_node)
        return new_node

    # 木構造の表示
    def print_tree(self, node=None, level=0):
        if node is None:
            node = self.root

        # 現在のノードの表示
        print("  " * level + str(node.value))

        # 子ノードの表示（再帰呼び出しを使用）
        for child in node.children:
            self.print_tree(child, level + 1)


# ---------------------------------------------------------------------
# 木構造の初期化（根ノードのみ作成）
print("木構造を構築します。")
tree = Tree(root_value="A")

# 子ノードの追加
print("ノードを追加します。")  
node_b = tree.add_child(tree.root, "B")
node_c = tree.add_child(tree.root, "C")
node_d = tree.add_child(node_b, "D")
node_e = tree.add_child(node_b, "E")
node_f = tree.add_child(node_c, "F")
node_g = tree.add_child(node_c, "G")
node_h = tree.add_child(node_c, "H")

# 木構造の表示
print("木構造を表示します。")  
tree.print_tree(node=tree.root)
