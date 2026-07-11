# 画像認識コンペ

画像認識のコンペは、事前学習済みバックボーンの選択、データ拡張、学習パイプラインの作り込みで競います。
timm などの公開モデルを前提に、いかに速く強いベースラインを立てて育てるかが勝負どころです。

## 押さえどころ

- バックボーン選択には実証研究の知見が使える。NeurIPS 2023「Battle of the Backbones」ではタスク横断の評価で ImageNet-21k 教師あり学習の ConvNeXt が最上位、中規模パラメータでは CNN 優位、ViT は大規模化で伸びる傾向。分類で強いモデルは検出やセグメンテーションでも強い傾向がある
- 公開モデルは「重みは固定したまま処理方法を変える」カスタマイズや、torch.compile や AMP による高速化で飼い慣らす（[野生のモデルを飼い慣らす](https://zenn.dev/bilzard/articles/tame-the-wild-models)）
- ベースラインを立ててから育てる進め方は[イベント](../../events.md)掲載の「画像コンペでのベースラインモデルの育て方」などの発表資料が参考になる
- 音声コンペもスペクトログラム化して画像モデルを適用することが多く、知見が流用できる（[音声コンペ](./audio.md)）

## 資料

### 入門・基礎

- [画像コンペことはじめ](https://zenn.dev/dalab/articles/41b1a0c3b3d410): キノコの分類を題材に、画像コンペの基本的な流れを紹介する入門記事。
- [Kaggleスコアアップセミナー～画像系コンペ入門[前編]（2023/08/02）](https://www.docswell.com/s/fixstars/KLLVPL-20230802)
- [Kaggleスコアアップセミナー～画像系コンペ入門[後編]（2023/09/26）](https://www.docswell.com/s/fixstars/5DE9RG-20230926)
- [Kaggle スコアアップセミナー ～画像系コンペDFL – Bundesliga Data Shootout 編～（2023/05/9）](https://www.docswell.com/s/fixstars/KENEMN-20230509)
- [コンピュータビジョン今昔物語 - 深層学習がＣＶの世界をどう変えたか - (JPTA Tech Talk講演資料)](https://takmin.hatenablog.com/entry/2020/09/10/161621)

### コンペの定跡

- [画像モデルのバックボーンとして最初に何を選ぶべきか？](https://zenn.dev/prgckwb/articles/how-to-select-backbone): 論文「Battle of the Backbones」をもとにバックボーン選択の指針を整理した記事。
- [野生のモデルを飼い慣らす](https://zenn.dev/bilzard/articles/tame-the-wild-models): timm などの公開モデルをタスクに適応させるカスタマイズと高速化のテクニック集。
- [Backboneとしてのtimm2025](https://speakerdeck.com/yu4u/backbonetositenotimm2025): timm の基本的な使い方と 2025 年時点のバックボーン事情をまとめた発表資料。
- [実は強い 非ViTな画像認識モデル](https://speakerdeck.com/tattaka/shi-haqiang-i-fei-vitnahua-xiang-ren-shi-moderu)
- [物体検出フレームワークMMDetectionで快適な開発](https://www.slideshare.net/TatsuyaSuzuki16/mmdetection-236032837)
- [類似画像検索モデルの開発ノウハウ](https://speakerdeck.com/lycorptech_jp/20260526a): Kaggle Grandmaster による類似画像検索モデル開発の知見。タスク概要からモデル学習の工夫まで。
- [動画コンペ小テク集](https://qiita.com/ShunsukeKikuchi/items/53f676a8ae0a3264ee8a): 動画コンペで定番のモデルや開発手法を紹介する知見集。
- [物体検出モデルの推論高速化入門](https://zenn.dev/eversteel_tech/articles/51f9b749b8f051): CPU 推論に焦点を当てた物体検出の高速化手法を実験付きで紹介する記事。
- [チュートリアル：モデルマージ](https://speakerdeck.com/rei0108/tiyutoriaru-moderumazi)

### モデル・技術動向

- [画像に対する自己教師あり表現学習手法について②](https://blog.recruit.co.jp/data/articles/ssl_vision_02/)
- [深層学習によるセマンティックセグメンテーションとその最新動向](https://speakerdeck.com/hf149/shen-ceng-xue-xi-niyorusemanteitukusegumentesiyontosofalsezui-xin-dong-xiang)
- [【DL輪読会】言語以外でのTransformerのまとめ](https://www.slideshare.net/DeepLearningJP2016/dltransformer-vit-perceiver-frozen-pretrained-transformer-etc)
- [最新の深層学習技術による古典くずし字認識の現状と今後の展望](http://shunk031.hatenablog.com/entry/kuzushiji-recognition-survey-2020)
- [DETR手法の変遷と最新動向（CVPR2025）](https://speakerdeck.com/tenten0727/detrshou-fa-nobian-qian-tozui-xin-dong-xiang-cvpr2025)
- [第62回名古屋CV・PRML勉強会：CVPR2025論文紹介 (MambaOut)](https://speakerdeck.com/naok615/di-62hui-ming-gu-wu-cvprmlmian-qiang-hui-cvpr2025lun-wen-shao-jie-mambaout): 状態空間モデル Mamba が画像認識に必要かを分析した論文の紹介資料。
- [点群処理Backbone Networkと点群の事前学習/表現学習](https://speakerdeck.com/nnchiba/biao-xian-xue-xi): 点群を対象にした深層学習の研究動向のサーベイ資料。
- [Vision Banana: Image Generators are Generalist Vision Learners](https://speakerdeck.com/kzykmyzw/vision-banana-image-generators-are-generalist-vision-learners): 画像生成モデルの微調整で汎用の画像認識モデルを作る Google DeepMind の取り組みの解説資料。
- [ドメイン特化なCLIPモデルとデータセットの紹介](https://speakerdeck.com/tattaka/domeinte-hua-na-clipmoderutodetasetutonoshao-jie)
- [高性能な日本語マルチモーダル基盤モデル「clip-japanese-base-v2」の公開](https://techblog.lycorp.co.jp/ja/20251218a): LINE ヤフーによる日本語特化 CLIP の公開告知。データフィルタリングと知識蒸留による改善を解説。
- [【論文紹介】Is CLIP ideal? No. Can we fix it? Yes!](https://speakerdeck.com/shun6211/lun-wen-shao-jie-is-clip-ideal-no-can-we-fix-it-yes-di-65hui-konpiyutabiziyonmian-qiang-hui-at-guan-dong): CLIP の埋め込み空間の課題と改善策を提案する論文の紹介資料。
- [視覚基盤モデル（DINOv3）を使って衛星画像コンペで勝ちたい](https://www.docswell.com/s/motokimura/KVM382-dinov3-sat-bench): 衛星画像コンペでの視覚基盤モデル活用の実験報告。
- [[輪講] SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features](https://speakerdeck.com/nk35jk/lun-jiang-siglip-2-multilingual-vision-language-encoders-with-improved-semantic-understanding-localization-and-dense-features)
- [LLMの効率化を支えるアルゴリズム](https://speakerdeck.com/taturabe/llmnoxiao-lu-hua-wozhi-eruarugorizumu)

## 関連概念

- [音声コンペ](./audio.md) / [自然言語処理コンペ](./nlp-llm.md) / [実験管理](./experiment-management.md)
