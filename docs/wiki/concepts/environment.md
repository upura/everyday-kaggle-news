# 環境構築

コンペ用の計算環境（ローカルマシン、クラウド、エディタ設定）に関する話題のページです。
Kaggle Notebook の制約を超えたいときの選択肢を集めています。

## 押さえどころ

- エディタ（VSCode）の設定を整えるだけでも深層学習の開発体験は大きく変わる
- 選択肢は大きく「自宅 GPU マシンの調達」と「クラウド（GCP や AWS）の利用」。クラウドは Terraform などの IaC でコンペごとに素早く立ち上げる方法がある
- 継続的に参加するなら費用管理も論点になる
- 環境をテンプレート化してコンペ間で使い回す話は[実験管理](./experiment-management.md)を参照

## 資料

- [深層学習モデル実装時のVSCode設定](http://shunk031.hatenablog.com/entry/how-to-setup-vscode-for-developing-deep-learning-model)
- [新しくKaggle用のマシンを調達しました（2020年ver）](https://nonbiri-tereka.hatenablog.com/entry/2020/12/24/223543)
- [Kagglerの自作PC入門！](https://qiita.com/Isaka-code/items/85c573d9320df9b97c48): Kaggle 用途を想定した自作 PC の入門記事。
- [深層学習ライブラリと量子化](https://techblog.goinc.jp/entry/2020/09/03/090000)
- [機械学習モデルの開発環境を構築する【ML-Light-02】【AWS Black Belt】](https://youtu.be/C8VYnJ-DF3I)
- [Terraformを使ってGoogleCloud上にKaggle環境をささっと構築する](https://zenn.dev/takayoshi/articles/002-kaggle-iac)
- [貸してください、RunPod を Kaggle でこう使うのはどうですか](https://zenn.dev/takeru1205/articles/e50bea5d3441ec): GPU クラウド「RunPod」を Kaggle 用途で使いやすくするライブラリの紹介。
- [Agentic Coding時代のデータ分析コンペの環境構築](https://yag.xyz/post/data_competition_setup/): AI エージェント前提のコンペ用ディレクトリ構成と取り組み方の紹介。
- [Google Colab is Coming to VS Code](https://developers.googleblog.com/en/google-colab-is-coming-to-vs-code/): VS Code から Colab の GPU を使える公式拡張の発表。
- [Create a Remote LLM Server Using Kaggle Notebooks and Ollama](https://medium.com/data-science-collective/create-a-remote-llm-server-using-kaggle-notebooks-and-ollama-acb299ead1e5): Kaggle の計算環境で LLM 推論サーバを立てる方法のコード付き解説。
- [Kaggle の Notebook 環境を VS Code (Cursor) で触りたい](https://zenn.dev/prgckwb/articles/kaggle-vscode-link): 手元の IDE から Kaggle Notebook 環境に接続する実験的機能の紹介。
- [Numerai Computeの費用節約](https://www.docswell.com/s/8980249862/K7R8Q1-2025-05-17-142926)

## 関連概念

- [実験管理](./experiment-management.md) / [PyTorch](./pytorch.md)
