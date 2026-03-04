"""graph_weighted_matrix.py

-----------------------------------------------------------------------
重みを持つ無向グラフ（Undirected graph）と有向グラフ
（Directed graph）を隣接行列で表現する場合の
サンプルプログラム。

このプログラムでは自分で定義したUndirectedWeightedGraphMatrix
クラスとDirectedWeightedGraphMatrixクラスを使用して、グラフの
エッジの追加と削除を行なっています。
さらに、エッジに対する重みの情報も保持するように実装して
います。

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


# 重みつき無向グラフのクラス定義
class UndirectedWeightedGraphMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    # エッジの追加（重みの変更）
    def add_edge(self, v1, v2, weight):
        if v1 < 0 or v1 >= self.size:
            raise IndexError("Index out of range")
        if v2 < 0 or v2 >= self.size:
            raise IndexError("Index out of range")

        # 対称行列になるように隣接行列を変更（行列の要素を重みに変更）
        self.matrix[v1][v2] = weight  # v1 -> v2
        self.matrix[v2][v1] = weight  # v2 -> v1

    # エッジの削除
    def remove_edge(self, v1, v2):
        if v1 < 0 or v1 >= self.size:
            raise IndexError("Index out of range")
        if v2 < 0 or v2 >= self.size:
            raise IndexError("Index out of range")

        # 対称行列になるように隣接行列を変更する
        self.matrix[v1][v2] = 0  # v1 -> v2
        self.matrix[v2][v1] = 0  # v2 -> v1

    # グラフの隣接行列を表示
    def display(self):
        print("Adjacency matrix (Undirected) **********")
        for row in self.matrix:
            print(row)
        print("*" * 40)


# 重みつき有向グラフのクラス定義
class DirectedWeightedGraphMatrix:
    def __init__(self, size):
        self.size = size
        self.matrix = [[0] * size for _ in range(size)]

    # エッジの追加（重みの変更）
    def add_edge(self, from_v, to_v, weight):
        if from_v < 0 or from_v >= self.size:
            raise IndexError("Index out of range")
        if to_v < 0 or to_v >= self.size:
            raise IndexError("Index out of range")
        
        self.matrix[from_v][to_v] = weight

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
# [重みつき無向グラフ] 隣接行列の初期化と構築
print("隣接行列で無向グラフ（重みつき）を構築します。")

uwg = UndirectedWeightedGraphMatrix(4)  # ノード数: 4 の隣接行列
uwg.add_edge(0, 1, 3)
uwg.add_edge(0, 2, 5)
uwg.add_edge(0, 3, 9)
uwg.add_edge(1, 2, 7)

# [重みつき無向グラフ] 構築したグラフの表示
uwg.display()

# [重みつき無向グラフ] エッジの削除
print("エッジを削除します。")
uwg.remove_edge(0, 2)

# [重みつき無向グラフ] エッジ削除後のグラフの表示
uwg.display()

# ----------------------------------------------------------------
# [重みつき有向グラフ] 隣接行列の初期化と構築
print("-" * 30)
print("隣接行列で有向グラフ（重みつき）を構築します。")

dg = DirectedWeightedGraphMatrix(4)  # ノード数: 4 の隣接行列
dg.add_edge(0, 1, 6)
dg.add_edge(0, 2, 3)
dg.add_edge(0, 3, 4)
dg.add_edge(2, 0, 5)
dg.add_edge(3, 1, 3)

# [重みつき有向グラフ] 構築したグラフの表示
dg.display()

# [重みつき有向グラフ] エッジの削除
print("エッジを削除します。")
dg.remove_edge(0, 1)

# [重みつき有向グラフ] ノード削除後のグラフの表示
dg.display()

