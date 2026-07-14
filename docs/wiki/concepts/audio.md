# 音声コンペ

音声や音響イベントを扱うコンペ（BirdCLEF、DCASE など）では、波形をメルスペクトログラムに変換して画像認識モデルを適用するのが定跡です。
異常音検知や音声認識など、タスクごとに設定の癖が強いのも特徴です。

## 押さえどころ

- 定番のパイプラインは「波形 → メルスペクトログラム → 画像認識モデル」。[画像認識コンペ](./image-recognition.md)の知見（バックボーン選択やデータ拡張）がそのまま活きる
- 異常音検知（DCASE Task 2 系）は「学習データは正常音のみ」の教師なし設定で、オートエンコーダ系のベースラインすら超えにくい難タスク（[DCASE 2020 Task 2 の解説](https://qiita.com/daisukelab/items/b106c567cf8927a5519a)）
- 音声認識は ESPnet Model Zoo などの学習済みモデルを数行のコードで利用できる
- 音声を扱うマルチモーダル LLM の潮流は[自然言語処理コンペ](./nlp-llm.md)とも接続する
- 鳥の鳴き声（BirdCLEF）や DCASE の異常音検知・音響イベント検出は毎年開催される定番コンペで、複数年分の振り返り記事が蓄積されている。ラベルなしデータの活用（DCASE2020 1位解法など）が勝敗を分けるポイントとして繰り返し登場する
- 時間-周波数解析の工夫（Superlets など）は、脳波（HMS コンペ）のような音声以外の波形データにも応用が効く

## 資料

### 音声認識

- [ESPnet による音声認識入門 ～ESPnet Model Zoo 編～](https://note.com/retrieva/n/nd04d38377f1b): 学習済みモデルをダウンロードして数行で音声認識を動かす入門記事。
- [Speech Language Models - a reazon-research Collection](https://huggingface.co/collections/reazon-research/speech-language-models): 日本語音声認識の事前学習済みモデル群の公開コレクション。
- [音声認識ライブラリ「HuggingSound」の紹介記事](https://www.ai-shift.co.jp/techblog/2547): 日本語データでファインチューニングする方法を解説。
- [Hugging Face「Robust Speech Recognition Challenge」開催](https://discuss.huggingface.co/t/open-to-the-community-robust-speech-recognition-challenge/13614): 多言語音声認識を題材にしたコンペの開催告知。
- [近年の音声認識手法の動向まとめ記事](https://ys0510.hatenablog.com/entry/e2e_asr): 一つのニューラルネットワークで処理する End-to-End 手法に焦点を当てた記事。
- [音声認識ライブラリ「ESPnet」の紹介記事](https://tech.retrieva.jp/entry/2020/12/23/170645): 学習済みモデルを用いた音声認識の実践例。
- [PyTorchによる音声分類チュートリアル](https://github.com/daisukelab/sound-clf-pytorch): Kaggle「Freesound General-Purpose Audio Tagging Challenge」を題材にしたチュートリアル。

### 異常音検知・音響イベント検出

- [機械音の異常検知チャレンジ DCASE 2020 Task 2](https://qiita.com/daisukelab/items/b106c567cf8927a5519a): 教師なし異常音検知タスクのデータセット分析と複数ベースラインの実験記録。コードも公開されている。
- [DCASE Challenge 2022 課題一覧発表](http://dcase.community/articles/challenge-tasks-for-dcase2022): 音響イベント検出コンペの年次課題発表。
- [2020〜2021年の鳥の鳴き声コンペ3つの振り返り記事](https://qiita.com/tattaka/items/ed355707963ec48a8106): 各コンペの概要と際立った解法をまとめた記事。
- [DCASE 2021 技術報告まとめ](http://dcase.community/challenge2021/task-unsupervised-detection-of-anomalous-sounds): 異常音検知など複数部門の上位チーム技術報告。
- [環境音認識の研究概要と動向紹介動画（DCASE2020含む）](https://linedevday.linecorp.com/2020/ja/sessions/5825): 「DCASE2020 Challenge」1 位解法の具体的手法も解説。
- [DCASE2020 Challenge 1位解法](https://engineering.linecorp.com/ja/blog/dcase2020-challenge/): YouTube 動画の音を分類する課題への取り組みを紹介。ラベルなしデータの活用が要点。

### モデル・技術動向

- [湘南kaggler会 音声認識で使うのってメルス・・・なんだっけ？](https://speakerdeck.com/sugupoko/20250413-xiang-nan-kagglerhui-yin-sheng-ren-shi-deshi-unotutemerusunandatuke)
- [Deep Learning (for Audio) with Python](https://www.youtube.com/playlist?list=PL-wATfeyAMNrtbkCNsLcpoAyBBRJZVlnf)
- [音学シンポジウム 2025 チュートリアル 「マルチモーダル大規模言語モデル入門」](https://github.com/ryota-komatsu/slp2025)
- [音声感情認識技術の進展と展望](https://speakerdeck.com/nagase/yin-sheng-gan-qing-ren-shi-ji-shu-nojin-zhan-tozhan-wang): 音声感情認識の基礎と研究動向のサーベイ資料。
- [Superlets: 時間-周波数解析における「超解像度」filterbank](https://zenn.dev/bilzard/articles/stft-wavelet-superlet): HMS コンペ優勝解法に登場した時間-周波数解析手法の解説記事。
- [クロスモーダル表現学習の研究動向: 音声関連を中心として](https://speakerdeck.com/ryomasumura/kurosumodarubiao-xian-xue-xi-noyan-jiu-dong-xiang-yin-sheng-guan-lian-wozhong-xin-tosite): 音声を中心としたクロスモーダル表現学習の研究動向の解説資料。
- [muana vol.11 音楽識別の事前学習モデル](https://speakerdeck.com/yamathcy/muana-vol-dot-11-yin-le-shi-bie-noshi-qian-xue-xi-moderu): 音楽識別のための事前学習済みモデルと活用知見の解説資料。
- [波形データを扱うニューラルネットワークの解説動画（SONY）](https://www.youtube.com/watch?v=_4r7uTIPG1s&feature=youtu.be): OSS「Neural Network Libraries」開発元による動画シリーズの一本。

## 関連概念

- [画像認識コンペ](./image-recognition.md) / [自然言語処理コンペ](./nlp-llm.md)
