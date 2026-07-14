# コンペ形式・技術動向の変遷

Kaggle のコンペは、表データ・GBDT を中心とした時代から、画像・自然言語処理の深層学習化、コード提出形式の定着を経て、直近では LLM エージェントと対戦型コンペがプラットフォームの中心機能になりつつあります。
本ページは各データ種別・技術動向系のページを横断する時系列の見取り図です（本リンク集は Weekly Kaggle News のアーカイブが始まる 2019 年末以降を主にカバーするため、それ以前の記述は一般的な文脈情報として扱っています）。

## 押さえどころ

- 表データ・GBDT はコンペの共通言語として今も生き続けている。Titanic の後継として月次開催された Tabular Playground Series がその象徴で、初学者の入口という役割は形を変えて続いている
- 2019〜2021 年にかけて、[表データコンペ](./tabular.md)と並走する形で[画像認識コンペ](./image-recognition.md)・[自然言語処理コンペ](./nlp-llm.md)が本格的な柱になった。同時期に「学習済みモデルと推論コードをノートブックとして提出する」[コードコンペティション](./code-competition.md)形式の導入が進み、実行時間制限・オフライン実行という制約が戦い方を変えた
- 「値の予測」ではなく「エージェントを提出して対戦する」Simulation Competitions は、実は 2018〜2021 年の Halite・Connect X・Lux AI・Hungry Geese の頃から存在する古参の形式。この時期はまだ強化学習中心の一分野という位置づけだった（[エージェント対戦コンペ](./agent-competition.md)）
- 2022〜2023 年は表・画像・NLP のどれが主流とも言えない並走期。[表データコンペ](./tabular.md)では「深層学習 vs 決定木」論争が続く一方、NLP 側では LLM によるデータ生成・水増しが精度向上の主要な手段として台頭し始めた
- 2023〜2025 年で LLM が戦い方そのものに入り込んだ。NLP コンペはエンコーダ型（BERT・DeBERTa 系）からデコーダ型 LLM への移行が明確になり、同時に AI コーディングエージェントが「惨敗」（2023 年、ChatGPT Code Interpreter）から「上位 30%」（2025 年、Claude Code）へとわずか 2 年で実用性を急速に高めた（[AI エージェント活用](./ai-agent.md)）
- 2025〜2026 年、初期の Simulation Competitions の系譜が新しい意味を持ち始めている。公式ゲームエンジン提供の大型対戦コンペや、Kaggle 自身が運営するモデル評価基盤「Game Arena」の登場により、対戦型コンペは実験的な一形式から、フロンティアモデルを評価する中心的な仕組みへと役割を広げた（[性能評価と検証](./evaluation-validation.md)も参照）
- 「その年に何が話題だったか」を振り返るアンケート・年次まとめ記事が 2020 年以降ほぼ毎年蓄積されており、技術動向を定点観測する材料になっている

## 資料

### 表データ時代の名残・共通の入口

