# コンペ開催

コンペに「参加する」側ではなく「開催する」側の知見を集めたページです。
コミュニティコンペの運営 Tips から、企業・研究データを使った開催報告までを扱います。

## 押さえどころ

- 企業主催コンペは「問題設計の工夫」を語る報告が多い。金融時系列（三井物産コモディティ予測・JPX 株価予測）を手がけた開催者による一連の解説は、データリークが起きやすい領域での設計上の勘所を具体的に示す
- 社内コンペは人材育成や組織文化の醸成を目的に据える例が目立つ（NTT グループ横断 100 人規模、パナソニック、リクルート、DeNA など）。難易度調整や役割設計など、外部公開のコミュニティコンペとは異なる運営上の配慮が語られる
- コミュニティコンペ（atmaCup、関西 Kaggler 会、大学サークルなど）は、個人や小規模チームでも開催できることを示す実践記が多い。継続開催のノウハウや、Hugging Face Competitions のようなプラットフォーム機能を使う軽量な開催方法も紹介されている
- 研究データを使った学会併設コンペは、開催後に成果を論文化する流れが定着している（重力波・IceCube・PANDA・OpenVaccine など Nature 系ジャーナルや arXiv への掲載例が複数）。上位解法の紹介だけでなく、コンペという形式自体の有効性を検証する内容も含む
- プラットフォーム運営者側の視点（Solafune・Nishika・RecSys Challenge など）からは、個人情報や機密データの取り扱いへの懸念（Nishika）、有効だった審査・運営手法の総括（RecSys Challenge）など、参加者目線では見えにくい運営特有の論点が語られる
- 評価設計・リーク対策は[性能評価と検証](./evaluation-validation.md)と表裏の関係にある

## 資料

### 企業主催コンペの開催報告

