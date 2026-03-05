"""depth_first_search.py

-----------------------------------------------------------------------
深さ優先探索（Depth-First Search; DFS）のサンプルプログラム。

このプログラムでは木構造のデータを使用して深さ優先探索を
実行しています。

注意1：
このプログラムでは tree_structure.py のプログラムを再掲
して使用しています。
木構造については 03_data_struct_B/tree_structure.py を
参照してください。
"""


# 木構造の単一ノードのクラス定義（03_data_struct_B/tree_structure.py）
class TreeNode:
    def __init__(self, value):
        # ノードの持つ値（名前や数値など）
        self.value = value
        # 子ノードのリスト
        self.children = []

    # 小ノードの追加
    def add_child(self, child_node):
        self.children.append(child_node)


# 木構造全体を管理するクラス定義（03_data_struct_B/tree_structure.py）
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


# 幅優先探索（全てのノードを探索）
def dfs_entire_tree(node):
    print(node.value, end=" ")

    # 再帰呼び出し
    for child in node.children:
        dfs_entire_tree(child)


# 幅優先探索（指定ノードを探索）
def dfs_target(node, target):
    print("調べているノード:", node.value)

    # 見つかった場合
    if node.value == target:
        print("見つかりました")
        return node

    # 再起呼び出し
    for child in node.children:
        result = dfs_target(child, target)
        if result is not None:
            return result

    # 見つからなかった場合
    print("葉ノード：見つかりませんでした")
    return None


# ---------------------------------------------------------------------
# 木構造の初期化（根ノードのみ作成）
print("木構造を構築します。")
tree = Tree(root_value="A")

# 子ノードの追加
print("ノードを追加します。")  
node_b = tree.add_child(tree.root, "B")
node_c = tree.add_child(tree.root, "C")
node_d = tree.add_child(tree.root, "D")
node_e = tree.add_child(node_b, "E")
node_f = tree.add_child(node_b, "F")
node_h = tree.add_child(node_c, "H")
node_i = tree.add_child(node_d, "I")
node_j = tree.add_child(node_d, "J")
node_k = tree.add_child(node_e, "K")
node_g = tree.add_child(node_h, "G")
node_l = tree.add_child(node_j, "L")

# 木構造の表示
print("木構造を表示します。")  
tree.print_tree(node=tree.root)

# ---------------------------------------------------------------------
# 深さ優先探索で全てのノードを探索
print("-" * 30)
print("深さ優先探索で全てのノードを順番に探索します。")
dfs_entire_tree(tree.root)

# ---------------------------------------------------------------------
# 深さ優先探索で指定したノードを探索
print("-" * 30)
target = "I"
print(f"深さ優先探索でノード {target} を探索します。")
node_found = dfs_target(tree.root, target)
