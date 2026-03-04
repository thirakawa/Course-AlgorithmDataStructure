"""graph_networkx.py

-----------------------------------------------------------------------
Pythonでグラフ構造を扱うための追加モジュール "networkx" を使
用したグラフ表現のプログラム。

このプログラムでは networkx モジュールを使用して、グラフのデー
タ構造を扱う処理を行います。
networkxでは無向グラフはGraph()、有向グラフはDiGraph()で作成す
ることができます。また、重みはエッジやノードの追加の際に属性値
として追加することができます。

注意：
networkx モジュールは、Python標準の組み込みモジュールではありま
せん。そのため、環境によっては追加のインストールが必要です。

参考リンク：
  API Reference:
    - https://networkx.org/documentation/stable/reference/index.html
  Gallary（さまざまな使用例）:
    - https://networkx.org/documentation/stable/auto_examples/index.html
"""


import networkx as nx


# [重みなし無向グラフ] ------------------------------------------------
print("-" * 30)
print("networkxで無向グラフ（重みなし）を構築します。")

undirected_g = nx.Graph()

# ノード追加
undirected_g.add_node("D")

# エッジ追加
undirected_g.add_edge("A", "B")
undirected_g.add_edge("B", "C")

# 現在のグラフのノードとエッジを表示
print("構築したグラフ構造:")
print("  Nodes:", list(undirected_g.nodes))
print("  Edges:", list(undirected_g.edges))

# ノード削除
undirected_g.remove_node("D")

# 削除後のグラフのノードとエッジを表示
print("ノード削除後:")
print("  Nodes:", list(undirected_g.nodes))
print("  Edges:", list(undirected_g.edges))


# [重みつき無向グラフ] ------------------------------------------------
print("-" * 30)
print("networkxで無向グラフ（重みあり）を構築します。")

undirected_weighted_g = nx.Graph()

# ノード追加
undirected_weighted_g.add_node("D")

undirected_weighted_g.add_edge("A", "B", weight=5)
undirected_weighted_g.add_edge("B", "C", weight=2)

# 現在のグラフのノードとエッジを表示
print("構築したグラフ構造:")
print("  Nodes:", list(undirected_weighted_g.nodes))
print("  Edges:", list(undirected_weighted_g.edges(data=True)))

# ノード削除
undirected_weighted_g.remove_node("D")

# 削除後のグラフのノードとエッジを表示
print("ノード削除後:")
print("  Nodes:", list(undirected_weighted_g.nodes))
print("  Edges:", list(undirected_weighted_g.edges(data=True)))


# [重みなし有向グラフ] ------------------------------------------------
print("-" * 30)
print("networkxで有向グラフ（重みなし）を構築します。")

directed_g = nx.DiGraph()

# ノード追加
directed_g.add_node("D")

directed_g.add_edge("A", "B")
directed_g.add_edge("B", "C")

# 現在のグラフのノードとエッジを表示
print("構築したグラフ構造:")
print("  Nodes:", list(directed_g.nodes))
print("  Edges:", list(directed_g.edges))

# ノード削除
directed_g.remove_node("D")

# 削除後のグラフのノードとエッジを表示
print("ノード削除後:")
print("  Nodes:", list(directed_g.nodes))
print("  Edges:", list(directed_g.edges))


# [重みつき有向グラフ] ------------------------------------------------
print("-" * 30)
print("networkxで有向グラフ（重みあり）を構築します。")

directed_weighted_g = nx.DiGraph()

# ノード追加
directed_weighted_g.add_node("D")

directed_weighted_g.add_edge("A", "B", weight=10)
directed_weighted_g.add_edge("B", "C", weight=3)

# 現在のグラフのノードとエッジを表示
print("構築したグラフ構造:")
print("  Nodes:", list(directed_weighted_g.nodes))
print("  Edges:", list(directed_weighted_g.edges(data=True)))

# ノード削除
directed_weighted_g.remove_node("D")

# 削除後のグラフのノードとエッジを表示
print("ノード削除後:")
print("  Nodes:", list(directed_weighted_g.nodes))
print("  Edges:", list(directed_weighted_g.edges(data=True)))