- [「Tabular Playground Series」の紹介記事](https://towardsdatascience.com/progressively-approaching-kaggle-f58db71a42a9?gi=32e36ede2a44): Titanic に代わる月次開催の練習用コンペを紹介する記事。
- [Tabular Playground Series 2021年4月分開始](https://www.kaggle.com/c/tabular-playground-series-apr-2021/): Titanic データに GAN を用いて生成したデータセットを使用。
- [BigQuery上の機械学習機能「BQML」の検証資料](https://speakerdeck.com/shimacos/bqmlkotohazime): Kaggle「Otto Group Product Classification Challenge」のデータを用いた検証結果。

### 深層学習化とコード提出形式の定着（2019〜2021年）

- [2010年以降のコンピュータビジョン分野の動向まとめ記事](https://gihyo.jp/dev/column/newyear/2021/computer-vision-trends): 深層学習による画像認識コンペの革新から近年の潮流までを解説。
- [「Code Competitions」形式のTipsまとめ記事](https://nonbiri-tereka.hatenablog.com/entry/2020/09/03/091530): 多くのコンペで導入が進む開催形式の攻略 Tips。
- [「Halite」AIコンペからの知見まとめ記事（2018年）](https://www.twosigma.com/insights/article/best-practices-from-building-a-machine-learning-bot-for-halite/): 「強化学習が必ずしも最良ではない」など至言をまとめた記事。
- [Kaggle「Halite by Two Sigma」強化学習体験談](https://threecourse.hatenablog.com/entry/2020/09/17/014155): ルールベースに対する難しさなどの所感を語る記事。

### 年次まとめ・定点観測

- [2020年の面白かったコンペ・論文に関する9人のKagglerアンケート記事](https://sorabatake.jp/18734/): 2020 年を振り返るアンケート結果のまとめ記事。
- [2021年の面白かったコンペと論文を7人のKagglerに調査した記事](https://sorabatake.jp/26199/): 回答者のコメントも併記した調査記事。
- [2022年時点での機械学習コンペの動向をまとめた記事](https://medium.com/machine-learning-insights/winning-approach-ml-competition-2022-b89ec512b1bb): プログラミング言語・上位解法アプローチ・利用ライブラリなどを可視化した記事。
- [Kaggleランカーの5人に聞いた、2023年面白かったコンペ5選と論文5選](https://sorabatake.jp/37130/): Grandmaster・Master 5 人へのアンケートをまとめた記事。
- [直近3年間のKaggle優勝解法を分析した記事](https://www.datarobot.com/jp/blog/is-deep-learning-almighty/): 非構造化データはディープラーニング、テーブルデータは勾配ブースティングという傾向を分析。
- [The State of Machine Learning Competitions 2025 Edition](https://mlcontests.com/state-of-machine-learning-competitions-2025/): 対戦トーナメント形式の導入を含む 2025 年のコンペ動向の年次まとめ。

### LLM・エージェントの主役化（2023〜2025年）

- [データコンペでCode Interpreter片手に戦ってみたけど惨敗でした](https://zenn.dev/karaage0703/articles/1fa0a14d4cdd63): ChatGPT の Code Interpreter でコミュニティコンペに挑んだ 2023 年の初期事例。
- [Claude Code と Kaggle をやったら何も考えずに上位30%になれた話](https://zenn.dev/genda_jp/articles/20250909_kaggle_with_claude_code): エージェントに任せた場合の到達点と限界、MLflow・GitHub を使った協働体制の実験報告。
- [Agent時代のKaggleで、人間は何を見るべきか (関西kaggler会 2026.5.22)](https://speakerdeck.com/chihironakayama/agentshi-dai-nokagglede-ren-jian-hahe-wojian-rubekika-guan-xi-kagglerhui-2026-dot-5-22): エージェントによるコーディングが普及した時代の Kaggle の変化と人間の役割を論じる発表資料。

### 対戦型・評価基盤としての定着（2025〜2026年）

- [The Pokémon Company - PTCG AI Battle Challenge Simulation](https://www.kaggle.com/competitions/pokemon-tcg-ai-battle): ポケモンカードゲームの対戦 AI を競う大型コンペ（Simulation Track）。
- [Kaggle Game Arena evaluates AI models through games](https://blog.google/innovation-and-ai/products/kaggle-game-arena/): モデル同士をゲームで対戦させる評価基盤 Game Arena の公式発表。
- [Game Arena: Poker and Werewolf, and Gemini 3 tops chess](https://blog.google/innovation-and-ai/models-and-research/google-deepmind/kaggle-game-arena-updates/): ポーカー・人狼ベンチマークの追加とチェストーナメント結果の続報。
- [AtCoder World Tour Finals 2025 に OpenAI がスポンサーとして参画](https://prtimes.jp/main/html/rd/p/000000059.000028415.html): 「人間 vs AI」のエキシビションが行われた競技プログラミングイベントの発表。

## 関連概念

- [表データコンペ](./tabular.md) / [画像認識コンペ](./image-recognition.md) / [自然言語処理コンペ](./nlp-llm.md) / [コードコンペティション](./code-competition.md) / [エージェント対戦コンペ](./agent-competition.md) / [AI エージェント活用](./ai-agent.md) / [性能評価と検証](./evaluation-validation.md)
