# PyTorch

PyTorch は Kaggle の深層学習コンペにおける実装のデファクトスタンダードです。
基礎はチュートリアルで押さえ、学習と推論の高速化テクニックで実験の回転を上げます。

## 押さえどころ

- 基礎は公式チュートリアル（日本語翻訳版あり）を一巡するのが近道
- 学習と推論の高速化（DataLoader 設定や AMP など）は、実験回数に直結するため早めに習慣化する
- 事前学習済みモデルの活用は[画像認識コンペ](./image-recognition.md)、Transformer 系の fine-tuning は[自然言語処理コンペ](./nlp-llm.md)を参照

## 資料

- [PyTorchチュートリアル（日本語翻訳版）](https://yutaroogawa.github.io/pytorch_tutorials_jp/)
- [PyTorch 2.0: Our next generation release](https://pytorch.org/blog/pytorch-2.0-release/): torch.compile を導入した PyTorch 2.0 の公式リリース告知。
- [JAX/Flaxで学ぶディープラーニングの仕組み](https://book.mynavi.jp/ec/products/detail/id=135373): JAX/Flax で CNN の実装を中心に解説する書籍。
- [PyTorchで高精度・高性能のEfficientNetを利用する](https://nonbiri-tereka.hatenablog.com/entry/2020/03/26/083557)
- [PyTorchでの学習・推論を高速化するコツ集](https://qiita.com/sugulu_Ogawa_ISID/items/62f5f7adee083d96a587)
- [TransformersでoptimizerのMuonを使う](https://zenn.dev/colum2131/scraps/5971d43e710718): コンペ上位解法でも使われる Optimizer「Muon」の使い方の紹介。
- [明日使えるかもしれないLoss Functionsのアイディアと実装](https://speakerdeck.com/ftakahashi/ming-ri-shi-erukamosirenailoss-functionsnoaideiatoshi-zhuang): 回帰・分類の特徴的な損失関数を PyTorch 実装つきで解説する資料。
- [深層ニューラルネットワークの高速化](https://www.amazon.co.jp/dp/4297143097): 量子化・枝刈り・蒸留・モデルマージなどの高速化手法と理論を解説する書籍。
- [モデルパラメータの算術](https://joisino.hatenablog.com/entry/2024/01/09/174517): 重みの平均（Model soups）など深層学習モデルの重みの算術の解説記事。
- [モデルの気持ちになって情報を与えよう](https://medium.com/@junkoda/%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E6%B0%97%E6%8C%81%E3%81%A1%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%A6%E6%83%85%E5%A0%B1%E3%82%92%E4%B8%8E%E3%81%88%E3%82%88%E3%81%86-4fd575d03fb1): モデルに「情報を与える」観点でコンペ解法を読み解く Grandmaster の記事。
- [Introducing Keras 3.0](https://keras.io/keras_3/): JAX・TensorFlow・PyTorch をバックエンドに使える Keras 3.0 の公開告知。
- [ニューラルネットワークの量子化手法の紹介](https://speakerdeck.com/emakryo/niyurarunetutowakunoliang-zi-hua-shou-fa-noshao-jie): モデル圧縮と高速化のための量子化手法の紹介資料。
- [深層モデルの高速化](https://speakerdeck.com/joisino/shen-ceng-moderunogao-su-hua): 推論時間制限のあるコンペにも役立つ深層学習高速化のサーベイ資料。
- [DeepSpeed: 深層学習の訓練と推論を劇的に高速化するフレームワーク](https://www.deepspeed.ai/assets/files/DeepSpeed_Overview_Japanese_2023Jun7th.pdf): Microsoft 製の高速化フレームワークの日本語解説資料。
- [高速な深層学習モデルアーキテクチャ2023](https://speakerdeck.com/yu4u/gao-su-nashen-ceng-xue-xi-moteruakitekutiya2023): 蒸留・量子化からアーキテクチャ別まで扱う高速化の調査資料。
- [AdamWにおける改善点をきちんと理解する](https://zenn.dev/bilzard/articles/adamw-demistified): Adam からの変更点を中心に AdamW の論文を解説する記事。
- [モデルの出力ではなく重みを混ぜ合わせるアンサンブル手法の論文](https://arxiv.org/abs/2203.05482): 推論時のモデルが 1 つで済む利点を持つ手法の提案論文。
- [PyTorch 1.11 リリース](https://pytorch.org/blog/pytorch-1.11-released/): TorchData・functorch などの新機能が追加。
- [PyTorchのDataLoaderクラスの高速化を解説する記事](https://zenn.dev/xiongjie/articles/0ae1378feb4204): 処理の概要を紐解きながら高速化の勘所を紹介。
- [TensorFlowとPyTorchを2022年時点で比較する記事](https://atmarkit.itmedia.co.jp/ait/articles/2201/16/news013.html): Google製の JAX への言及も含む比較記事。
- [PyTorch Lightning の紹介資料](https://speakerdeck.com/yongtae723/pytorch-lightningfalsesusume): コード記述を簡略化する PyTorch Lightning の紹介。同内容のブログ記事も公開。
- [PyTorchとJAXの速度比較記事](https://www.mattari-benkyo-note.com/2021/11/17/ssw-jax-vs-torch/): PyTorch 高速化の技法としても参考になる検証記事。
- [PyTorch 1.10 リリース](https://pytorch.org/blog/pytorch-1.10-new-library-releases/): 過学習抑制のための Label Smoothing などの機能を追加。
- [PyTorchで頻出のコードをまとめた記事](https://qiita.com/takubb/items/7d45ae701390912c7629): 乱数固定・データ準備・学習・評価などの定型コード集。
- [PyTorchのコードをJAXに書き換える方法の紹介記事](https://zenn.dev/jellied_unagi/articles/d986044a425e94): 実行時間の比較も掲載する書き換えガイド。
- [回帰問題でのDropout利用に関する検証記事](https://st1990.hatenablog.com/entry/2021/07/31/155511): 「Dropout と BatchNorm を併用しない方が良い」という話題を検証した記事。

## 関連概念

- [画像認識コンペ](./image-recognition.md) / [自然言語処理コンペ](./nlp-llm.md) / [環境構築](./environment.md)
