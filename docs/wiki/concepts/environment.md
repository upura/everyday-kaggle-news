# 環境構築

コンペ用の計算環境(ローカルマシン・クラウド・エディタ設定)に関する話題のページです。
Kaggle Notebook の制約を超えたいときの選択肢を集めています。

## 押さえどころ

- エディタ(VSCode)の設定を整えるだけでも深層学習の開発体験は大きく変わる
- 選択肢は大きく「自宅 GPU マシンの調達」と「クラウド(GCP・AWS)の利用」。クラウドは Terraform などの IaC でコンペごとに素早く立ち上げる方法がある
- 継続的に参加するなら費用管理も論点になる
- 環境をテンプレート化してコンペ間で使い回す話は[実験管理](./experiment-management.md)を参照

## 資料

- [深層学習モデル実装時のVSCode設定](http://shunk031.hatenablog.com/entry/how-to-setup-vscode-for-developing-deep-learning-model)
- [新しくKaggle用のマシンを調達しました（2020年ver）](https://nonbiri-tereka.hatenablog.com/entry/2020/12/24/223543)
- [深層学習ライブラリと量子化](https://techblog.goinc.jp/entry/2020/09/03/090000)
- [機械学習モデルの開発環境を構築する【ML-Light-02】【AWS Black Belt】](https://youtu.be/C8VYnJ-DF3I)
- [Terraformを使ってGoogleCloud上にKaggle環境をささっと構築する](https://zenn.dev/takayoshi/articles/002-kaggle-iac)
- [Numerai Computeの費用節約](https://www.docswell.com/s/8980249862/K7R8Q1-2025-05-17-142926)

## 関連概念

- [実験管理](./experiment-management.md) / [PyTorch](./pytorch.md)
