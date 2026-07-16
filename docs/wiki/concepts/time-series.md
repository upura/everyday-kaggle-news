# 時系列予測コンペ

時系列予測のコンペは、金融や需要予測などを題材にします。
未来情報のリークを防ぐバリデーション設計の出来が、スコアの信頼性を左右します。
時期（era）によるレジーム変化への頑健性や、評価指標に合わせた損失関数の設計も特有の論点です。

## 押さえどころ

- 学習と検証の分割は必ず時間で切る。未来の情報が特徴量に混入する形のリークが最頻出の失敗（[性能評価と検証](./evaluation-validation.md)も参照）
- 交差検証の設計に唯一解はなく、Combinatorial Purged Cross-Validation など複数の手法が今も Kaggler の間で議論され続けている（[時系列データの検証用データセット構築方法を議論する記事](https://zenn.dev/ymd/articles/fd08fb46bc868c)）
- 評価指標（順位相関など）と損失関数のズレは、torchsort などの微分可能なソートを使ってカスタム損失で直接最適化できる（[金融時系列予測における評価指標に応じた損失関数のデザイン](https://zenn.dev/tonic/articles/70cc6c46408aeb)）
- 時期によって特徴量と目的変数の関係が変わる問題には、分割の「方向の一貫性」を最大化する WarpGBM / Directional Era-Splitting のようなアプローチがある
- 2020〜21 年頃は Darts・PyTorch Forecasting・Prophet などライブラリの使い方紹介が中心だったが、2024〜25 年にはゼロショットで使える時系列基盤モデル（Chronos-Bolt、TimesFM など）が主要な話題になっている。少パラメータのモデルが大規模基盤モデルの性能を上回る報告もあり、基盤モデルへの過信には注意が必要（[パラメータ4個で710M超えのFoundation Modelに勝った時系列予測手法FLAIRの全貌](https://zenn.dev/t_honda/articles/flair-time-series-forecasting)）
- Transformer の時系列予測への有効性は、賛否両論の論文が繰り返し引用される決着していない論点

## 資料

### ライブラリ・ツール

- [「PyTorch Forecasting」の紹介記事](https://towardsdatascience.com/introducing-pytorch-forecasting-64de99b9ef46?gi=7393708a2fb): 最先端の時系列モデルを手軽に利用できるライブラリの紹介。
- [時系列予測に使えるPythonライブラリまとめ記事](http://zakopilo.hatenablog.jp/entry/2020/07/19/173851): Prophet・PyFlux・Pyro・PyTorch・LightGBM の使い方を紹介。
- [Prophetによる時系列データ予測: Analyst-in-the-Loop](https://zenn.dev/aidemy/articles/3587a5c0d4c210): 株価データを題材にした Prophet による分析の流れの紹介。
- [最先端時系列データ分析モデルETSformerを使ってみた](https://qiita.com/Isaka-code/items/848589fc4d7dd153e915): Salesforce 製の時系列モデル ETSformer の紹介記事。

### 時系列基盤モデル・LLM活用

- [時系列基盤モデルChronos-Boltでお手軽に時系列予測を試してみた](https://acro-engineer.hatenablog.com/entry/2025/02/18/120000): AWS の時系列基盤モデルを AutoGluon 経由でゼロショット推論・fine-tuning する実例。
- [パラメータ4個で710M超えのFoundation Modelに勝った時系列予測手法FLAIRの全貌](https://zenn.dev/t_honda/articles/flair-time-series-forecasting): 少パラメータで基盤モデルを上回る性能を報告する時系列予測手法の解説記事。
- [時系列基盤モデルの現在(2025/12)](https://qiita.com/pigooosuke/items/1ee44c088e3db6c3c801): 時系列基盤モデルの研究動向を、検証論文も含めて整理したサーベイ記事。
- [時系列データのための大規模言語モデル](https://zenn.dev/tsurubee/articles/00446669b6c83a): サーベイ論文をもとに時系列データへの LLM 活用の手法分類を紹介する記事。
- [Google Colabで時系列基盤モデルを試す①：Google timesfm](https://note.com/hatti8/n/n734aca9d4afb): 商用可能ライセンスの時系列基盤モデル 4 つを試す記事。
- [Informer: Beyond Efficient Transformer for Long Sequence Time-Series Forecasting 解説記事](https://cookie-box.hatenablog.com/entry/2021/02/11/195822): 時系列データの長期予測手法を関連研究・背景付きで紹介。

### 検証設計・評価指標

- [異なる時系列間でもGBDTの予測結果をロバストに 〜WarpGBMとDirectional Era-Splitting〜](https://zenn.dev/nishimoto/articles/ee40c5f9edda7c): 時期をまたいで安定するシグナルを学習する決定木の分割基準を、Numerai データでの実験付きで解説。
- [金融時系列予測における評価指標に応じた損失関数のデザイン](https://zenn.dev/tonic/articles/70cc6c46408aeb): torchsort を使い順位相関係数を直接最適化するカスタム損失の実装を紹介。
- [KaggleDays_Paris_2022（CPMPさんの発表資料）](https://github.com/jfpuget/KaggleDays_Paris_2022): 時系列予測での交差検証に関する発表資料。
- [Numeraiで学ぶ金融時系列モデル評価指標](https://zenn.dev/katsu1110/articles/c1269aec88ee05): 金融時系列の評価指標の特徴と Python 実装例の紹介。
- [時系列データに関する性能検証の方法を議論する記事](https://note.com/currypurin/n/n7bd3153a7238): 多くの Kaggler の意見を取りまとめた議論記事。
- [時系列データの検証用データセット構築方法を議論する記事](https://zenn.dev/ymd/articles/fd08fb46bc868c): Combinatorial Purged Cross-Validation などの手法を紹介。
- [TimeSeriesSplitをカラム指定でソートするコードの公開](https://blog.amedama.jp/entry/time-series-cv): 痒いところに手が届く改良を紹介する記事。

### Transformer・深層学習モデリング

- [Kaggleで学ぶ系列データのための深層学習モデリング](https://speakerdeck.com/yu4u/kaggletexue-huxi-lie-tetanotamenoshen-ceng-xue-xi-moterinku): 系列データを扱ったコンペと上位解法から深層学習モデリングを俯瞰する資料。
- [時系列予測にTransformerを使うのは有効か？](https://www.slideshare.net/ssuser369dbc/transformer-261229829): 賛否両論の論文を題材に Transformer の時系列予測への有効性を解説する資料。
- [Transformerを用いた時系列予測の記事](https://blog.brainpad.co.jp/entry/2021/02/17/140000): 製品購入量の予測タスクを題材にした概要説明と実装。

### 実務・前処理・書籍

- [第3会 関東Kaggler会_マーケット予測コンペの問題設計と取り組み方](https://www.docswell.com/s/8980249862/KR2YD1-KantoKaggler3rd_MarketCompetition)
- [実践Data Scienceシリーズ Pythonではじめる時系列分析入門](https://www.amazon.co.jp/dp/4065369827): 古典的手法から新しい手法までを実践的に解説する書籍。
- [LinkedInが開発した時系列モデル“Greykite”の理論と実装](https://www.pagumi-bayesian.com/2022/11/17/greykite/)
- [時系列データの前処理まとめ](https://www.eureka-moments-blog.com/entry/2022/09/13/221213): 『機械学習のための「前処理」入門』を参考にした前処理手法のまとめ。
- [Polarsで始める時系列データ処理 #atmaCup 19 振り返り会 LT枠](https://speakerdeck.com/koheiiwamasa/polarsdeshi-merushi-xi-lie-detachu-li-number-atmacup-19-zhen-rifan-rihui-ltwaku)
- [機械学習を用いた株価予測に役立つ日本語情報のリンク集](https://note.com/regonn314/n/n4d2b3edb62be): Kaggle「Jane Street Market Prediction」など頻出テーマの情報源をまとめた記事。
- [時系列データからの特徴抽出の考え方・ツール紹介記事（DataRobot）](https://blog.datarobot.com/jp/use_manufacturing_sensor_data_for_machine_learning): 転職した Kaggle Grandmaster の Senkin さんも登場する記事。

## 関連概念

- [表データコンペ](./tabular.md) / [性能評価と検証](./evaluation-validation.md)
