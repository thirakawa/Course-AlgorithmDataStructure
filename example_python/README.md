# アルゴリズムとデータ構造: Python プログラム

このディレクトリには、講義で扱うアルゴリズムとデータ構造の Python 実装が含まれています。


## 概要

`example_python` には次のディレクトリがあり、それぞれ次のような項目のプログラムが含まれています。

**01_basic_alg_flow**

- 順次構造 (Sequential structure)
- 選択構造 (Selection structure)
- 反復構造 (Repeating structure)

**02_data_struct_A**

- 配列
- リスト（連結リスト）
- スタック
- キュー
- ハッシュテーブル

**03_data_struct_B**

- グラフ（無向・有向・重みなし・重みつき）
- 木構造
- 二分木
- 二分探索木
- 木構造版（最大・最小）ヒープ
- 配列版（最大・最小）ヒープ

**04_search**

- 線形探索
- 二分探索
- ハッシュ探索
- 幅優先探索
- 深さ優先探索

**05_sort**

- 選択ソート
- 挿入ソート
- バブルソート
- マージソート
- クイックソート
- 木構造版ヒープソート
- 配列版ヒープソート
- 計数ソート（バケットソート・ビンソート）
- 基数ソート

**06_str_matching**

- 素朴な文字列パターン照合
- KMP (Knuth–Morris–Pratt) 法
- BM (Boyer-Moore) 法

**07_recursive_alg**

- 再帰処理による階乗計算
- ハノイの塔

**08_application**

- エラトステネスのふるい
- ユークリッドの互助法
- k-meansクラスタリング


## Python 環境のセットアップ

このリポジトリに含まれるPythonプログラムを実行するために必要な環境設定について記述します。

1. **仮想環境の作成**（`venv` を使用）:

    ここでは、環境構築の一例として `venv` を使用します。
    OSによってコマンドが異なるため、自身のOSに合わせて設定してください。

    **A. Mac / Linux の場合**

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

    **B. Windows の場合**

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

2. **依存関係のインストール**

    プログラムの実行に必要な追加パッケージをインストールします。

    ```bash
    pip install -r requirements.txt
    ```

以上で、環境構築は完了です。

## Pythonプログラムの実行方法

実行したいプログラムがあるサブフォルダ（例: `03_basic_alg_flow`）に移動し、Python ファイルを実行します。
以下では、`example_python/03_basic_alg_flow/01_sequential_struct.py`を実行する場合の例を示します。

```bash
cd 03_basic_alg_flow
python 01_sequential_struct.py
```
