# flake8-bugbear sample

本リポジトリは flake8 の拡張機能である[flake8-bugbear](https://github.com/PyCQA/flake8-bugbear)のサンプルコード確認用リポジトリです。
以下の手順でサンプルを確認可能ですが、コードのみであれば公式リポジトリにサンプルコードがありますのでそちらを参考にしたほうが良いかと思います。

https://github.com/PyCQA/flake8-bugbear/tree/master/tests

## 環境詳細

- Python: 3.9.6
- flake8: 3.9.2
- flake8-bugbear: 21.4.3

### 事前準備

- Docker インストール
- VS Code インストール
- VS Code の拡張機能「Remote - Containers」インストール
  - https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
- 本リポジトリの clone

### 開発手順

1. VS Code 起動
2. 左下の緑色のアイコンクリック
3. 「Remote-Containersa: Reopen in Container」クリック
4. しばらく待つ
   - 初回の場合コンテナー image の取得や作成が行われる
5. 起動したら確認可能
