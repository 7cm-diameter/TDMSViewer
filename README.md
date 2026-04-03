# TDMSViewer
`tdms` ファイルを GUI 上で表示し、閾値検出などの処理を行うツールです。

## Install

このプロジェクトは Python パッケージマネージャー `uv` で管理されています。  
依存関係のインストールや実行には `uv` を使用してください。

まず、各自の環境に `uv` をインストールしてください。  
インストール方法は公式ドキュメントを参照してください。  
https://docs.astral.sh/uv/

### `uv`インストール後
ターミナル上で以下のコマンドを実行します。
```
git clone <repository-url> TDMSViewer
cd TDMSViewer
```

ターミナル上で`uv sync`を実行して依存関係をインストールします。
問題なくインストールできたら、`uv run tdms-viewer`を実行すると、GUIが立ち上がります。
