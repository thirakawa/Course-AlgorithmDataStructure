"""graph_unweighted_set.py

-----------------------------------------------------------------------
重みを持たない無向グラフ（Undirected graph）と有向グラフ
（Directed graph）をノード集合とエッジ集合で表現する場合
のサンプルプログラム。

このプログラムでは自分で定義したUndirectedGraphクラスと
DirectedGraphクラスを使用して、グラフのノードとエッジの
追加と削除を行なっています。

MEMO:
グラフのノードは頂点とも呼ばれます。そのため、
英語では Node (Nodes) または Vertex (Vertices) の
名称があり、数式やプログラムでは、変数名として
Vertex の `v` が頻繁に使用されます。
"""


# （重みなし）無向グラフのクラス定義
class UndirectedGraph:
    def __init__(self):
        self.nodes = {}  # 空の集合（辞書オブジェクト）を定義

    # ノードの追加
    def add_node(self, v):
        if v not in self.nodes:
            self.nodes[v] = []

    # エッジの追加（ノードが存在しなければ、ノードも新規追加）
    def add_edge(self, v1, v2):
        self.add_node(v1)
        self.add_node(v2)
        self.nodes[v1].append(v2)  # v1 -> v2 のエッジ追加
        self.nodes[v2].append(v1)  # v2 -> v1 のエッジ追加

    # エッジの削除
    def remove_edge(self, v1, v2):
        if v1 not in self.nodes:
            raise KeyError(f"No such node: {v1}")
        if v2 not in self.nodes:
            raise KeyError(f"No such node: {v2}")

        self.nodes[v1].remove(v2)  # v1 -> v2 のエッジ削除
        self.nodes[v2].remove(v1)  # v2 -> v1 のエッジ削除

    # ノードの削除
    def remove_node(self, v):
        if v not in self.nodes:
            raise KeyError(f"No such node: {v}")

        # つながっている各隣接ノードからエッジを削除
        for target_node in list(self.nodes[v]):
            self.remove_edge(v, target_node)

        # 最後に自身を削除（自分から出るエッジも同時に削除）
        del self.nodes[v]

    # グラフ集合の情報を表示
    def display(self):
        print("Undirected graph *************")
        for v in self.nodes:
            print(v, ":", self.nodes[v])
        print("*" * 30)


# （重みなし）有向グラフのクラス定義
class DirectedGraph:
    def __init__(self):
        self.nodes = {}  # 空の集合（辞書オブジェクト）を定義

    # ノードの追加
    def add_node(self, v):
        if v not in self.nodes:
            self.nodes[v] = []

    # エッジの追加（ノードが存在しなければ、ノードも新規追加）
    def add_edge(self, from_v, to_v):
        self.add_node(from_v)
        self.add_node(to_v)
        self.nodes[from_v].append(to_v)  # from_v -> to_v のエッジ追加

    # エッジの削除
    def remove_edge(self, from_v, to_v):
        if from_v not in self.nodes:
            raise KeyError(f"No such node: {from_v}")
        if to_v not in self.nodes:
            raise KeyError(f"No such node: {to_v}")
        
        # 有向グラフなので、from_v から to_v への一方向のエッジのみ削除
        self.nodes[from_v].remove(to_v)

    # ノードの削除
    def remove_node(self, v):
        if v not in self.nodes:
            raise KeyError(f"No such node: {v}")

        # 自分に入ってくるエッジを削除
        for u in list(self.nodes.keys()):
            if v in self.nodes[u]:
                self.remove_edge(u, v)

        # 最後にノード自体を削除（自分から出るエッジも同時に削除）
        del self.nodes[v]

    # グラフ集合の情報を表示
    def display(self):
        print("Directed graph ***************")
        for v in self.nodes:
            print(v, ":", self.nodes[v])
        print("*" * 30)


# ---------------------------------------------------------------------
# [重みなし無向グラフ] グラフの初期化と構築
print("集合表現で無向グラフ（重みなし）を構築します。")

ug = UndirectedGraph()
ug.add_edge("A", "B")
ug.add_edge("A", "D")
ug.add_edge("B", "C")
ug.add_edge("B", "E")
ug.add_edge("C", "D")
ug.add_edge("C", "F")
ug.add_edge("D", "F")
ug.add_edge("E", "F")

# [重みなし無向グラフ] 構築したグラフの表示
ug.display()

# [重みなし無向グラフ] ノードの削除
print("ノード C を削除します。")
ug.remove_node("C")

# [重みなし無向グラフ] ノード削除後のグラフの表示
ug.display()

# ----------------------------------------------------------------
# [重みなし有向グラフ] グラフの初期化と構築
print("-" * 30)
print("集合表現で有向グラフ（重みなし）を構築します。")

# 使用例
dg = DirectedGraph()
dg.add_edge("A", "B")
dg.add_edge("B", "C")
dg.add_edge("B", "D")
dg.add_edge("C", "A")
dg.add_edge("C", "B")
dg.add_edge("D", "E")
dg.add_edge("E", "C")

# [重みなし有向グラフ] 構築したグラフの表示
dg.display()

# [重みなし有向グラフ] ノードの削除
print("ノード B を削除します。")
dg.remove_node("B")

# [重みなし有向グラフ] ノード削除後のグラフの表示
dg.display()
