# PyTorch

PyTorch は Kaggle の深層学習コンペにおける実装のデファクトスタンダードです。
基礎はチュートリアルで押さえ、学習と推論の高速化テクニックで実験の回転を上げます。

## 押さえどころ

- 基礎は公式チュートリアル（日本語翻訳版あり）を一巡するのが近道
- 学習と推論の高速化（DataLoader 設定や AMP など）は、実験回数に直結するため早めに習慣化する
- 事前学習済みモデルの活用は[画像認識コンペ](./image-recognition.md)、Transformer 系の fine-tuning は[自然言語処理コンペ](./nlp-llm.md)を参照

## 資料

- [PyTorchチュートリアル（日本語翻訳版）](https://yutaroogawa.github.io/pytorch_tutorials_jp/)
- [PyTorchで高精度・高性能のEfficientNetを利用する](https://nonbiri-tereka.hatenablog.com/entry/2020/03/26/083557)
- [PyTorchでの学習・推論を高速化するコツ集](https://qiita.com/sugulu_Ogawa_ISID/items/62f5f7adee083d96a587)
- [TransformersでoptimizerのMuonを使う](https://zenn.dev/colum2131/scraps/5971d43e710718): コンペ上位解法でも使われる Optimizer「Muon」の使い方の紹介。
- [明日使えるかもしれないLoss Functionsのアイディアと実装](https://speakerdeck.com/ftakahashi/ming-ri-shi-erukamosirenailoss-functionsnoaideiatoshi-zhuang): 回帰・分類の特徴的な損失関数を PyTorch 実装つきで解説する資料。
- [深層ニューラルネットワークの高速化](https://www.amazon.co.jp/dp/4297143097): 量子化・枝刈り・蒸留・モデルマージなどの高速化手法と理論を解説する書籍。
- [モデルパラメータの算術](https://joisino.hatenablog.com/entry/2024/01/09/174517): 重みの平均（Model soups）など深層学習モデルの重みの算術の解説記事。
- [モデルの気持ちになって情報を与えよう](https://medium.com/@junkoda/%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E6%B0%97%E6%8C%81%E3%81%A1%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%A6%E6%83%85%E5%A0%B1%E3%82%92%E4%B8%8E%E3%81%88%E3%82%88%E3%81%86-4fd575d03fb1): モデルに「情報を与える」観点でコンペ解法を読み解く Grandmaster の記事。

## 関連概念

- [画像認識コンペ](./image-recognition.md) / [自然言語処理コンペ](./nlp-llm.md) / [環境構築](./environment.md)
