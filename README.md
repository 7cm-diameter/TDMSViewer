# TDMSViewer
`tdms` ファイルを GUI 上で表示し、閾値検出などの処理を行うツールです。

## Install

このプロジェクトは Python パッケージマネージャー `uv` で管理されています。  
依存関係のインストールや実行には `uv` を使用してください。

まず、各自の環境に `uv` をインストールしてください。  
インストール方法は[公式ドキュメント](https://docs.astral.sh/uv/)を参照してください。  

もしも`git`が各自の環境になければ、あらかじめインストールしてください。
インストール方法は[公式ドキュメント](https://git-scm.com/install/linux)を参照してください。

### `uv`と`git`のインストール後

ターミナル上で以下のコマンドを実行します。
```
git clone https://github.com/7cm-diameter/TDMSViewer TDMSViewer
cd TDMSViewer
```

ターミナル上で`uv sync`を実行して依存関係をインストールします。
問題なくインストールできたら、`uv run tdms-viewer`を実行すると、GUIが立ち上がります。
