# 画像認識コンペ

画像認識のコンペは、事前学習済みバックボーンの選択・データ拡張・学習パイプラインの作り込みで競います。
timm などの公開モデルを前提に、いかに速く強いベースラインを立てて育てるかが勝負どころです。

## 押さえどころ

- バックボーン選択には実証研究の知見が使える。NeurIPS 2023「Battle of the Backbones」では ImageNet-21k 教師あり学習の ConvNeXt が総合的に強く、中規模パラメータでは CNN 優位、ViT は大規模化で伸びる傾向。分類で強いモデルは検出・セグメンテーションでも強い傾向がある
- 公開モデルは「重みは固定したまま処理方法を変える」カスタマイズや、torch.compile・AMP による高速化で飼い慣らす([野生のモデルを飼い慣らす](https://zenn.dev/bilzard/articles/tame-the-wild-models))
- ベースラインを立ててから育てる進め方は[イベント](../../events.md)掲載の「画像コンペでのベースラインモデルの育て方」などの発表資料が参考になる
- 音声・音響コンペもスペクトログラム化して画像モデルを適用することが多く、知見が流用できる([音声・音響コンペ](./audio.md))

## 資料

- [画像モデルのバックボーンとして最初に何を選ぶべきか？](https://zenn.dev/prgckwb/articles/how-to-select-backbone): 論文「Battle of the Backbones」をもとにバックボーン選択の指針を整理した記事。
- [野生のモデルを飼い慣らす](https://zenn.dev/bilzard/articles/tame-the-wild-models): timm などの公開モデルをタスクに適応させるカスタマイズと高速化のテクニック集。
- [Kaggleスコアアップセミナー～画像系コンペ入門[前編]（2023/08/02）](https://www.docswell.com/s/fixstars/KLLVPL-20230802)
- [Kaggleスコアアップセミナー～画像系コンペ入門[後編]（2023/09/26）](https://www.docswell.com/s/fixstars/5DE9RG-20230926)
- [実は強い 非ViTな画像認識モデル](https://speakerdeck.com/tattaka/shi-haqiang-i-fei-vitnahua-xiang-ren-shi-moderu)
- [Kaggle スコアアップセミナー ～画像系コンペDFL – Bundesliga Data Shootout 編～（2023/05/9）](https://www.docswell.com/s/fixstars/KENEMN-20230509)
- [コンピュータビジョン今昔物語 - 深層学習がＣＶの世界をどう変えたか - (JPTA Tech Talk講演資料)](https://takmin.hatenablog.com/entry/2020/09/10/161621)
- [物体検出フレームワークMMDetectionで快適な開発](https://www.slideshare.net/TatsuyaSuzuki16/mmdetection-236032837)
- [画像に対する自己教師あり表現学習手法について②](https://blog.recruit.co.jp/data/articles/ssl_vision_02/)
- [深層学習によるセマンティックセグメンテーションとその最新動向](https://speakerdeck.com/hf149/shen-ceng-xue-xi-niyorusemanteitukusegumentesiyontosofalsezui-xin-dong-xiang)
- [【DL輪読会】言語以外でのTransformerのまとめ](https://www.slideshare.net/DeepLearningJP2016/dltransformer-vit-perceiver-frozen-pretrained-transformer-etc)
- [最新の深層学習技術による古典くずし字認識の現状と今後の展望](http://shunk031.hatenablog.com/entry/kuzushiji-recognition-survey-2020)
- [DETR手法の変遷と最新動向（CVPR2025）](https://speakerdeck.com/tenten0727/detrshou-fa-nobian-qian-tozui-xin-dong-xiang-cvpr2025)
- [ドメイン特化なCLIPモデルとデータセットの紹介](https://speakerdeck.com/tattaka/domeinte-hua-na-clipmoderutodetasetutonoshao-jie)
- [[輪講] SigLIP 2: Multilingual Vision-Language Encoders with Improved Semantic Understanding, Localization, and Dense Features](https://speakerdeck.com/nk35jk/lun-jiang-siglip-2-multilingual-vision-language-encoders-with-improved-semantic-understanding-localization-and-dense-features)
- [チュートリアル：モデルマージ](https://speakerdeck.com/rei0108/tiyutoriaru-moderumazi)
- [LLMの効率化を支えるアルゴリズム](https://speakerdeck.com/taturabe/llmnoxiao-lu-hua-wozhi-eruarugorizumu)

## 関連概念

- [音声・音響コンペ](./audio.md) / [自然言語処理・LLM コンペ](./nlp-llm.md) / [実験管理](./experiment-management.md)
