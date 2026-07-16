# 環境構築

コンペ用の計算環境（ローカルマシン、クラウド、エディタ設定）に関する話題のページです。
Kaggle Notebook の制約を超えたいときの選択肢を集めています。

## 押さえどころ

- 大きな選択肢は「自宅 GPU マシンの調達」「クラウド（GCP・AWS・RunPod など）の利用」「Google Colaboratory・Kaggle Notebook などの無料/定額枠」の3系統。継続的に参加するなら費用対効果と管理コストが論点になる
- クラウドは Terraform などの IaC でコンペごとに環境を素早く立ち上げる運用が定着してきた
- Google Colaboratory は Pro/Pro+ やコンピューティングユニット制、TPU 提供などで機能を拡張し続ける一方、Python バージョンや利用規約の変更が度々発生するため追随が必要
- Kaggle Notebook 自体も GPU 環境や信頼性の改善が継続的に行われており、VS Code・Cursor などローカル IDE から接続して使う選択肢も増えている
- パッケージ管理は rye・Poetry などのツールや Docker を用いたコンペ環境の再現性確保に関心が向かっている。NumPy 2.0 のようなメジャーアップデートでは既存コードとの互換性に注意が必要
- エディタ（VS Code）の設定を整えるだけでも深層学習の開発体験は大きく変わる。SSH 接続でのバックグラウンド実行など、長時間の学習を止めずに作業する工夫も定番
- 環境をテンプレート化してコンペ間で使い回す話は[実験管理](./experiment-management.md)を参照

## 資料

### エディタ・IDE連携（VS Code・Cursor）

