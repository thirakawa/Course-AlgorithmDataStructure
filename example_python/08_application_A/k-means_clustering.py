"""k-means_clustering.py

-----------------------------------------------------------------------
k-means法によってデータをk個のクラスタにクラスタリングする
サンプルプログラム。
"""


import random
import math


# 2つのデータのユークリッド距離を計算する関数
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


# k-meansクラスタリングの関数
def k_means(data, k, max_iter=100):
    print("k-means開始 =======================")

    # 初期中心をランダムに選択
    centroids = random.sample(data, k)
    print("  初期化された中心点:", centroids)

    for i in range(max_iter):
        clusters = [[] for _ in range(k)]

        # 各点を最も近い中心へ割り当て
        for point in data:
            distances = [distance(point, c) for c in centroids]
            min_index = distances.index(min(distances))
            clusters[min_index].append(point)

        # 新しい中心を計算
        new_centroids = []
        for cluster in clusters:
            if cluster:  # 空クラスタ対策
                x_mean = sum(p[0] for p in cluster) / len(cluster)
                y_mean = sum(p[1] for p in cluster) / len(cluster)
                new_centroids.append((x_mean, y_mean))
            else:
                new_centroids.append(random.choice(data))

        # 収束判定（セントロイドが変わらなくなるか）
        if new_centroids == centroids:
            break

        # 中心点の更新
        centroids = new_centroids
        print(f"  {i} 回目の中心点:", centroids)

    print("k-means終了 =======================")
    return centroids, clusters


# ---------------------------------------------------------------------
# クラスタリングするデータとクラスタ数 (k) の定義
data = [(1, 2), (2, 1), (1, 1), (8, 8), (9, 8), (8, 9), (5, 5), (6, 5), (5, 6)]
k = 3
print(f"与えられたデータを {k} 個のクラスタに分割します。")

# k-meansクラスタリングの実行
centroids, clusters = k_means(data, k)

# 結果の表示
print("最終的な中心点:", centroids)
print("クラスタ:")
for i, cluster in enumerate(clusters):
    print(f"クラスタ番号 {i}:", cluster)