- [LINEヤフー データサイエンス Meetup「三井物産コモディティ予測チャレンジ」の舞台裏-AlpacaTechパート](https://speakerdeck.com/gamella/lineyahu-detasaiensu-meetup-san-jing-wu-chan-komodeiteiyu-ce-tiyarenzi-nowu-tai-li-alpacatechpato): 企業主催 Kaggle コンペの設計者による発表資料。金融タスク特有の問題設計の工夫を説明。
- [Kaggleコンペ「MITSUI & CO. Commodity Prediction Challenge」問題設計 詳細解説](https://zenn.dev/gamella/articles/7e944bd18cdbe6): 同コンペの設計担当者による解説記事。金融時系列コンペ特有の課題と設計意図を詳述。
- [【Kaggle×人材育成】NTTグループ横断で100人が参加！Python初心者も2時間で楽しめるKaggleオンサイトコンペをやった話](https://qiita.com/daikon_desu/items/e6f672324d5d9c2ab1f3): 企業内の初心者向けオンサイトコンペの開催報告。修正箇所をプロンプトに限定する難易度調整など運営の工夫を紹介。
- [JPX Tokyo Stock Exchange Prediction 開催知見](https://zenn.dev/gamella/articles/eaf7fe5a96bdf0): 金融コンペの問題設計の工夫を綴る主催者記事。
- [日経電子版のデータを用いた機械学習コンペティションをKaggle Days Tokyoで開催しました](https://hack.nikkei.com/blog/report_kaggle_days_tokyo)
- [パナソニックグループ社内コンペの開催報告](https://tech-ai.panasonic.com/jp/blog_page.html?id=20220805): Kaggle Grandmaster の社員が監修し、データも公開された社内コンペの報告記事。
- [社内コンペ開催に向けたサンプルノートブックの紹介記事](https://blog.recruit.co.jp/data/articles/mlcomp2021_sample_notebooks/): コンペにおける役割や意識した点を綴った記事。
- [リクルート社内機械学習コンテストの開催報告連載記事](https://blog.recruit.co.jp/data/articles/ml_compe2021_vol1/): 開催の背景や目的を紹介する連載第 1 回。
- [社内データ分析コンペを独自サイトで開催した事例記事](https://engineers.ntt.com/entry/2021/08/30/130431): 順位表に加えコード共有・議論機能も備えた独自コンペサイトの構築事例。
- [DeNAの機械学習基盤に関する発表動画](https://techcon.dena.com/2021/session/12/): コンペ形式で事業課題を解決する仕組みを紹介。
- [プッシュ通知開封率予測を題材にした社内コンペの紹介記事](https://tech.connehito.com/entry/2020/08/27/165753): 自社データを使う社内コンペの取り組みやすさを紹介。

### コミュニティコンペの開催Tips・実践記

- [コミュニティコンペティションを開催するときの Tips 集](https://www.abap34.com/posts/community_competetion_tips.html)
- [コンペを気楽に開催しよーぜ!@関西Kaggler会](https://speakerdeck.com/nyk510/konpewoqi-le-nikai-cui-siyoze-at-guan-xi-kagglerhui): atmaCup 主催者によるコンペ開催のすすめの発表資料。
- [Kaggleコミュニティコンペの開き方と振り返り](https://qiita.com/Ryushi496/items/dfc5dea38ac03e33acc8)
- [Kaggle days Championshipのようなコンペを開催した話](https://zenn.dev/ryushi496/articles/4df4f2412cfdd9): 6 時間で 2 コンペを解く形式のコミュニティコンペの開催報告。
- [kaggleコミュニティコンペ開催報告と上位解法](https://zenn.dev/ryushi496/articles/6213f94a4c7f29): 写真の撮影国を当てるコミュニティコンペの開催報告と上位解法。
- [traP コンペ 2023 夏 sponsored by ピクシブ株式会社 運営後記](https://trap.jp/post/1975/): 大学サークルによるコミュニティコンペ運営の記録。
- [東工大サークルでの Kaggle 部設立記](https://trap.jp/post/1697/): 初心者向けコンペの開催記録を含む Kaggle 部設立の記事。
- [Hugging FaceのCompetitionsでscriptコンペをホストしてみた](https://www.ai-shift.co.jp/techblog/4271): Hugging Face の Competitions 機能による社内コンペ開催の報告。
- [[関西Kaggler会 配布版] コミュニティコンペの継続的な開催について](https://speakerdeck.com/nejumi/guan-xi-kagglerhui-pei-bu-ban-komiyuniteikonpenoji-sok-de-nakai-cui-nituite): Kaggle の機能を用いた独自コンペの継続開催の知見をまとめた資料。
- [Kaggle Conversations（Adaption Labs）](https://www.youtube.com/watch?v=lnKnLZd66Ng): Adaption Labs の CEO が、同社が開催した Kaggle コンペの狙いと AI 研究の展望を語る動画シリーズ。
- [Kaggleでコンペを開催する場合の検討事項をまとめた記事](https://note.com/m3dag/n/na1f1667a0ccb): 必要な情報や開催の利点を紹介する記事。
- [「CA × atmaCup 2nd」開催側視点の振り返り記事](https://developers.cyberagent.co.jp/blog/archives/28220/): サイバーエージェントによるコンペ開催の意義を語る記事。
- [サイバーエージェントのデータ分析コンペ開催知見の発表資料](https://speakerdeck.com/ykaneko1992/bizinesu-falseren-de-nixi-siikonpekai-cui-falseyarifang): 開催で得られた知見とビジネス価値を紹介。Mobility Technologies・ヤフーの Master も登壇。
- [atmaCup主催者nyk510さんによるコンペ設計の取り組み紹介](https://speakerdeck.com/nyk510/onsaitodetakonpefalsemei-li-guan-waruquan-yuan-gale-siikonpeshe-ji-falsetamefalsequ-rizu-mi): 課題設計に加え初心者向けサポートにも言及。
- [アイリス株式会社が機械学習コンペ環境構築コードをOSS公開](https://github.com/AillisInc/ml_competition_platform): 管理者が評価指標を定義し参加者がファイル投稿できる枠組み。

### 研究データ・学会併設コンペの開催論文

- [Learning to detect continuous gravitational waves: an open data-analysis competition](https://arxiv.org/abs/2509.06445)
- [Public Kaggle Competition IceCube Analysis](https://arxiv.org/abs/2307.15289)
- [PLAsTiCC Astronomical Classification Results](https://arxiv.org/abs/2012.12392)
- [Ribonanza: deep learning of RNA structure through dual crowdsourcing](https://www.biorxiv.org/content/10.1101/2024.02.24.581671v1): Kaggle「Stanford Ribonanza RNA Folding」の成果と知見をまとめた論文。
- [IceCube -- Neutrinos in Deep Ice The Top 3 Solutions from the Public Kaggle Competition](https://arxiv.org/abs/2310.15674): IceCube コンペ上位 3 チームの取り組みを紹介する論文。
- [大規模な船舶の検出・特性評価コンペの結果報告論文](https://arxiv.org/abs/2206.00897): データセットやコードも公開したコンペ結果の報告論文。
- [SIGNATE「SUBARU 画像認識チャレンジ」データセット・結果報告論文](https://arxiv.org/abs/2204.12717): 運転支援システム「アイサイト」の走行中画像から先行車速度を推論するコンペの報告書。
- [Kaggle「LANL Earthquake Prediction」開催に関する論文](https://www.pnas.org/content/118/5/e2011362118): 優勝チームの意外な戦略や、コンペ開催の意義に言及する論文。
- [Kaggle「PANDA Challenge」の成果を報告するNature Medicine掲載論文](https://www.wouterbulten.nl/blog/tech/panda-challenge/): 課題の背景やコンペ上位解法を紹介する論文。
- [SIGNATE「熱帯低気圧（台風等）検出アルゴリズム作成」コンペのまとめ論文](https://progearthplanetsci.springeropen.com/articles/10.1186/s40645-021-00459-y): 海洋研究開発機構主催コンペを通じた性能向上を報告する論文。
- [Deep learning models for predicting RNA degradation via dual crowdsourcing](https://www.nature.com/articles/s42256-022-00571-8): Kaggle「OpenVaccine」の成果と得られた知見をまとめた Nature Machine Intelligence 掲載論文。
- [Analysis of the Human Protein Atlas Weakly Supervised Single-Cell Classification competition](https://www.nature.com/articles/s41592-022-01606-z): コンペの設計と結果を報告する論文。
- [チューニングコンペティション（LLM-jp）開催報告](https://drive.google.com/file/d/1M1bpEDvARxSq-KNbudf1B8V4kbpYxO5u/view): 言語処理学会第 31 回年次大会のワークショップ内で開催された LLM チューニングコンペの開催報告。

### プラットフォーム運営者の視点

- [【募集案内】人工知能学会コンペティション開催支援制度募集要領](https://www.ai-gakkai.or.jp/event/ai-seminar/competition_convening_support/): 最大 100 万円の助成でコンペ開催を支援する学会制度。
- [データサイエンスコンテストを開催するときに考えること](https://qiita.com/torumitsutake/items/c4998e455f76808a63a7): Solafune 運営者による開催側視点の検討事項まとめ。
- [Nishika「判例の個人情報の自動マスキング」コンペ運営振り返り記事](https://note.com/nishika_inc/n/n78447a423abe): 開催の背景・上位解法・固有表現抽出データセット作りの過程を紹介。
- [Nishikaによる「データサイエンスコンペ」紹介記事（運営視点）](https://note.com/nishika_inc/n/n473a6c4a6a07): コンペのメリットと情報保護上の懸念を運営目線で解説。

## 関連概念

- [コンペプラットフォーム](../../platform.md) / [性能評価と検証](./evaluation-validation.md)
