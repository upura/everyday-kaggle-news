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

### モデル・技術動向

- [画像に対する自己教師あり表現学習手法について②](https://blog.recruit.co.jp/data/articles/ssl_vision_02/)
- [深層学習によるセマンティックセグメンテーションとその最新動向](https://speakerdeck.com/hf149/shen-ceng-xue-xi-niyorusemanteitukusegumentesiyontosofalsezui-xin-dong-xiang)
- [【DL輪読会】言語以外でのTransformerのまとめ](https://www.slideshare.net/DeepLearningJP2016/dltransformer-vit-perceiver-frozen-pretrained-transformer-etc)
- [最新の深層学習技術による古典くずし字認識の現状と今後の展望](http://shunk031.hatenablog.com/entry/kuzushiji-recognition-survey-2020)
- [DETR手法の変遷と最新動向（CVPR2025）](https://speakerdeck.com/tenten0727/detrshou-fa-nobian-qian-tozui-xin-dong-xiang-cvpr2025)
- [第62回名古屋CV・PRML勉強会：CVPR2025論文紹介 (MambaOut)](https://speakerdeck.com/naok615/di-62hui-ming-gu-wu-cvprmlmian-qiang-hui-cvpr2025lun-wen-shao-jie-mambaout): 状態空間モデル Mamba が画像認識に必要かを分析した論文の紹介資料。
- [点群処理Backbone Networkと点群の事前学習/表現学習](https://speakerdeck.com/nnchiba/biao-xian-xue-xi): 点群を対象にした深層学習の研究動向のサーベイ資料。
- [CVPR 2025 Report](https://x.com/HirokatuKataoka/status/1934663060200833392): 画像認識の国際会議 CVPR 2025 の研究潮流を 180 ページ超にまとめた参加報告資料。
- [Large Vision Language Model (LVLM) に関する最新知見まとめ (Part 1)](https://speakerdeck.com/onely7/large-vision-language-model-lvlm-niguan-suruzui-xin-zhi-jian-matome-part-1): LLM と画像処理をつなぐ機構に焦点を当てた LVLM の知見まとめ。
- [ECCV 2024 速報 (PDF)](https://hirokatsukataoka.net/temp/presen/241004ECCV2024Report_finalized.pdf): 国際会議 ECCV 2024 の研究動向を 130 ページ超にまとめた報告資料。
- [ICCV 2023 速報 (PDF)](https://hirokatsukataoka.net/temp/presen/231006ICCV%202023%20Report%20(Release%20Ver.).pdf): 国際会議 ICCV 2023 の研究動向を 170 ページにまとめた報告資料。
- [「CVPR2023-速報-」ResearchPortトップカンファレンス定点観測 vol.9](https://research-p.com/column/1237): CVPR2023 の投稿状況とキーワードの分析記事。
- [最近のVisual Odometry with Deep Learning](https://speakerdeck.com/tattaka/zui-jin-novisual-odometry-with-deep-learning): 深層学習によるカメラ姿勢追跡の研究動向まとめ。
- [Segment Anything Model 2](https://speakerdeck.com/tenten0727/segment-anything-model-2): SAM 2 を初代との差分も含めて解説する資料。
- [Meta開発のセグメンテーションモデル Segment Anything Model(SAM) の解説](https://zenn.dev/fusic/articles/ml-segment-anything-meta): 初代 SAM の概要を端的にまとめた解説記事。
- [自然言語とVision&Language](https://speakerdeck.com/kuehara/zi-ran-yan-yu-tovision-and-language): 深層学習初期から大規模モデルまでの Vision & Language 研究動向の概観資料。
- [⾃⼰教師あり学習によるビジョン基盤モデルの事前学習](https://speakerdeck.com/hf149/jiao-shi-arixue-xi-niyorubiziyonji-pan-moderunoshi-qian-xue-xi): 画像の自己教師あり学習の代表的手法と発展的話題のまとめ。
- [自己教師あり学習による事前学習（CVIMチュートリアル）](https://speakerdeck.com/naok615/zi-ji-jiao-shi-arixue-xi-niyorushi-qian-xue-xi-cvimtiyutoriaru): 自己教師あり事前学習のサーベイチュートリアル資料。
- [大規模画像テキストデータのフィルタリング手法の紹介](https://speakerdeck.com/lyakaap/da-gui-mo-hua-xiang-tekisutodetanohuirutaringushou-fa-noshao-jie): データフィルタリングで性能を競うコンペを題材にした発表資料。
- [日本語CLIP 学習済みモデルと評価用データセットの公開](https://blog.recruit.co.jp/data/articles/japanese-clip/): 日本語特化 CLIP のモデルと評価データセットの公開記事。
- [AI×医用画像の現状と可能性_2023年版](https://speakerdeck.com/tdys13/aixmedical-imaging-in-japan-2023): 医用画像 AI の研究・応用動向のまとめ資料。
- [最高性能の、日本語画像言語特徴抽出モデル「Japanese Stable CLIP」をリリースしました](https://ja.stability.ai/blog/japanese-stable-clip): Stability AI による日本語特化 CLIP の公開告知。
- [高性能な日本語マルチモーダル基盤モデル「clip-japanese-base」を公開しました](https://techblog.lycorp.co.jp/ja/20240514b): LINE ヤフーによる日本語 CLIP 初版の公開と開発手法の解説。
- [論文まとめ: Local Feature Matching Using Deep Learning: A Survey(202401)](https://qiita.com/fam_taro/items/27f20ccf85fe86821fe6): 局所特徴量マッチングの総説論文の紹介記事。
- [Vision Banana: Image Generators are Generalist Vision Learners](https://speakerdeck.com/kzykmyzw/vision-banana-image-generators-are-generalist-vision-learners): 画像生成モデルの微調整で汎用の画像認識モデルを作る Google DeepMind の取り組みの解説資料。
- [ドメイン特化なCLIPモデルとデータセットの紹介](https://speakerdeck.com/tattaka/domeinte-hua-na-clipmoderutodetasetutonoshao-jie)
- [高性能な日本語マルチモーダル基盤モデル「clip-japanese-base-v2」の公開](https://techblog.lycorp.co.jp/ja/20251218a): LINE ヤフーによる日本語特化 CLIP の公開告知。データフィルタリングと知識蒸留による改善を解説。
- [【論文紹介】Is CLIP ideal? No. Can we fix it? Yes!](https://speakerdeck.com/shun6211/lun-wen-shao-jie-is-clip-ideal-no-can-we-fix-it-yes-di-65hui-konpiyutabiziyonmian-qiang-hui-at-guan-dong): CLIP の埋め込み空間の課題と改善策を提案する論文の紹介資料。
- [Zero-shot Learning網羅的サーベイ：CLIPが切り開いたVision & Languageの新しい世界](https://techblog.exawizards.com/entry/2023/05/10/055218): CLIP 後続の研究 70 本程度を調査したサーベイ記事。
- [Face Recognition @ ECCV2022](https://speakerdeck.com/takarasawa_/face-recognition-at-eccv2022): ArcFace を起点とした顔認証分野の ECCV2022 論文調査資料。
- [AI×医用画像の現状と可能性_2022年版](https://speakerdeck.com/tdys13/aixmedical-imaging-in-japan-2022): 医用画像 AI 領域の研究動向をまとめた資料。
- [動作認識に関するサーベイ資料](https://www.slideshare.net/ttamaki/ss-254290005): 動作認識の手法・タスク・データセットをまとめた資料。
- [CNN vs ViT](https://speakerdeck.com/yushiku/cnn-vs-vit): CNN と ViT を複数観点で比較する発表資料。
- [ECCV 2022 参加記録](https://acro-engineer.hatenablog.com/entry/2022/10/28/123000): 面白かった論文 5 本を紹介する参加記録。
- [『Vision Transformer入門』書評](https://note.com/maxwell/n/nbdda95bc01e0)
- [『Vision Transformer入門』著者による紹介記事](https://snowman-88888.hatenablog.com/entry/2022/09/17/090000): 執筆の背景と各章の概要のまとめ。
- [dethub](https://github.com/okotaku/dethub): 物体検出・セグメンテーションのベースラインと精度向上手法を検討するリポジトリ。
- [衛星データを題材にした機械学習タスクの紹介](https://sorabatake.jp/27897/): 物体検出・セグメンテーション・画像分類・超解像などの整理記事。
- [視覚基盤モデル（DINOv3）を使って衛星画像コンペで勝ちたい](https://www.docswell.com/s/motokimura/KVM382-dinov3-sat-bench): 衛星画像コンペでの視覚基盤モデル活用の実験報告。
- [[輪講] SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features](https://speakerdeck.com/nk35jk/lun-jiang-siglip-2-multilingual-vision-language-encoders-with-improved-semantic-understanding-localization-and-dense-features)
- [LLMの効率化を支えるアルゴリズム](https://speakerdeck.com/taturabe/llmnoxiao-lu-hua-wozhi-eruarugorizumu)
- [Mobile-Former: Bridging MobileNet and Transformer（CVPR 2022 解説資料）](https://speakerdeck.com/tereka114/mobile-former-bridging-mobilenet-and-transformer): CVPR2022 論文読み会での発表資料。
- [Image Matching Challenge 2022 国際会議ワークショップ報告](https://engineers.ntt.com/entry/2022/07/28/090254): 異なる視点から撮影された2画像のマッチング課題に関する報告記事。
- [MIRU2022特別企画「局所特徴量・AlexNet・カーネル法」](https://sites.google.com/view/miru2022/program/specialevent?authuser=0): 過去の著名な研究や時代背景に焦点を当てた講演資料。
- [局所特徴抽出における特徴表現の変遷まとめ](https://speakerdeck.com/hf149/ju-suo-te-zheng-liang-hua-xiang-ren-shi-niokerute-zheng-biao-xian-huo-de-falsebian-qian): SIFT から Vision Transformer まで幅広い変遷を紹介する資料。
- [CVPR 2022 論文の日本語まとめ](https://xpaperchallenge.org/cv/survey/cvpr2022_summaries/listall/): 有志による CVPR 2022 採択論文の日本語サマリ集。
- [少量データ・ラベルから効率的に学習する技術の最新研究動向（SSII2022）](https://www.slideshare.net/SSII_Slides/ssii2022-ss2): 不足情報を補うための手法を概観した資料。
- [画像認識分野でのTransformer応用解説（SSII2022）](https://speakerdeck.com/yushiku/20220608_ssii_transformer): Transformer の概要・応用範囲・近年の潮流を紹介。
- [階層的Vision Transformerの研究動向まとめ](https://www.slideshare.net/ren4yu/hierarchical-vision-transformer): Swin Transformer など Kaggle でも多用されるモデルの研究動向。
- [ArcFace関連の距離学習手法サーベイ](https://speakerdeck.com/takarasawa_/face-recognition-and-arcface-papers): 顔認識タスクを題材に距離学習関連の関連研究をまとめた資料。

## 関連概念

- [音声コンペ](./audio.md) / [自然言語処理コンペ](./nlp-llm.md) / [実験管理](./experiment-management.md)