- [深層学習モデル実装時のVSCode設定](http://shunk031.hatenablog.com/entry/how-to-setup-vscode-for-developing-deep-learning-model)
- [Google Colab is Coming to VS Code](https://developers.googleblog.com/en/google-colab-is-coming-to-vs-code/): VS Code から Colab の GPU を使える公式拡張の発表。
- [Kaggle の Notebook 環境を VS Code (Cursor) で触りたい](https://zenn.dev/prgckwb/articles/kaggle-vscode-link): 手元の IDE から Kaggle Notebook 環境に接続する実験的機能の紹介。
- [SSH接続＋VSCodeでのJupyterカーネルのバックグラウンド実行 for Kaggler](https://qiita.com/shu421/items/9c58aefe97087756bc39): 長時間の学習処理を止めずに実行する方法の紹介。
- [VS CodeにTensorBoard連携機能が実装](https://devblogs.microsoft.com/python/python-in-visual-studio-code-february-2021-release/): タブ上で TensorBoard を起動できる新機能。
- [Visual Studio CodeでJupyter Notebookを使う拡張機能公開](https://forest.watch.impress.co.jp/docs/news/1289446.html): Python 以外の言語でも利用可能な拡張機能。
- [Google Colab・Kaggle NotebookでVSCodeを起動するライブラリ「colabcode」](https://github.com/abhishekkrthakur/colabcode): より手軽に実行できるようになったツール。チュートリアル動画も公開。

### ローカル・オンプレ環境

- [新しくKaggle用のマシンを調達しました（2020年ver）](https://nonbiri-tereka.hatenablog.com/entry/2020/12/24/223543)
- [Kagglerの自作PC入門！](https://qiita.com/Isaka-code/items/85c573d9320df9b97c48): Kaggle 用途を想定した自作 PC の入門記事。
- [Which GPU(s) to Get for Deep Learning](https://timdettmers.com/2023/01/30/which-gpu-for-deep-learning/): 深層学習用 GPU を性能・費用の観点で比較する定番記事。
- [PC構築初心者による Kaggle 用 オンプレ GPU マシン組み立て事始め](https://kaeru-nantoka.hatenablog.com/entry/2022/12/04/165444)
- [コンペ用GPU付きマシンの購入体験記](https://fam-taro.hatenablog.com/entry/2020/12/17/235648): 検討背景・手順・購入後の所感を語る記事。

### クラウド環境（GCP・AWS・RunPod）

- [機械学習モデルの開発環境を構築する【ML-Light-02】【AWS Black Belt】](https://youtu.be/C8VYnJ-DF3I)
- [Terraformを使ってGoogleCloud上にKaggle環境をささっと構築する](https://zenn.dev/takayoshi/articles/002-kaggle-iac)
- [貸してください、RunPod を Kaggle でこう使うのはどうですか](https://zenn.dev/takeru1205/articles/e50bea5d3441ec): GPU クラウド「RunPod」を Kaggle 用途で使いやすくするライブラリの紹介。
- [GCP A100GPU-VMでKaggle-Docker環境を構築（2023年3月版）](https://qiita.com/calpis10000/items/fb18b8d6a1e021a6f755): GCP インスタンスに Kaggle Docker 環境を組む手順の記事。
- [大規模AIクラウド計算システム「ABCI」の利用Tipsまとめ](https://speakerdeck.com/yoshipon/fastest-deep-learning-on-abci): アーキテクチャ・ライブラリ・プロファイラの観点で紹介する資料。
- [Amazon SageMaker Studio Lab検証記事（Google Colaboratoryとの比較）](https://atmarkit.itmedia.co.jp/ait/articles/2112/20/news035.html): ブラウザ上の Python 実行環境の比較検証。
- [Amazon SageMaker Studio Lab発表（AWS公式）](https://aws.amazon.com/blogs/aws/now-in-preview-amazon-sagemaker-studio-lab-a-free-service-to-learn-and-experiment-with-ml/): CPU で 12 時間、GPU で 4 時間利用できる無料の機械学習実行環境。
- [「KagglerのためのBigQuery活用手法」登壇資料](https://cloudonair.withgoogle.com/events/ml-summit): Kaggle Master tkm2261 さんによる BigQuery 活用手法の紹介資料。
- [AWS「Amazon EC2 DL1インスタンス」一般提供開始](https://press.aboutamazon.com/news-releases/news-release-details/aws-announces-general-availability-amazon-ec2-dl1-instances): 汎用 GPU と比較し価格効率が 40% 優れる学習特化インスタンスの発表。
- [AWS re:Invent「SageMaker Feature Store」発表](https://dev.classmethod.jp/articles/breaking-sagemaker-feature-store/): SageMaker Data Wrangler・Pipelines なども合わせて発表。
- [GitHub・AWSを用いたKaggle提出自動化の取り組み](https://tepppei.hatenablog.com/entry/2020/07/19/120625): 学習・予測・提出を自動化する一連の流れの紹介。
- [GCP「AIプラットフォーム」機能の解説記事](https://qiita.com/hiromu166/items/507fc0fb466c7149dccf): 手軽に JupyterLab の実行環境を構築する方法を紹介。

### Google Colaboratory・TPU

- [Two New Ways to Manage Cell Execution](https://medium.com/google-colab/two-new-ways-to-manage-cell-execution-fbad61b40882): Google Colab のセル実行に関する 2 つの新機能の紹介。
- [Local runtimes（Colaboratory公式ドキュメント）](https://research.google.com/colaboratory/local-runtimes.html): 任意の端末で Colab 相当の環境を作れる公式 Docker イメージの案内。
- [colab.google](https://colab.google/): Google Colab の更新情報がまとまる公式ページ。
- [Colab Updated to Python 3.9](https://medium.com/google-colab/colab-updated-to-python-3-9-2593f8b1eb79): Google Colab の Python バージョン更新の公式告知。
- [Colab Updated to Python 3.8](https://medium.com/google-colab/colab-updated-to-python-3-8-4922f9970a72)
- [Colaboratory にコンピューティングユニットが登場](https://research.google.com/colaboratory/intl/ja/faq.html): 利用可能な計算資源を可視化・追加購入できる機能の公式 FAQ。
- [Numerai Computeの費用節約](https://www.docswell.com/s/8980249862/K7R8Q1-2025-05-17-142926)
- [Google Colaboratoryの使い方入門資料](https://speakerdeck.com/imash/googlecolaboratoryfalseshi-ifang-ru-men-2022nian-du-hiuyi-teng-zemi): ブラウザ上の Python 実行環境の基本的な使い方を説明する資料。
- [Google Colab Pro+にスケジュール実行機能が追加](https://github.com/googlecolab/colabtools/wiki/Scheduled-notebooks): 公式リリースノートによる新機能の紹介。
- [TPUについてKaggleの観点からまとめた記事](https://zenn.dev/koukyo1994/articles/53b828f5a3ae1c): 概要や使い方、注意点や対策をコードと共に紹介。
- [Google Colaboratory課金版の日本解禁告知](https://twitter.com/GoogleColab/status/1374769408397041664?s=20): FAQ も合わせて更新。
- [Google Colaboratory利用規約の更新（日本の支払い情報追加）](https://colab.research.google.com/pro/terms): Pro の利用可能国拡大への布石となる更新。
- [Kaggle公式によるTPU解説動画（Phil Culliton）](https://www.youtube.com/watch?v=BSeWHzjMHMU&feature=youtu.be): Kaggle 上での TPU 利用 Tips を紹介する動画。
- [Google Colaboratoryの便利なTips紹介記事](https://amitness.com/2020/06/google-colaboratory-tips/): TensorFlow バージョン切り替えなどあまり知られていない機能を紹介。

### Kaggle Notebook環境

- [Create a Remote LLM Server Using Kaggle Notebooks and Ollama](https://medium.com/data-science-collective/create-a-remote-llm-server-using-kaggle-notebooks-and-ollama-acb299ead1e5): Kaggle の計算環境で LLM 推論サーバを立てる方法のコード付き解説。
- [kaggle小技まとめてみた(随時更新予定)](https://note.com/chumajin/n/nfafe926a69cf): Kaggle Notebook 環境の便利機能のまとめ。
- [KaggleデータセットをGoogle Colaboratoryにダウンロードするスクリプト](https://tic-memo.netlify.app/posts/kaggle-download-data/): Kaggle Notebook と同様のフォルダ構造で配置。
- [KaggleのGPU環境の舞台裏記事（NVIDIA）](https://news.developer.nvidia.com/how-kaggle-makes-gpus-accessible-to-5-million-data-scientists/): 2 週間ごとの Docker image 更新など、ユーザ体験向上の取り組みを紹介。
- [KaggleのProduct ManagerによるNotebooks環境パフォーマンス改善報告](https://mrisdal.github.io/blog/posts/improved-kaggle-notebooks-reliability/): 改修の背景とユーザ評価向上について言及。
- [pathlib.PathをKaggle Notebooks環境で使う記事](https://tawara.hatenablog.com/entry/2020/05/06/154651): ディレクトリ・ファイル操作の使い方をまとめた記事。

### 開発ツール・パッケージ管理

- [深層学習ライブラリと量子化](https://techblog.goinc.jp/entry/2020/09/03/090000)
- [Agentic Coding時代のデータ分析コンペの環境構築](https://yag.xyz/post/data_competition_setup/): AI エージェント前提のコンペ用ディレクトリ構成と取り組み方の紹介。
- [NumPy 2.0⁠⁠、6/16にリリース](https://gihyo.jp/article/2024/05/numpy-2.0): 2006 年以来のメジャー更新となる NumPy 2.0 の紹介記事。
- [Dockerで構築する機械学習環境【2024年版】](https://zenn.dev/mkj/articles/33befbaf38c693): Docker による機械学習環境構築の利点と使い方の解説記事。
- [ryeでKaggleとほぼ同じML開発環境を構築してみた](https://zenn.dev/kohecchi/articles/4413e41b462d43): パッケージ管理ツール rye で Kaggle 相当の環境を組む手順の紹介。
- [Poetry × JupyterLabで機械学習環境を整える](https://zenn.dev/colum2131/scraps/1bf61d61a7993e): JupyterLab の環境構築と Jupyter AI の試用記録。
- [Google Colaboratory/Kaggle Notebookが生産性を高める](https://gihyo.jp/article/2022/12/increase-productivity-of-r-04): R 言語での Colab・Kaggle Notebook 活用法の解説記事。
- [Anaconda Notebooks / Anaconda Learning の紹介](https://www.anaconda.com/blog/introducing-python-training-and-cloud-hosted-notebooks-from-anaconda): クラウド Notebook と学習コンテンツの新サービス発表。
- [Python 3.11 の新機能](https://www.python.jp/news/wnpython311/index.html): 高速化などの新機能をまとめた記事。
- [NVIDIA「cuNumeric」発表](https://developer.nvidia.com/blog/nvidia-announces-availability-for-cunumeric-public-alpha/): GPU で動作する NumPy 互換ライブラリの公式発表。
- [JupyterLabデスクトップアプリ公開](https://blog.jupyter.org/jupyterlab-desktop-app-now-available-b8b661b17e9a?gi=40aa9008009f): macOS・Windows など複数プラットフォームに対応。
- [JupyterLab v3.0公開](https://blog.jupyter.org/jupyterlab-3-0-is-out-4f58385e25bb?gi=1ee614935786): デバッグツールやドキュメント目次生成機能を追加。
- [Pythonの型アノテーション機能まとめ記事](https://qiita.com/nicco_mirai/items/c1810ed2a6fc8c53c006): 利用可能バージョンを明示して機能を紹介。
- [RStudio v1.4でPython利用が可能に](https://blog.rstudio.com/2020/10/07/rstudio-v1-4-preview-python-support/): インタラクティブな実行と可視化結果の確認に対応。
- [Netflix製Notebook環境「Polynote」の紹介記事](https://medium.com/dataseries/netflixs-polynote-is-a-new-open-source-framework-to-build-better-data-science-notebooks-4bdab6b8d0ae): Jupyter Notebook にはない高度なコーディング補助機能を紹介。
- [Dockerを用いたPython環境構築のTips記事](https://nykergoto.hatenablog.jp/entry/2020/07/25/%E6%A9%9F%E6%A2%B0%E5%AD%A6%E7%BF%92%E3%81%AAdockerfile%E3%82%92%E6%9B%B8%E3%81%8F%E3%81%A8%E3%81%8D%E3%81%AB%E6%B0%97%E3%82%92%E3%81%A4%E3%81%91%E3%81%A8%E3%81%8F%E3%81%A8%E8%89%AF%E3%81%84%E3%81%93): キャッシュの意図的な削除とビルド時テストを推奨。
- [「Memory Error」への対処法をまとめた記事](http://nonbiri-tereka.hatenablog.com/entry/2020/03/17/080457): 具体的な Python コードとともに複数の Tips を紹介。

## 関連概念

- [実験管理](./experiment-management.md) / [PyTorch](./pytorch.md) / [サービス・ツール](../../service.md)
