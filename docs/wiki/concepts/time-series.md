# 時系列予測コンペ

時系列予測のコンペは、金融や需要予測などを題材にします。
未来情報のリークを防ぐバリデーション設計の出来が、スコアの信頼性を左右します。
時期（era）によるレジーム変化への頑健性や、評価指標に合わせた損失関数の設計も特有の論点です。

## 押さえどころ

- 学習と検証の分割は必ず時間で切る。未来の情報が特徴量に混入する形のリークが最頻出の失敗（[性能評価と検証](./evaluation-validation.md)も参照）
- 評価指標（順位相関など）と損失関数のズレは、torchsort などの微分可能なソートを使ってカスタム損失で直接最適化できる（[金融時系列予測における評価指標に応じた損失関数のデザイン](https://zenn.dev/tonic/articles/70cc6c46408aeb)）
- 時期によって特徴量と目的変数の関係が変わる問題には、分割の「方向の一貫性」を最大化する WarpGBM / Directional Era-Splitting のようなアプローチがある
- ゼロショットで使える時系列基盤モデル（Chronos-Bolt など）も選択肢になってきた

## 資料

- [第3会 関東Kaggler会_マーケット予測コンペの問題設計と取り組み方](https://www.docswell.com/s/8980249862/KR2YD1-KantoKaggler3rd_MarketCompetition)
- [Kaggleで学ぶ系列データのための深層学習モデリング](https://speakerdeck.com/yu4u/kaggletexue-huxi-lie-tetanotamenoshen-ceng-xue-xi-moterinku): 系列データを扱ったコンペと上位解法から深層学習モデリングを俯瞰する資料。
- [異なる時系列間でもGBDTの予測結果をロバストに 〜WarpGBMとDirectional Era-Splitting〜](https://zenn.dev/nishimoto/articles/ee40c5f9edda7c): 時期をまたいで安定するシグナルを学習する決定木の分割基準を、Numerai データでの実験付きで解説。
- [金融時系列予測における評価指標に応じた損失関数のデザイン](https://zenn.dev/tonic/articles/70cc6c46408aeb): torchsort を使い順位相関係数を直接最適化するカスタム損失の実装を紹介。
- [時系列基盤モデルChronos-Boltでお手軽に時系列予測を試してみた](https://acro-engineer.hatenablog.com/entry/2025/02/18/120000): AWS の時系列基盤モデルを AutoGluon 経由でゼロショット推論・fine-tuning する実例。
- [パラメータ4個で710M超えのFoundation Modelに勝った時系列予測手法FLAIRの全貌](https://zenn.dev/t_honda/articles/flair-time-series-forecasting): 少パラメータで基盤モデルを上回る性能を報告する時系列予測手法の解説記事。
- [時系列基盤モデルの現在(2025/12)](https://qiita.com/pigooosuke/items/1ee44c088e3db6c3c801): 時系列基盤モデルの研究動向を、検証論文も含めて整理したサーベイ記事。
- [実践Data Scienceシリーズ Pythonではじめる時系列分析入門](https://www.amazon.co.jp/dp/4065369827): 古典的手法から新しい手法までを実践的に解説する書籍。
- [時系列データのための大規模言語モデル](https://zenn.dev/tsurubee/articles/00446669b6c83a): サーベイ論文をもとに時系列データへの LLM 活用の手法分類を紹介する記事。
- [Google Colabで時系列基盤モデルを試す①：Google timesfm](https://note.com/hatti8/n/n734aca9d4afb): 商用可能ライセンスの時系列基盤モデル 4 つを試す記事。
- [Prophetによる時系列データ予測: Analyst-in-the-Loop](https://zenn.dev/aidemy/articles/3587a5c0d4c210): 株価データを題材にした Prophet による分析の流れの紹介。
- [Polarsで始める時系列データ処理 #atmaCup 19 振り返り会 LT枠](https://speakerdeck.com/koheiiwamasa/polarsdeshi-merushi-xi-lie-detachu-li-number-atmacup-19-zhen-rifan-rihui-ltwaku)

## 関連概念

- [表データコンペ](./tabular.md) / [性能評価と検証](./evaluation-validation.md)
