# 音声コンペ

音声や音響イベントを扱うコンペ（BirdCLEF、DCASE など）では、波形をメルスペクトログラムに変換して画像認識モデルを適用するのが定跡です。
異常音検知や音声認識など、タスクごとに設定の癖が強いのも特徴です。

## 押さえどころ

- 定番のパイプラインは「波形 → メルスペクトログラム → 画像認識モデル」。[画像認識コンペ](./image-recognition.md)の知見（バックボーン選択やデータ拡張）がそのまま活きる
- 異常音検知（DCASE Task 2 系）は「学習データは正常音のみ」の教師なし設定で、オートエンコーダ系のベースラインすら超えにくい難タスク（[DCASE 2020 Task 2 の解説](https://qiita.com/daisukelab/items/b106c567cf8927a5519a)）
- 音声認識は ESPnet Model Zoo などの学習済みモデルを数行のコードで利用できる
- 音声を扱うマルチモーダル LLM の潮流は[自然言語処理コンペ](./nlp-llm.md)とも接続する

## 資料

- [国際音声AIコンペ総合第1位：URGENT Challenge優勝モデルの技術解説](https://zenn.dev/softbank/articles/bf95e2e274cf97): 多様な劣化を含む音声を復元する国際コンペの優勝解法の技術解説。
- [機械音の異常検知チャレンジ DCASE 2020 Task 2](https://qiita.com/daisukelab/items/b106c567cf8927a5519a): 教師なし異常音検知タスクのデータセット分析と複数ベースラインの実験記録。コードも公開されている。
- [ESPnet による音声認識入門 ～ESPnet Model Zoo 編～](https://note.com/retrieva/n/nd04d38377f1b): 学習済みモデルをダウンロードして数行で音声認識を動かす入門記事。
- [湘南kaggler会 音声認識で使うのってメルス・・・なんだっけ？](https://speakerdeck.com/sugupoko/20250413-xiang-nan-kagglerhui-yin-sheng-ren-shi-deshi-unotutemerusunandatuke)
- [Deep Learning (for Audio) with Python](https://www.youtube.com/playlist?list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf)
- [音学シンポジウム 2025 チュートリアル 「マルチモーダル大規模言語モデル入門」](https://github.com/ryota-komatsu/slp2025)
- [Speech Language Models - a reazon-research Collection](https://huggingface.co/collections/reazon-research/speech-language-models): 日本語音声認識の事前学習済みモデル群の公開コレクション。
- [音声感情認識技術の進展と展望](https://speakerdeck.com/nagase/yin-sheng-gan-qing-ren-shi-ji-shu-nojin-zhan-tozhan-wang): 音声感情認識の基礎と研究動向のサーベイ資料。
- [Superlets: 時間-周波数解析における「超解像度」filterbank](https://zenn.dev/bilzard/articles/stft-wavelet-superlet): HMS コンペ優勝解法に登場した時間-周波数解析手法の解説記事。

## 関連概念

- [画像認識コンペ](./image-recognition.md) / [自然言語処理コンペ](./nlp-llm.md)
