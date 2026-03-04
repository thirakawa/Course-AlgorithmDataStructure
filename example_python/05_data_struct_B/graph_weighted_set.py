"""graph_weighted_set.py

-----------------------------------------------------------------------
重みを持つ無向グラフ（Undirected graph）と有向グラフ
（Directed graph）をノード集合とエッジ集合で表現する場合
のサンプルプログラム。

このプログラムでは自分で定義したUndirectedWeightedGraph
クラスとDirectedWeightedGraphクラスを使用して、グラフの
ノードとエッジの追加と削除を行なっています。
さらに、エッジに対する重みの情報も保持するように実装して
います。

MEMO:
グラフのノードは頂点とも呼ばれます。そのため、
英語では Node (Nodes) または Vertex (Vertices) の
名称があり、数式やプログラムでは、変数名として
Vertex の `v` が頻繁に使用されます。
"""


# 重みつき無向グラフのクラス定義
class UndirectedWeightedGraph:
    def __init__(self):
        self.nodes = {}  # 空の集合（辞書オブジェクト）を定義

    # ノードの追加
    def add_node(self, v):
        if v not in self.nodes:
            self.nodes[v] = []

    # エッジの追加（ノードが存在しなければ、ノードも新規追加）
    def add_edge(self, v1, v2, weight):
        self.add_node(v1)
        self.add_node(v2)
        self.nodes[v1].append((v2, weight))  # v1 -> v2 のエッジの追加（接続先のノードと重みのタプル）
        self.nodes[v2].append((v1, weight))  # v2 -> v1 のエッジの追加（接続先のノードと重みのタプル）

    # エッジの削除
    def remove_edge(self, v1, v2):
        if v1 not in self.nodes:
            raise KeyError(f"No such node: {v1}")
        if v2 not in self.nodes:
            raise KeyError(f"No such node: {v2}")
        
        # 削除対象のエッジ以外を残すことでエッジを削除
        self.nodes[v1] = [(w, wt) for (w, wt) in self.nodes[v1] if w != v2]  # v1 -> v2 のエッジ削除
        self.nodes[v2] = [(w, wt) for (w, wt) in self.nodes[v2] if w != v1]  # v2 -> v1 のエッジ削除

    # ノードの削除
    def remove_node(self, v):
        if v not in self.nodes:
            raise KeyError(f"No such node: {v}")

        # つながっている各隣接ノードからエッジを削除
        for target_node, _ in list(self.nodes[v]):
            self.remove_edge(v, target_node)

        # 自身のノードを削除（自分から出るエッジも同時に削除）
        del self.nodes[v]

    # グラフ集合の情報を表示
    def display(self):
        print("Weighted undirected graph **************")
        for v in self.nodes:
            print(v, ":", self.nodes[v])
        print("*" * 40)


# 重みつき有向グラフのクラス定義
class DirectedWeightedGraph:
    def __init__(self):
        self.nodes = {}  # 空の集合（辞書オブジェクト）を定義

   # ノードの追加
    def add_node(self, v):
        if v not in self.nodes:
            self.nodes[v] = []

    # エッジの追加（ノードが存在しなければ、ノードも新規追加）
    def add_edge(self, from_v, to_v, weight):
        self.add_node(from_v)
        self.add_node(to_v)
        self.nodes[from_v].append((to_v, weight))  # from_v -> to_v のエッジの追加

    # エッジの削除
    def remove_edge(self, from_v, to_v):
        if from_v not in self.nodes:
            raise KeyError(f"No such node: {from_v}")
        if to_v not in self.nodes:
            raise KeyError(f"No such node: {to_v}")
        
        # 有向グラフなので、from_v から to_v への一方向のエッジのみ削除
        # （削除対象のエッジ以外を残すことでエッジを削除）
        self.nodes[from_v] = [(w, wt) for (w, wt) in self.nodes[from_v] if w != to_v]
    
    # ノードの削除
    def remove_node(self, v):
        if v not in self.nodes:
            raise KeyError(f"No such node: {v}")
        
        # 自分に入ってくるエッジも削除
        for u in list(self.nodes.keys()):
            for target_node, _ in self.nodes[u]:
                if target_node == v:
                    self.remove_edge(u, v)

        # 最後にノード自体を削除（自分から出るエッジも同時に削除）
        del self.nodes[v]

    # グラフ集合の情報を表示
    def display(self):
        print("Weighted directed graph ***************")
        for v in self.nodes:
            print(v, ":", self.nodes[v])
        print("*" * 40)


# ---------------------------------------------------------------------
# [重みつき無向グラフ] グラフの初期化と構築
print("集合表現で無向グラフ（重みあり）を構築します。")

uwg = UndirectedWeightedGraph()
uwg.add_edge("A", "B", 3)
uwg.add_edge("A", "D", 5)
uwg.add_edge("B", "C", 4)
uwg.add_edge("B", "E", 9)
uwg.add_edge("C", "D", 8)
uwg.add_edge("C", "F", 1)
uwg.add_edge("D", "F", 6)
uwg.add_edge("E", "F", 2)

# [重みつき無向グラフ] 構築したグラフの表示
uwg.display()

# [重みつき無向グラフ] ノードの削除
print("ノード C を削除します。")
uwg.remove_node("C")

# [重みつき無向グラフ] ノード削除後のグラフの表示
uwg.display()

# ----------------------------------------------------------------
# [重みつき有向グラフ] グラフの初期化と構築
print("-" * 30)
print("集合表現で有向グラフ（重みあり）を構築します。")

dwg = DirectedWeightedGraph()
dwg.add_edge("A", "B", 5)
dwg.add_edge("B", "C", 3)
dwg.add_edge("B", "D", 7)
dwg.add_edge("C", "A", 2)
dwg.add_edge("C", "B", 1)
dwg.add_edge("D", "E", 4)
dwg.add_edge("E", "C", 8)

# [重みつき有向グラフ] 構築したグラフの表示
dwg.display()

# [重みつき有向グラフ] ノードの削除
print("ノード B を削除します。")
dwg.remove_node("B")

# [重みつき有向グラフ] ノード削除後のグラフの表示
dwg.display()
