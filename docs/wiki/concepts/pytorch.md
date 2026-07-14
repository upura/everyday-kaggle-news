# PyTorch

PyTorch は Kaggle の深層学習コンペにおける実装のデファクトスタンダードです。
基礎はチュートリアルで押さえ、学習と推論の高速化テクニックで実験の回転を上げます。

## 押さえどころ

- 基礎は公式チュートリアル（日本語翻訳版あり）を一巡するのが近道
- 学習と推論の高速化（DataLoader 設定や AMP など）は、実験回数に直結するため早めに習慣化する
- 事前学習済みモデルの活用は[画像認識コンペ](./image-recognition.md)、Transformer 系の fine-tuning は[自然言語処理コンペ](./nlp-llm.md)を参照

## 資料

### 基礎・チュートリアル・書籍

- [PyTorchチュートリアル（日本語翻訳版）](https://yutaroogawa.github.io/pytorch_tutorials_jp/)
- [JAX/Flaxで学ぶディープラーニングの仕組み](https://book.mynavi.jp/ec/products/detail/id=135373): JAX/Flax で CNN の実装を中心に解説する書籍。
- [PyTorchで高精度・高性能のEfficientNetを利用する](https://nonbiri-tereka.hatenablog.com/entry/2020/03/26/083557)
- [深層ニューラルネットワークの高速化](https://www.amazon.co.jp/dp/4297143097): 量子化・枝刈り・蒸留・モデルマージなどの高速化手法と理論を解説する書籍。
- [TensorFlowとPyTorchを2022年時点で比較する記事](https://atmarkit.itmedia.co.jp/ait/articles/2201/16/news013.html): Google製の JAX への言及も含む比較記事。
- [PyTorchで頻出のコードをまとめた記事](https://qiita.com/takubb/items/7d45ae701390912c7629): 乱数固定・データ準備・学習・評価などの定型コード集。
- [PyTorchのコードをJAXに書き換える方法の紹介記事](https://zenn.dev/jellied_unagi/articles/d986044a425e94): 実行時間の比較も掲載する書き換えガイド。
- [Microsoft「Learn PyTorch Fundamentals」入門講座](https://medium.com/pytorch/learn-pytorch-fundamentals-with-microsoft-learn-abe663cce194): 画像認識・自然言語処理・音声分類を題材に Jupyter Notebook を実行できる講座。
- [Kaggle GrandmasterのDieterさんによるPyTorch Lightning活用登壇](https://www.youtube.com/watch?v=0HQCK_l-njI&feature=youtu.be): 開催中のコンペへの挑戦や初学者向けアドバイスも紹介。
- [『Deep Learning with PyTorch』日本語翻訳版出版](https://www.amazon.co.jp/PyTorch%E5%AE%9F%E8%B7%B5%E5%85%A5%E9%96%80-Eli-Stevens/dp/4839974691): PyTorch の基礎から実践までを扱う 3 部構成の書籍。
- [ディープラーニングの動向を6つの観点でまとめた動画](https://www.youtube.com/watch?v=MSmGddXGqBg&feature=youtu.be): モデルの End-to-end 化・大規模化・汎用化などを図解で紹介。

### 高速化・最適化テクニック

- [PyTorchでの学習・推論を高速化するコツ集](https://qiita.com/sugulu_Ogawa_ISID/items/62f5f7adee083d96a587)
- [ニューラルネットワークの量子化手法の紹介](https://speakerdeck.com/emakryo/niyurarunetutowakunoliang-zi-hua-shou-fa-noshao-jie): モデル圧縮と高速化のための量子化手法の紹介資料。
- [深層モデルの高速化](https://speakerdeck.com/joisino/shen-ceng-moderunogao-su-hua): 推論時間制限のあるコンペにも役立つ深層学習高速化のサーベイ資料。
- [DeepSpeed: 深層学習の訓練と推論を劇的に高速化するフレームワーク](https://www.deepspeed.ai/assets/files/DeepSpeed_Overview_Japanese_2023Jun7th.pdf): Microsoft 製の高速化フレームワークの日本語解説資料。
- [高速な深層学習モデルアーキテクチャ2023](https://speakerdeck.com/yu4u/gao-su-nashen-ceng-xue-xi-moteruakitekutiya2023): 蒸留・量子化からアーキテクチャ別まで扱う高速化の調査資料。
- [PyTorchのDataLoaderクラスの高速化を解説する記事](https://zenn.dev/xiongjie/articles/0ae1378feb4204): 処理の概要を紐解きながら高速化の勘所を紹介。
- [PyTorchとJAXの速度比較記事](https://www.mattari-benkyo-note.com/2021/11/17/ssw-jax-vs-torch/): PyTorch 高速化の技法としても参考になる検証記事。
- [PyTorch学習高速化ライブラリ「torch_ort.ORTModule」公開](https://cloudblogs.microsoft.com/opensource/2021/07/13/accelerate-pytorch-training-with-torch-ort/): 言語モデルのファインチューニングが 1.2〜1.3 倍程度高速化。
- [深層学習の効率化に関するブログ記事（Google研究者、第3弾）](https://www.kdnuggets.com/2021/07/high-performance-deep-learning-part3.html): 同著者によるサーベイ論文も公開。
- [複数GPUでのモデル学習手法比較記事（DP vs DDP）](https://qiita.com/fam_taro/items/df6061b589c3ccf86089): Distributed Data Parallel を推奨する検証記事。
- [深層学習の学習効率化に関する網羅的サーベイ論文](https://arxiv.org/abs/2106.08962): モデリングだけでなくインフラ・ハードウェアの話題も扱う論文。
- [PyTorch公式「Performance Tuning Guide」の検証記事](https://www.mattari-benkyo-note.com/2021/04/27/pytorch-performance-tuning-guide-1-parameter-grad-none/): `parameter.grad = None` の効果などを検証する連載第 1 弾。
- [NVIDIA GTC 2021のPyTorch関連セッションまとめ記事](https://medium.com/pytorch/nvidia-gtc-2021-hosts-over-50-pytorch-sessions-4312e9e8f3ee): 「PyTorch Performance Tuning Guide」など多数のセッションを紹介。
- [PyTorchで大規模データセットを扱う「WebDataset」の紹介記事](https://cyberagent.ai/blog/research/14632/): TensorFlow の TFRecord に相当する仕組みの紹介。
- [PyTorchでGPUの計算時間を計測する方法の紹介記事](https://www.mattari-benkyo-note.com/2021/03/21/pytorch-cuda-time-measurement/): 単純な time() 使用時の問題点も指摘。
- [PyTorch Profilerの紹介記事（v1.8.1）](https://pytorch.org/blog/introducing-pytorch-profiler-the-new-and-improved-performance-tool/): 学習所要時間を細かな単位で分析できる新機能。
- [PyTorchでのTPU活用に関する記事（Hugging Face）](https://huggingface.co/blog/pytorch-xla): PyTorch/XLA を用いた TPU 活用の取り組みを紹介。
- [PyTorch Lightning v1.0.0リリース](https://github.com/PyTorchLightning/pytorch-lightning/releases/tag/1.0.0): ホームページ改修と初のコミュニティイベント開催の告知も掲載。
- [PyTorch Metric Learningの直近リリースまとめ](https://medium.com/@tkm45/pytorch-metric-learning-whats-new-15d6c71a644b): 新規導入された損失関数やアルゴリズムを紹介。
- [ニューラルネットワークの量子化に関する解説記事](https://lab.mo-t.com/blog/quantization-frameworks): 高速化・軽量化に繋がる量子化の概要と利用可能なライブラリを紹介。
- [PyTorch簡略化ライブラリ「Catalyst」がTPU対応（v20.08）](https://twitter.com/Scitator/status/1289530125608919041?s=20): デバイス設定のみで TPU 利用に対応。
- [ディープラーニングによる「マルチタスク学習」の解説動画](https://www.youtube.com/watch?v=2R7CurdWmSY&feature=youtu.be): 複数機能を 1 モデルで学習させる手法の利点と課題を紹介。
- [3次元モデルを扱うライブラリ「PyTorch3D」公開（Facebook AI）](https://ai.facebook.com/blog/-introducing-pytorch3d-an-open-source-library-for-3d-deep-learning/): 短編動画でライブラリの特徴を紹介。

### モデル・アーキテクチャ・損失関数研究

- [TransformersでoptimizerのMuonを使う](https://zenn.dev/colum2131/scraps/5971d43e710718): コンペ上位解法でも使われる Optimizer「Muon」の使い方の紹介。
- [明日使えるかもしれないLoss Functionsのアイディアと実装](https://speakerdeck.com/ftakahashi/ming-ri-shi-erukamosirenailoss-functionsnoaideiatoshi-zhuang): 回帰・分類の特徴的な損失関数を PyTorch 実装つきで解説する資料。
- [モデルパラメータの算術](https://joisino.hatenablog.com/entry/2024/01/09/174517): 重みの平均（Model soups）など深層学習モデルの重みの算術の解説記事。
- [モデルの気持ちになって情報を与えよう](https://medium.com/@junkoda/%E3%83%A2%E3%83%87%E3%83%AB%E3%81%AE%E6%B0%97%E6%8C%81%E3%81%A1%E3%81%AB%E3%81%AA%E3%81%A3%E3%81%A6%E6%83%85%E5%A0%B1%E3%82%92%E4%B8%8E%E3%81%88%E3%82%88%E3%81%86-4fd575d03fb1): モデルに「情報を与える」観点でコンペ解法を読み解く Grandmaster の記事。
- [AdamWにおける改善点をきちんと理解する](https://zenn.dev/bilzard/articles/adamw-demistified): Adam からの変更点を中心に AdamW の論文を解説する記事。
- [モデルの出力ではなく重みを混ぜ合わせるアンサンブル手法の論文](https://arxiv.org/abs/2203.05482): 推論時のモデルが 1 つで済む利点を持つ手法の提案論文。
- [回帰問題でのDropout利用に関する検証記事](https://st1990.hatenablog.com/entry/2021/07/31/155511): 「Dropout と BatchNorm を併用しない方が良い」という話題を検証した記事。
- [GPU計算ライブラリ「CuPy」v8.0.0公開](https://tech.preferred.jp/ja/blog/cupy-v8/): 行列演算高速化や Optuna を用いた最適化などを追加。
- [PyTorchのパフォーマンス改善の紹介動画（ECCV 2020チュートリアル）](https://twitter.com/karpathy/status/1299921324333170689?s=20): コンピュータビジョン国際会議でのチュートリアル発表。
- [Keras風のインターフェースを持つPyTorchライブラリ「NeuralPy」](https://github.com/imdeepmind/NeuralPy): モデルの学習・推論を手軽に行えるライブラリ。
- [PyTorchでTPUを使うライブラリ「PyTorch-XLA」の紹介記事](https://nonbiri-tereka.hatenablog.com/entry/2020/05/26/082922): 簡単な使い方と所感をまとめた記事。
- [深層学習の最適化手法解説動画（SGD・Adamなど）](https://www.youtube.com/watch?v=q933reMpvX8&feature=youtu.be): ミニバッチ勾配降下法から Adam までを体系的に紹介。
- [「Mixed Precision」の解説スライド](https://www.slideshare.net/ssuser21af5b/mixedprecision): PyTorch での実験例と Kaggle Master の知見を交えた解説。
- [Optimizer比較記事（SGD・Adam・AdamW・Adabound・RAdam）](http://acro-engineer.hatenablog.com/entry/2019/12/25/130000): 精度・収束速度・安定性を CIFAR10 実験で比較。

### ライブラリ・フレームワーク・リリース情報

- [PyTorch 2.0: Our next generation release](https://pytorch.org/blog/pytorch-2.0-release/): torch.compile を導入した PyTorch 2.0 の公式リリース告知。
- [Introducing Keras 3.0](https://keras.io/keras_3/): JAX・TensorFlow・PyTorch をバックエンドに使える Keras 3.0 の公開告知。
- [PyTorch 1.11 リリース](https://pytorch.org/blog/pytorch-1.11-released/): TorchData・functorch などの新機能が追加。
- [PyTorch Lightning の紹介資料](https://speakerdeck.com/yongtae723/pytorch-lightningfalsesusume): コード記述を簡略化する PyTorch Lightning の紹介。同内容のブログ記事も公開。
- [PyTorch 1.10 リリース](https://pytorch.org/blog/pytorch-1.10-new-library-releases/): 過学習抑制のための Label Smoothing などの機能を追加。
- [PyTorch 1.9 リリース](https://pytorch.org/blog/pytorch-1.9-released/): torchtext v0.10.0、Transformers v4.7.0（PyTorch 1.9 対応）も同時公開。
- [Lightning Flash v0.3 公開](https://pytorch-lightning.medium.com/lightning-flash-0-3-new-tasks-visualization-tools-data-pipeline-and-flash-registry-api-1e236ba9530): PyTorch Lightning チームによる最先端モデルの手軽な実装ライブラリ。
- [PyTorch Lightningの紹介記事](https://speakerdeck.com/takarasawa_/pytorch-lightning): 基本的な理念と実現できる機能を端的にまとめた記事。
- [PyTorchデバイス間処理ライブラリ「Accelerate」v0.3.0公開](https://github.com/huggingface/accelerate/releases/tag/v0.3.0): TPU 利用時に便利な関数などを追加。
- [C++深層学習ライブラリ「Flashlight」公開（Facebook）](https://ai.facebook.com/blog/flashlight-fast-and-flexible-machine-learning-in-c-plus-plus/): 音声認識プロジェクトでの利用実績があるライブラリ。
- [PyTorchの評価関数ライブラリ「TorchMetrics」の紹介記事](https://pytorch-lightning.medium.com/torchmetrics-pytorch-metrics-built-to-scale-7091b1bec919): 独自の評価関数を定義する方法も解説。
- [ソニーのOSS深層学習ライブラリ「Neural Network Libraries」YouTubeチャンネル開設](https://www.youtube.com/watch?v=4bNAPKTUVtE&feature=youtu.be): 論文解説や技術講座も予定した公式チャンネル。
- [PyTorch Lightning v1.1公開](https://medium.com/pytorch/pytorch-lightning-1-1-model-parallelism-training-and-more-logging-options-7d1e47db7b0b): メモリを節約する sharded model training 機能をベータ実装。
- [TensorFlow v2.4公開](https://blog.tensorflow.org/2020/12/whats-new-in-tensorflow-24.html): Keras の mixed precision 機能が安定版として提供。
- [torchvision v0.8.0の更新情報まとめ記事](https://buildersbox.corp-sansan.com/entry/2020/11/05/110000): PyTorch v1.7 リリースに伴うファイル直接入出力・前処理の GPU 利用に対応。
- [TensorRTで推論を高速化する記事](https://aru47.hatenablog.com/entry/2020/11/28/131116): 複数 GPU や混合精度学習を扱う関連記事も公開。
- [分散並列処理フレームワーク「Ray」v1.0.0公開](https://www.anyscale.com/blog/announcing-ray-1-0): ハイパーパラメータ調整の Ray Tune など高機能なライブラリを提供。
- [Uber「Generative Teaching Networks」論文の紹介記事](https://medium.com/dataseries/uber-creates-deep-neural-networks-to-generate-training-data-for-other-deep-neural-networks-553fedcaa74d): ニューラルネットワークで学習用データセットを生成する手法の紹介。
- [PyTorchによるディープラーニング実装の学び方（3部作）](https://medium.com/pytorch/pytorch%E3%82%92%E7%94%A8%E3%81%84%E3%81%9F%E3%83%87%E3%82%A3%E3%83%BC%E3%83%97%E3%83%A9%E3%83%BC%E3%83%8B%E3%83%B3%E3%82%B0%E5%AE%9F%E8%A3%85%E3%81%AE%E5%AD%A6%E7%BF%92%E6%96%B9%E6%B3%95-part-1-e5f6ad77e0ff): PyTorch コミュニティメンバによる実装学習法の連載。
- [「PyTorch Image Models（timm）」の紹介記事](https://nonbiri-tereka.hatenablog.com/entry/2020/08/26/084816): EfficientNet や ResNeSt などを `create_model` で手軽に利用できるライブラリ。
- [ニューラルネットワークの式の型・shape推論機能の開発記事（PFN）](https://tech.preferred.jp/ja/blog/semi-static-type-shape-and-symbolic-shape-inference/): print デバッグを回避できる shape 推論機能の紹介。
- [Label Smoothingの効果を解説する記事（Google Brain）](https://medium.com/@lessw/label-smoothing-deep-learning-google-brain-explains-why-it-works-and-when-to-use-sota-tips-977733ef020): 最終層への影響を可視化して議論。

## 関連概念

- [画像認識コンペ](./image-recognition.md) / [自然言語処理コンペ](./nlp-llm.md) / [環境構築](./environment.md)
