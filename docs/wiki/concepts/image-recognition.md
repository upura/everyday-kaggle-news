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

網羅的な一覧は[話題別一覧の「画像認識」](../../materials.md#画像認識)を参照。

## 関連概念

- [音声・音響コンペ](./audio.md) / [自然言語処理・LLM コンペ](./nlp-llm.md) / [実験管理](./experiment-management.md)
