"""graph_unweighted_matrix.py

-----------------------------------------------------------------------
重みを持たない無向グラフ（Undirected graph）と有向グラフ
（Directed graph）を隣接行列で表現する場合の
サンプルプログラム。

このプログラムでは自分で定義したUndirectedGraphMatrixクラスと
DirectedGraphMatrixクラスを使用して、グラフのエッジの追加と削
除を行なっています。

注意：
隣接行列を使用したグラフ表現では、後からノード追加を行うことは
少なく、最初に定義したノード数でデータを処理することが一般的で
す。これは、ノードの追加や削除の処理を隣接行列で行おうとすると、
計算コストが高くなるためです。このプログラムでは、この慣例に従っ
てノードの追加や削除の処理は扱わず、接続関係を表現する処理を行
なっています。

MEMO:
グラフのノードは頂点とも呼ばれます。そのため、
英語では Node (Nodes) または Vertex (Vertices) の
名称があり、数式やプログラムでは、変数名として
Vertex の `v` が頻繁に使用されます。
"""


# （重みなし）無向グラフのクラス定義
class UndirectedGraphMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    # エッジの追加
    def add_edge(self, v1, v2):
        if v1 < 0 or v1 >= self.size:
            raise IndexError("Index out of range")
        if v2 < 0 or v2 >= self.size:
            raise IndexError("Index out of range")
        
        # 対称行列になるように隣接行列を変更
        self.matrix[v1][v2] = 1  # v1 -> v2
        self.matrix[v2][v1] = 1  # v2 -> v1

    # エッジの削除
    def remove_edge(self, v1, v2):
        if v1 < 0 or v1 >= self.size:
            raise IndexError("Index out of range")
        if v2 < 0 or v2 >= self.size:
            raise IndexError("Index out of range")

        # 対称行列になるように隣接行列を変更
        self.matrix[v1][v2] = 0  # v1 -> v2
        self.matrix[v2][v1] = 0  # v2 -> v1

    # グラフの隣接行列を表示
    def display(self):
        print("Adjacency matrix (Undirected) **********")
        for row in self.matrix:
            print(row)
        print("*" * 40)


# （重みなし）有向グラフのクラス定義
class DirectedGraphMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    # エッジの追加
    def add_edge(self, from_v, to_v):
        if from_v < 0 or from_v >= self.size:
            raise IndexError("Index out of range")
        if to_v < 0 or to_v >= self.size:
            raise IndexError("Index out of range")
        
        self.matrix[from_v][to_v] = 1

    # エッジの削除
    def remove_edge(self, from_v, to_v):
        if from_v < 0 or from_v >= self.size:
            raise IndexError("Index out of range")
        if to_v < 0 or to_v >= self.size:
            raise IndexError("Index out of range")
        
        self.matrix[from_v][to_v] = 0

    # グラフの隣接行列を表示
    def display(self):
        print("Adjacency matrix (Directed) ************")
        for row in self.matrix:
            print(row)
        print("*" * 40)


# ---------------------------------------------------------------------
# [重みなし無向グラフ] 隣接行列の初期化と構築
print("隣接行列で無向グラフ（重みなし）を構築します。")

ug = UndirectedGraphMatrix(4)  # ノード数: 4 の隣接行列
ug.add_edge(0, 1)
ug.add_edge(0, 2)
ug.add_edge(0, 3)
ug.add_edge(1, 2)

# [重みなし無向グラフ] 構築したグラフの表示
ug.display()

# [重みなし無向グラフ] エッジの削除
print("エッジを削除します。")
ug.remove_edge(0, 2)

# [重みなし無向グラフ] エッジ削除後のグラフの表示
ug.display()

# ----------------------------------------------------------------
# [重みなし有向グラフ] 隣接行列の初期化と構築
print("-" * 30)
print("隣接行列で有向グラフ（重みなし）を構築します。")

dg = DirectedGraphMatrix(4)  # ノード数: 4 の隣接行列
dg.add_edge(0, 1)
dg.add_edge(0, 2)
dg.add_edge(0, 3)
dg.add_edge(2, 0)
dg.add_edge(3, 1)

# [重みなし有向グラフ] 構築したグラフの表示
dg.display()

# [重みなし有向グラフ] エッジの削除
print("エッジを削除します。")
dg.remove_edge(0, 1)

# [重みなし有向グラフ] ノード削除後のグラフの表示
dg.display()
