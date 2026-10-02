# 入門者・初学者向け

Kaggle の概要、初心者が最初に取り組むべきこと、定番の学習資料をまとめています。

## Kaggle とは

Kaggle は、機械学習モデルの性能を競い合うデータサイエンスコンペティションのプラットフォームです。
企業や研究機関が提供する実データと課題に対し、世界中の参加者が予測精度を競います。
プラットフォーム側でユーザ管理、順位表、スコア計算の基盤が提供されているため、主催者は比較的手軽にコンペを開催でき、参加者も多くのコンペに挑戦しやすい利点があります。
データ分析の普及に伴い認知度が高まり、登録ユーザ数は 2000 万人を超えています。

## コンペはいつ開催されているか

Kaggle では常に複数のコンペが開催されています。
[Kaggle 公式のコンペ一覧](https://www.kaggle.com/competitions)で確認できるほか、有志による X（旧 Twitter）の bot も活用できます。

- [Kagoole](https://x.com/kagoole): 新着コンペを通知します。
- [data-compe-alerts](https://x.com/DataCompeAlerts): 開催中のコンペの開催期間を毎日投稿します。

各コンペには、メダルやランキングポイントの付与対象かどうかが設定されています。
付与対象のコンペほど多くの参加者が集まる傾向があります。

## 実行環境

Kaggle では、ブラウザ上で Python や R を実行できる Code（Notebook）環境が提供されています。
主要な機械学習ライブラリがあらかじめ導入されており、必要に応じてライブラリを追加することも可能です。
週あたりの利用時間制限はあるものの、GPU や TPU も無料で利用できます。

## 押さえておきたい前提知識

Kaggle に参加するにあたって、次の知識があるとスムーズに進められます。
国際人工知能オリンピック（IOAI）では、参加者に期待する知識を理論と実践に分けてシラバス（[日本語訳版](https://ioai-japan.org/ioai2025-syllabus/)）に整理しています。

- 機械学習（特に教師あり学習）の基礎理論
- Python によるデータ処理とモデル実装
- Kaggle プラットフォームの操作方法

すべてを事前に網羅する必要はありません。最低限の基本を押さえたら、実際のコンペへの参加を通じて不足した知識を補っていく進め方が適しています。

## 最初に見るべきページ

- 「[最新情報の確認](./recent.md)」から、開催中や開催予定のコンペを探せます。
- その他の話題は[目次](../README.md)から探せます。

## 定番資料

Titanic などのチュートリアルコンペを終えたあと、実践的なコンペへどう進むかが次の段階です。
以下の定番資料で、その後の進め方をつかめます。
体系的に学びたい場合は「[書籍](./books.md)」、継続するための考え方は「[心構え](./wiki/concepts/mindset.md)」を参照してください。

- [Kaggleに登録したら次にやること ～ これだけやれば十分闘える！Titanicの先へ行く入門 10 Kernel ～](https://qiita.com/upura/items/3c10ff6fed4e7c3d70f0): タイタニックコンペを終えた初心者が次に挑戦すべき公開コードやコンペを紹介する記事。
- [Kaggle入門動画をつくった](https://yutori-datascience.hatenablog.com/entry/2017/10/24/215647): Kaggle の基礎知識とチュートリアルへの取り組み方を解説する入門動画の紹介。
- [【2位入賞】ずんだもんとめたんで学ぶKaggle 入門 & 参戦記 Part 1【Petfinderコンペ】](https://www.youtube.com/watch?v=Ug5uce0kbtQ&list=PLkBjLQIGEjJl9icR4WdHkn29OJrrHE3sn): 初心者向けに入門手順とコンペ参加の流れを解説する動画シリーズ。
- [Kaggle Learn](https://www.kaggle.com/learn): 公式の学習コンテンツ。基礎を短時間で確認できます。
- [機械学習初心者がKaggleの「入門」を高速で終えるための、おすすめ資料などまとめ（2026年7月版）](https://note.com/currypurin/n/na800851cb884): 『Kaggleのチュートリアル第7版』の著者による入門資料まとめ。
- [Kaggleのハードルを下げたい！](https://qiita.com/Isaka-code/items/3935cdb2a0bda331e07c): 初心者が参加への心理的ハードルを下げるための考え方と基礎知識をまとめた記事。
- [kaggleハンズオン](https://www.docswell.com/s/marbou090/V5GMD5-2021-04-19-132114): テーブルデータのコンペを題材に、提出までの一連の作業を体験できるスライド教材。
- [Kaggleコンペの始め方](https://aitc.dentsusoken.com/column/column19/): 初期の取り組み方や計算機環境を解説する入門記事。
- [Kaggle役立ちアイテム紹介（入門編）](https://speakerdeck.com/k951286/kaggleyi-li-tiaitemushao-jie-ru-men-bian): 環境構築、学習、モデルのカテゴリ別に便利なサービスやツールを紹介する資料。
- [機械学習帳](https://chokkan.github.io/mlnote/): 機械学習の理論と Python 実装を学べる、東京工業大学情報理工学院の講義資料。
- [Python早見帳](https://chokkan.github.io/python/): 基礎的な文法から NumPy や Matplotlib まで扱う、プログラムと実行結果をセットにした学習教材。
- [リクルートのKaggle Master 4人による初学者向け解説記事](https://www.atmarkit.co.jp/ait/articles/2105/12/news010.html): 概要や具体的な取り組み方をまとめた入門記事。
- [Kaggle Learn新講座「AIに関する倫理」公開](https://www.kaggle.com/learn/intro-to-ai-ethics): 機械学習モデルのバイアスや公平性を扱う入門教材。
- [Kaggle入門Tips記事（Housing Prices Competitionを題材に）](https://towardsdatascience.com/how-to-get-started-on-kaggle-competitions-68b91e3e803a?gi=5501692f63e6): データ理解からモデルの学習と検証までの流れを解説。
- [Kaggle「Computer Vision」学習コース設置](https://www.kaggle.com/learn/computer-vision): 事前学習済みモデルを用いた画像分類モデルの作成方法を学ぶコース。
- [fast.aiによる深層学習入門動画（Jeremy Howard講師）](https://www.freecodecamp.org/news/learn-deep-learning-from-the-president-of-kaggle/): 元 Kaggle 社長が講師を務める入門動画。
- [Yann LeCun教授によるディープラーニング講義資料一式](https://medium.com/@NYUDataScience/yann-lecuns-deep-learning-course-at-cds-is-now-fully-online-accessible-to-all-787ddc8bf0af): スライド、講義動画、PyTorch 実装の Notebook を公開。
- [「Papers with Code」とarXivの提携](https://medium.com/paperswithcode/papers-with-code-partners-with-arxiv-ecc362883167): arXiv 論文ページにコードタブが新設。
- [DeNAのKagglerとコンペで学ぶデータサイエンス実践講座](https://dena.ai/news/202010-ds-challenge-season2/): テーマごとにコンペと解法を議論する構成の社内講座。
- [「機械学習：TensorFlowでゼロからヒーローへ」動画シリーズ](https://blog.tensorflow.org/2020/08/introducing-tensorflow-videos-japanese.html): 概要説明から「じゃんけん識別器」実装までを扱う 4 部構成の動画。
- [Kaggle「データクレンジング」講座](https://www.kaggle.com/learn/data-cleaning): 欠損値処理、スケーリング、日付や文字列の処理を扱う入門講座。

## 話題別の学び方ガイド

興味のあるデータ種別やコンペ形式が決まったら、対応する概念ページの「押さえどころ」と「入門・基礎」の資料から読み始めるのがおすすめです。各概念ページにその話題の定跡、技術動向、資料一覧が集約されています。コンペ形式そのものの歴史的な流れは「[コンペ形式・技術動向の変遷](./wiki/concepts/competition-evolution.md)」を参照してください。

- **表データ**: [表データコンペ](./wiki/concepts/tabular.md)。まずは [The Kaggle Grandmasters Playbook](https://developer.nvidia.com/blog/the-kaggle-grandmasters-playbook-7-battle-tested-modeling-techniques-for-tabular-data/) で定跡の全体像をつかむのがおすすめ
- **画像認識**: [画像認識コンペ](./wiki/concepts/image-recognition.md)。まずは [画像コンペことはじめ](https://zenn.dev/dalab/articles/41b1a0c3b3d410) から
- **自然言語処理・LLM**: [自然言語処理コンペ](./wiki/concepts/nlp-llm.md)。まずは [大規模言語モデル (LLM) 入門](https://speakerdeck.com/rist/da-gui-mo-yan-yu-moderu-llm-ru-men) から
- **時系列予測**: [時系列予測コンペ](./wiki/concepts/time-series.md)。時間分割バリデーションの原則を最初に押さえる
- **音声**: [音声コンペ](./wiki/concepts/audio.md)。まずは [ESPnet による音声認識入門 ～ESPnet Model Zoo 編～](https://note.com/retrieva/n/nd04d38377f1b) から
- **グラフ**: [グラフ](./wiki/concepts/graph.md)。まずは [グラフ道場](https://yuya-s.github.io/GraphDojo/) の演習から
- **推薦**: [推薦](./wiki/concepts/recommendation.md)。まずは [レコメンドアルゴリズム入門](https://qiita.com/birdwatcher/items/b60822bdf9be267e1328) から
- **数理最適化**: [数理最適化コンペ](./wiki/concepts/optimization.md)。AtCoder（特に AHC）の経験がそのまま活きる
- **エージェント対戦**: [エージェント対戦コンペ](./wiki/concepts/agent-competition.md)。まずは [誰でもわかる強化学習](https://speakerdeck.com/imai_eruel/reinforcement-learning-for-everyone) から

データ種別によらず共通する土台（[実験管理](./wiki/concepts/experiment-management.md)、[環境構築](./wiki/concepts/environment.md)、[性能評価と検証](./wiki/concepts/evaluation-validation.md)）や、コード提出の制約（[コードコンペティション](./wiki/concepts/code-competition.md)）は、どのコンペに取り組む場合でも事前に確認しておくと役立ちます。学び続けるための心構えは「[心構え](./wiki/concepts/mindset.md)」を参照してください。
