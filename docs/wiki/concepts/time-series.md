# 時系列予測コンペ

時系列予測のコンペは、金融や需要予測などを題材にします。
未来情報のリークを防ぐバリデーション設計の出来が、スコアの信頼性を左右します。
時期(era)によるレジーム変化への頑健性や、評価指標に合わせた損失関数の設計も特有の論点です。

## 押さえどころ

- 学習と検証の分割は必ず時間で切る。未来の情報が特徴量に混入する形のリークが最頻出の失敗([性能評価と検証](./evaluation-validation.md)も参照)
- 評価指標(順位相関など)と損失関数のズレは、torchsort などの微分可能なソートを使ってカスタム損失で直接最適化できる([金融時系列予測における評価指標に応じた損失関数のデザイン](https://zenn.dev/tonic/articles/70cc6c46408aeb))
- 時期によって特徴量と目的変数の関係が変わる問題には、分割の「方向の一貫性」を最大化する WarpGBM / Directional Era-Splitting のようなアプローチがある
- ゼロショットで使える時系列基盤モデル(Chronos-Bolt など)も選択肢になってきた

## 資料

- [第3会 関東Kaggler会_マーケット予測コンペの問題設計と取り組み方](https://www.docswell.com/s/8980249862/KR2YD1-KantoKaggler3rd_MarketCompetition)
- [異なる時系列間でもGBDTの予測結果をロバストに 〜WarpGBMとDirectional Era-Splitting〜](https://zenn.dev/nishimoto/articles/ee40c5f9edda7c): 時期をまたいで安定するシグナルを学習する決定木の分割基準を、Numerai データでの実験付きで解説。
- [金融時系列予測における評価指標に応じた損失関数のデザイン](https://zenn.dev/tonic/articles/70cc6c46408aeb): torchsort を使い順位相関係数を直接最適化するカスタム損失の実装を紹介。
- [時系列基盤モデルChronos-Boltでお手軽に時系列予測を試してみた](https://acro-engineer.hatenablog.com/entry/2025/02/18/120000): AWS の時系列基盤モデルを AutoGluon 経由でゼロショット推論・fine-tuning する実例。
- [Polarsで始める時系列データ処理 #atmaCup 19 振り返り会 LT枠](https://speakerdeck.com/koheiiwamasa/polarsdeshi-merushi-xi-lie-detachu-li-number-atmacup-19-zhen-rifan-rihui-ltwaku)

## 関連概念

- [表データコンペ](./tabular.md) / [性能評価と検証](./evaluation-validation.md)
