# グラフ

グラフ構造データ（ネットワーク、分子、関係データなど）を扱う話題のページです。
表データやテキストとは異なり、ノード間の接続関係を捉えるモデリング（グラフニューラルネットワークなど）が求められます。

## 押さえどころ

- グラフ構造データは「ノードとエッジ」の接続関係そのものが情報を持つため、GBDT に落とし込む特徴量エンジニアリング（次数、近傍集約、グラフ埋め込みなど）を行うか、GNN による直接のモデリングを行うかが最初の分岐になる
- Kaggle 単独でのグラフコンペは少なく、「KDD Cup 2021」に続く[NeurIPS 2022 の大規模グラフコンペ](https://ogb.stanford.edu/neurips2022/)（Open Graph Benchmark 主催）のように、国際学会併設の大規模ベンチマーク形式で開催される傾向がある
- 体系的な学習リソースは比較的充実している。演習形式の[グラフ道場](https://yuya-s.github.io/GraphDojo/)、スタンフォード大学「Machine Learning with Graphs」講義、『グラフニューラルネットワーク』などの書籍で、基礎からアーキテクチャまでを一通り追える
- 企業の取引関係グラフからの格付け予測（GCN と LightGBM の比較など）のように、コンペ以外の実務でもグラフ構造データを活用した深層学習事例が蓄積されている
- 大規模グラフでは cuGraph のような GPU 対応ライブラリによる前処理や分析の高速化も選択肢になる

## 資料

- [グラフ道場 (Graph Dojo)](https://yuya-s.github.io/GraphDojo/)
- [データのつながりを活かす技術〜ネットワーク／グラフデータの機械学習から得られる新視点](https://gihyo.jp/book/2025/978-4-297-14784-6): グラフ構造データの特徴抽出と機械学習活用を解説する書籍。
- [僕たちがグラフニューラルネットワークを学ぶ理由](https://speakerdeck.com/joisino/pu-tatigagurahuniyurarunetutowakuwoxue-buli-you): 『グラフニューラルネットワーク』著者による導入と応用の紹介資料。
- [グラフニューラルネットワーク(GNN)徹底解説！用途と仕組みからPyGでの実装まで](https://zenn.dev/kami/articles/83c2daff760f5d): 前提知識から PyG 実装までを扱う GNN の解説記事。
- [グラフニューラルネットワーク（PyTorch実装つき書籍）](https://www.ohmsha.co.jp/book/9784274228872/): 基本的な知識や研究事例を PyTorch 実装とともに紹介する書籍。
- [大規模グラフデータを題材にしたNeurIPS 2022コンペ](https://ogb.stanford.edu/neurips2022/): 「KDD Cup 2021」に続き 2 度目の開催となった国際学会併設コンペ。
- [グラフニューラルネットワークの解説記事](https://theaisummer.com/gnn-architectures/): グラフ表現学習の基礎から代表的な GNN アーキテクチャまでを扱う解説記事。
- [GPU上でグラフデータを分析するライブラリ「cuGraph」の紹介記事](https://acro-engineer.hatenablog.com/entry/2021/05/21/120000): PageRank の計算速度を比較し、cuGraph の導入方法を解説する記事。
- [スタンフォード大学「Machine Learning with Graphs」講義動画](https://www.youtube.com/playlist?list=PLoROMvodv4rPLKxIpqhjhPgdQy7imNkDn): ノード埋め込みや GNN の理論を体系的に扱う講義動画。
- [GCNを用いた企業格付け予測手法（SIG-FIN発表）](https://www.slideshare.net/MasakazuMori2/gcn-230165927): 取引関係の有向グラフから特徴を獲得する手法を、LightGBM との精度比較を交えて提案した発表資料。
- [グラフのデータ分析に関する概説資料](https://www.slideshare.net/ssuser0c8361/20200212-227754437): グラフ表現学習、グラフ畳み込みニューラルネットワーク、学会動向をまとめた資料。
- [ネットワークデータに対する深層学習の紹介記事](https://buildersbox.corp-sansan.com/entry/2021/02/19/114000): 数式を抑えてタスクの全体像と代表的モデルを解説した記事。
- [Graph Neural Networks: Foundations, Frontiers, and Applications](https://graph-neural-networks.github.io/): 27 章にわたる無料公開のグラフニューラルネットワーク書籍。

## 関連概念

- [表データコンペ](./tabular.md) / [推薦](./recommendation.md)
