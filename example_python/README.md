# Python 環境のセットアップ

このディレクトリには、講義で扱うアルゴリズムとデータ構造の Python 実装が含まれています。

## Python環境の構築

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
