# 画像認識コンペ

画像認識のコンペは、事前学習済みバックボーンの選択、データ拡張、学習パイプラインの作り込みで競います。
timm などの公開モデルを前提に、いかに速く強いベースラインを立てて育てるかが勝負どころです。ViT・CLIP・自己教師あり学習などの技術動向は [画像認識・視覚モデルの技術動向](./image-recognition-trends.md) を参照してください。

## 押さえどころ

- バックボーン選択には実証研究の知見が使える。NeurIPS 2023「Battle of the Backbones」ではタスク横断の評価で ImageNet-21k 教師あり学習の ConvNeXt が最上位、中規模パラメータでは CNN 優位、ViT は大規模化で伸びる傾向。分類で強いモデルは検出やセグメンテーションでも強い傾向がある
- 公開モデルは「重みは固定したまま処理方法を変える」カスタマイズや、torch.compile や AMP による高速化で飼い慣らす（[野生のモデルを飼い慣らす](https://zenn.dev/bilzard/articles/tame-the-wild-models)）
- ベースラインを立ててから育てる進め方は[イベント](../../events.md)掲載の「画像コンペでのベースラインモデルの育て方」などの発表資料が参考になる
- 音声コンペもスペクトログラム化して画像モデルを適用することが多く、知見が流用できる（[音声コンペ](./audio.md)）
- 分類には timm が定番だが、物体検出・セグメンテーションでは MMDetection・OpenMMLab・Segmentation Models PyTorch など専用ライブラリが使われる。いずれも公開実装をタスクに合わせてどうカスタムするかが腕の見せどころになる

## 資料

### 入門・基礎


- [画像コンペことはじめ](https://zenn.dev/dalab/articles/41b1a0c3b3d410): キノコの分類を題材に、画像コンペの基本的な流れを紹介する入門記事。
- [深層学習による画像認識の基礎](https://www.ohmsha.co.jp/book/9784274231841/): CNN と ViT を実践例とサンプルコードつきで解説する書籍。
- [Kaggleスコアアップセミナー～画像系コンペ入門[前編]（2023/08/02）](https://www.docswell.com/s/fixstars/KLLVPL-20230802)
- [Kaggleスコアアップセミナー～画像系コンペ入門[後編]（2023/09/26）](https://www.docswell.com/s/fixstars/5DE9RG-20230926)
- [Kaggle スコアアップセミナー ～画像系コンペDFL – Bundesliga Data Shootout 編～（2023/05/9）](https://www.docswell.com/s/fixstars/KENEMN-20230509)
- [コンピュータビジョン今昔物語 - 深層学習がＣＶの世界をどう変えたか - (JPTA Tech Talk講演資料)](https://takmin.hatenablog.com/entry/2020/09/10/161621)
- [Vision Transformer入門](https://www.amazon.co.jp/dp/4297130580): Transformer を画像認識分野に応用した Vision Transformer に関する日本語書籍。

### コンペの定跡


- [画像モデルのバックボーンとして最初に何を選ぶべきか？](https://zenn.dev/prgckwb/articles/how-to-select-backbone): 論文「Battle of the Backbones」をもとにバックボーン選択の指針を整理した記事。
- [野生のモデルを飼い慣らす](https://zenn.dev/bilzard/articles/tame-the-wild-models): timm などの公開モデルをタスクに適応させるカスタマイズと高速化のテクニック集。
- [Backboneとしてのtimm2025](https://speakerdeck.com/yu4u/backbonetositenotimm2025): timm の基本的な使い方と 2025 年時点のバックボーン事情をまとめた発表資料。
- [実は強い 非ViTな画像認識モデル](https://speakerdeck.com/tattaka/shi-haqiang-i-fei-vitnahua-xiang-ren-shi-moderu)
- [物体検出フレームワークMMDetectionで快適な開発](https://www.slideshare.net/TatsuyaSuzuki16/mmdetection-236032837)
- [Segmentation Models Pytorch の BackBone をカスタムする方法](https://zenn.dev/syu_tan/articles/c56919106e3682): SMP ライブラリの使い方と拡張方法の解説記事。
- [OpenMMLabの始め方@SUMMER 2023](https://qiita.com/fam_taro/items/7f028dfeae2a79a10fe1): 画像認識ライブラリ OpenMMLab の使い方と Kaggle での事例の紹介。
- [類似画像検索モデルの開発ノウハウ](https://speakerdeck.com/lycorptech_jp/20260526a): Kaggle Grandmaster による類似画像検索モデル開発の知見。タスク概要からモデル学習の工夫まで。
- [動画コンペ小テク集](https://qiita.com/ShunsukeKikuchi/items/53f676a8ae0a3264ee8a): 動画コンペで定番のモデルや開発手法を紹介する知見集。
- [物体検出モデルの推論高速化入門](https://zenn.dev/eversteel_tech/articles/51f9b749b8f051): CPU 推論に焦点を当てた物体検出の高速化手法を実験付きで紹介する記事。
- [チュートリアル：モデルマージ](https://speakerdeck.com/rei0108/tiyutoriaru-moderumazi)
- [Kaggle画像コンペでやっていること①](https://qiita.com/Kmat67916008/items/7aaa41be4e25bace43dc): Kaggle Grandmaster による画像コンペ Tips 連載の第 1 回。
- [Kaggle画像コンペでやっていること②](https://qiita.com/Kmat67916008/items/73e303451e3bc69e50bb): 連載第 2 回。タスク固有の特徴を考えたモデリングを解説。
- [Kaggle画像コンペでやっていること④](https://qiita.com/Kmat67916008/items/d7586a28e6ec8595d579): Kaggle Grandmaster による画像コンペ Tips 連載の最終回。
- [Solafune「マルチ解像度画像の車両検出」提出までの流れ](https://zenn.dev/kwashizzz/articles/solafune-vehicle-det-mmdet): 地上撮影画像から車両を検出するコンペの提出手順を解説。
- [TPUで動作するTensorFlow用の画像データ拡張ライブラリ imgaug-tf](https://github.com/hirune924/imgaug-tf): UW-Madison GI Tract Image Segmentation の参加者が作成・公開。
- [ConvNeXtで小さいサイズの画像を扱う際の知見](https://lab.mo-t.com/blog/convnext): 実験結果と共に改善の流れを解説する記事。

## 関連概念

- [画像認識・視覚モデルの技術動向](./image-recognition-trends.md) / [音声コンペ](./audio.md) / [自然言語処理コンペ](./nlp-llm.md) / [実験管理](./experiment-management.md) / [コンペ形式・技術動向の変遷](./competition-evolution.md)
