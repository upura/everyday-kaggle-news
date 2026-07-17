# 操作ログ

LLM Wiki としての操作履歴です（新しいものが上）。

- 2026-07-17 restructure: 管理者の依頼により一覧ページ「[コンペ開催カレンダー](../calendar.md)」を新設。GitHub Actions の update-competitions ワークフロー（毎日 06:00 JST、`tools/fetch_competitions.py`）が Kaggle API から開催中のメダル対象コンペ（awardsPoints が真のもの）を取得して `docs/competitions.json` を更新し、`docs/calendar.md` がカテゴリ別の色分け・絞り込み・ツールチップ・表形式ビュー付きのタイムラインで表示する。締切が 400 日以上先のコンペは「常設・長期開催」として分離して表示。README.md の目次（「情報収集・コミュニティ」）と [最新情報の確認](../recent.md) の「コンペの開催情報」に導線を追加。稼働にはリポジトリシークレット KAGGLE_API_TOKEN（従来形式の KAGGLE_USERNAME / KAGGLE_KEY でも可）の設定が必要
- 2026-07-16 restructure: `docs/quickstart.md` に新セクション「話題別の学び方ガイド」を追加。表データ・画像認識・自然言語処理・LLM・時系列予測・音声・グラフ・推薦・数理最適化・エージェント対戦の9話題について、対応する概念ページと最初に読むべき入門資料1本を案内する導線を新設した。初学者が「Titanicの先」で興味のある話題を選んだ後、迷わず該当概念ページの「押さえどころ」「入門・基礎」に進めるようにする狙い。データ種別によらず共通する土台（実験管理・環境構築・性能評価と検証・コードコンペティション）と心構えページへの案内も追加。既存の「定番資料」節・他のセクションは変更していない
- 2026-07-14 ingest: 新規概念ページ「[コンペ形式・技術動向の変遷](./concepts/competition-evolution.md)」を新設（資料18件、4つの `###` 小見出しに整理）。表データ・GBDT 中心の時代から、画像・NLP の深層学習化とコード提出形式の定着、LLM・エージェントの主役化、対戦型コンペの評価基盤化までを横断する時系列の見取り図として作成。既存の[表データコンペ](./concepts/tabular.md)・[画像認識コンペ](./concepts/image-recognition.md)・[自然言語処理コンペ](./concepts/nlp-llm.md)・[コードコンペティション](./concepts/code-competition.md)・[エージェント対戦コンペ](./concepts/agent-competition.md)・[AI エージェント活用](./concepts/ai-agent.md)・[性能評価と検証](./concepts/evaluation-validation.md)の各ページから資料・洞察を再構成したもので、新規の資料発掘はしていない。上記7ページの「関連概念」に本ページへの相互リンクを追加。README.md の目次（「技術動向」見出し）・最近の更新を更新
- 2026-07-14 restructure: Weekly Kaggle News 全号（#1〜#343）のバックフィルが完了し資料が出揃ったことを受け、全19本の概念ページの「押さえどころ」を推敲。各ページの資料欄（タイトル・注釈）を通読し、資料が少なかった時期に書かれたまま更新されていなかった記述や、複数ソースを横断すれば読み取れるのに反映されていなかった時系列的な変化・定番パターンを補強した（例: tabular.md の GPU 高速化・Target Encoding の系譜、nlp-llm-trends.md の日本語モデルの担い手の変遷、pytorch.md の Optimizer 系譜、graph.md の学習リソース拡充など）。「資料」欄・「関連概念」欄・ページ構成（見出し）は一切変更していない。特定資料に強く依存する主張には資料へのリンクを付与し、事実の捏造は行っていない
- 2026-07-14 lint: サイト全体監査で見つかった 3 件に対応。(1) `.claude/skills/lint/SKILL.md` の検査項目リストが `tools/verify_wiki.py` に追加済みの検査6〜8（solutions.md 競技名重複・URL重複・未エスケープパイプ検出）を反映していなかったため追記。(2) `docs/service.md` が概念マップ上で孤立（接続数0）していたため、environment.md（開発ツール文脈）・ai-agent.md（コーディングエージェント向けプラグイン文脈）・mindset.md（コミュニティ文脈）の「関連概念」にリンクを追加。(3) `.github/workflows/monthly-linkcheck.yml` に job レベルの `timeout-minutes: 90` を追加（リンク総数の増加に伴う実行時間肥大化への備え）
- 2026-07-14 restructure: README.md の目次を再構成。「実践・定跡（コンペのタスク別）」と「一般的な研究・モデル動向」が同じ見出しに混在していた点を解消するため、[画像認識・視覚モデルの技術動向](./concepts/image-recognition-trends.md)・[LLM・自然言語処理の技術動向](./concepts/nlp-llm-trends.md) の 2 ページを「### データ種別・タスク」から独立した新見出し「### 技術動向」へ移動。また 1 ページのみで独立していた「### コンペの開催」見出しを廃止し、[コンペ開催](./concepts/competition-hosting.md) を「### 情報収集・コミュニティ」へ統合（開催側の知見はコンペ選定・エコシステムの情報という点で platform.md・events.md と性質が近いと判断）。ページ本体・エントリは変更していない。`docs/concept-map.md` の `GROUPS`／`COLORS` 配列を新しい見出し構成に合わせて更新（`docs/graph.json` はビルド時に `tools/build_graph_data.py` が README.md から再生成するため、スクリプト自体の変更は不要）。将来的に他ページ（tabular など）が分割された場合も「### 技術動向」を受け皿にできる
- 2026-07-14 restructure: 資料件数が突出していた nlp-llm.md（213件）と image-recognition.md（145件）を、実践・定跡ページと技術動向ページに分割。nlp-llm.md は「入門・基礎」「コンペの定跡」（92件）を維持し、「モデル・技術動向」「日本語モデル・リソース」「ライブラリ・ツール」「研究動向・サーベイ・イベント」（120件）を新設の [LLM・自然言語処理の技術動向](./concepts/nlp-llm-trends.md) へ移設。image-recognition.md は「入門・基礎」「コンペの定跡」（24件）を維持し、「Vision Transformer・Transformer動向」「CLIP・マルチモーダル」「自己教師あり学習」「国際会議サーベイ・参加報告」「モデル・技術動向」（120件）を新設の [画像認識・視覚モデルの技術動向](./concepts/image-recognition-trends.md) へ移設。既存の `###` 小見出しをそのまま新ページへ移すのみで、資料エントリの文言・URL・注釈は変更していない（移設前後で URL 集合の一致を確認）。両新ページとも README.md の「### データ種別・タスク」に追記（カテゴリ自体は変更していないため `docs/concept-map.md` の `GROUPS` 配列・`tools/build_graph_data.py` の変更は不要）。他の概念ページ（tabular・competition-hosting など）は各小見出しが 30 件以下に収まっており、今回は分割対象から除外
- 2026-07-14 restructure: 監査で判明した「資料 15 件超・見出しなし」の概念ページ 13 本（image-recognition・tabular・pytorch・environment・mindset・competition-hosting・evaluation-validation・time-series・agent-competition・optimization・recommendation・audio・experiment-management は既存見出しを維持）に `###` 小見出しを追加して整理（nlp-llm.md は別コミットで先行対応済み）。全て機械的な並べ替えのみで、既存の資料エントリの文言・URL・注釈は一切変更していない（各ページで整理前後の項目数を比較し一致を確認）。nlp-llm.md（212件→6見出し）と image-recognition.md（144件→7見出し）は依然として資料件数が多く、将来的に複数ページへの分割も検討の余地がある

- 2026-07-14 lint: 監査で見つかった重複を解消。solutions.md の「RecSys Challenge 2020」div を「RecSys Challenge」div に統合。ai-agent・audio・experiment-management・agent-competition・optimization・mindset の各概念ページに残っていた solutions.md との重複エントリ計 6 件を削除（解法・参加録は solutions.md に一元化）。competition-hosting.md の開催論文と重複していた G2Net の論文リンクを solutions.md 側から削除。`tools/verify_wiki.py` に検査を3件追加: solutions.md 内の競技名(h3)重複検出、solutions.md と他ページの URL 重複検出、リスト項目内の未エスケープパイプ文字検出（kramdown がテーブルと誤解釈する問題の再発防止）

- 2026-07-14 restructure: 概念ページ「学会コンペ」を廃止。解法・参加録 23 件は `docs/solutions.md` へ移設（既存の AI王 div に 4 件追記、新設した KDD Cup / HuMob Challenge / 2COOOL の各 div と既存の汎用「学会コンペ」div に集約）、コンペ開催論文・開催報告 3 件は [コンペ開催](./concepts/competition-hosting.md) へ、残る概説・プロジェクトページ・開催告知 11 件は [コンペプラットフォーム](../platform.md) の新設セクション「学会併設コンペ」へ統合。重複していたエントリ 1 件は除去。README.md の目次・関連概念のリンクを更新

- 2026-07-14 ingest: WKN #1〜#9（9 号、並列取得バッチ処理）→ 新規 33 件。solutions.md に div 1 新設（Santa's Workshop Tour 2019）、既存の WiDS Datathon 2020 div に追記。nlp-llm ×8、tabular ×7、pytorch ×4、image-recognition ×4、evaluation-validation ×2、milestones ×5、optimization ×2、mindset ×3、service.md ×2、events ×2、environment ×2、graph ×2、experiment-management ×1 に配分。これで WKN 全号（#1〜#343）のバックフィルが完了
- 2026-07-14 ingest: WKN #10〜#24（15 号、並列取得バッチ処理）→ 新規 78 件。solutions.md に div 2 新設（Google QUEST Q&A Labeling / WiDS Datathon 2020）、既存の 2019 Data Science Bowl・SIGNATE・Nishika 各 div に追記。nlp-llm ×14、tabular ×15、image-recognition ×5、pytorch ×3、evaluation-validation ×7、optimization ×5、milestones ×8、mindset ×5、events ×2、environment ×2、time-series ×3、agent-competition ×1、graph ×1、competition-hosting ×3、service.md ×2、experiment-management ×1 に配分
- 2026-07-14 ingest: WKN #25〜#39（15 号、並列取得バッチ処理）→ 新規 114 件。抽出時に発見した URL/注釈の不一致（旧形式パーサの段落誤対応）1 件は誤情報として除外。solutions.md に div 9 新設（SIIM-ISIC Melanoma Classification / 第4回FUJIFILM Brain(s)コンテスト / TReNDS Neuroimaging / NFL Big Data Bowl / M5 Forecasting - Uncertainty / Accuracy / Deepfake Detection Challenge / iMet Collection 2020 - FGVC7 / Open Images 2019 - Object Detection / University of Liverpool - Ion Switching）、既存の Tweet Sentiment Extraction・Basketball Behavior Challenge・Abstraction and Reasoning Challenge・PANDA Challenge・SIGNATE 各 div に追記。nlp-llm ×16、tabular ×16、pytorch ×10、events ×8、milestones ×7、mindset ×7、image-recognition ×9、evaluation-validation ×3、code-competition ×1、recommendation ×2、time-series ×3、books.md ×3、quickstart.md ×3、service.md ×6、environment ×8、agent-competition ×3、competition-hosting ×3、experiment-management ×3、audio ×1、platform.md ×1 に配分
- 2026-07-14 ingest: WKN #40〜#54（15 号、並列取得バッチ処理）→ 新規 139 件。号 #40 はスラッグが `weekly-kaggle-issue-40-20-09-18`（「news」を含まない）である点を確認。solutions.md に div 11 新設（CDP - Unlocking Climate Solutions / Black-Box Optimization Challenge / OSIC Pulmonary Fibrosis Progression / Bengali.AI Handwritten Grapheme Classification / Basketball Behavior Challenge: BBC2020 / RSNA STR Pulmonary Embolism Detection / 2019 Data Science Bowl / Abstraction and Reasoning Challenge / RecSys Challenge 2020 / Prostate cANcer graDe Assessment (PANDA) Challenge / Cornell Birdcall Identification）、既存の MoA・OpenVaccine・Tweet Sentiment Extraction・SIGNATE・atmaCup 各 div に追記。nlp-llm ×13、tabular ×21、pytorch ×19、image-recognition ×10、events ×10、milestones ×12、audio ×5、books.md ×5、service.md ×9、optimization ×6、mindset ×3、competition-hosting ×3、agent-competition ×7、academic-competition ×3、evaluation-validation ×3、environment ×9、recommendation ×2、experiment-management ×4、quickstart.md ×6、platform.md ×2、time-series ×1 に配分
- 2026-07-14 ingest: WKN #55〜#69（15 号、並列取得バッチ処理）→ 新規 133 件（同一告知の重複 2 件はスキップ）。solutions.md に div 6 つ新設（Rainforest Connection Species Audio Detection / Lyft Motion Prediction for Autonomous Vehicles / Riiid! Answer Correctness Prediction / NFL 1st and Future - Impact Detection / IEEE-CIS Fraud Detection / OpenVaccine: COVID-19 mRNA Vaccine Degradation Prediction）、既存の MoA・SIGNATE・ProbSpace・atmaCup 各 div に追記。nlp-llm ×16、tabular ×22、pytorch ×10、experiment-management ×9、events ×12、milestones ×10、environment ×8、image-recognition ×8、academic-competition ×2、competition-hosting ×4、recommendation ×2、optimization ×3、graph ×2、evaluation-validation ×2、books.md ×3、agent-competition ×1、mindset ×3、platform.md ×2、service.md ×2、quickstart.md ×1、time-series ×4 に配分
- 2026-07-14 ingest: WKN #70〜#84（15 号、並列取得バッチ処理）→ 新規 102 件（Kaggle 求人募集など資料性の低い告知 1 件はスキップ）。solutions.md に div 6 つ新設（BirdCLEF 2021 / Shopee - Price Match Guarantee / Bristol-Myers Squibb – Molecular Translation / Coleridge Initiative - Show US the Data / Indoor Location & Navigation / ProbSpace「論文の被引用数予測」）、既存の AI王・SIGNATE・MLB 各 div に追記。nlp-llm ×15、image-recognition ×12、pytorch ×12、events ×14、tabular ×7、milestones ×4、recommendation ×6、evaluation-validation ×3、academic-competition ×3、agent-competition ×2、mindset ×2、experiment-management ×2、graph ×2、audio ×1、environment ×1、service.md ×2、platform.md ×2、quickstart.md ×1 に配分
- 2026-07-14 ingest: WKN #85〜#99（15 号、並列取得バッチ処理）→ 新規 92 件（同一内容の重複告知・時限性の初心者向けコンペ開始告知など計 4 件はスキップ）。アーカイブ全体を確認し、WKN が号 #1（2019-12-20）まで遡れることを確認（号 #40 のみスラッグが `weekly-kaggle-issue-40-...` 形式で「news」を含まない）。solutions.md に div 10 新設（Google Landmark Retrieval 2021 / Google Landmark Recognition 2021 / G2Net Gravitational Wave Detection / SETI Breakthrough Listen / Google Smartphone Decimeter Challenge / CommonLit Readability Prize / SIIM-FISABIO-RSNA COVID-19 Detection / MLB Player Digital Engagement Forecasting / #SwipeToSuccess）、既存の Solafune・SIGNATE 各 div に追記。nlp-llm ×12、image-recognition ×10、events ×13、milestones ×7、mindset ×4、pytorch ×5、tabular ×7、evaluation-validation ×4、environment ×5、recommendation ×2、academic-competition ×3、competition-hosting ×3、agent-competition ×1、graph ×1、code-competition ×1、audio ×1、optimization ×1、experiment-management ×3、service.md ×1、books.md ×1 に配分
- 2026-07-14 ingest: WKN #100〜#112（13 号、並列取得バッチ処理）→ 新規 94 件（Kaggle との関連が薄いプログラミング教育調査記事 1 件はスキップ）。solutions.md に div 9 つ新設（G-Research Crypto Forecasting / Sartorius - Cell Instance Segmentation / PetFinder.my - Pawpularity Contest / NFL Health & Safety - Helmet Assignment / Google Brain - Ventilator Pressure Prediction / chaii - Hindi and Tamil Question Answering / Nishika 小説家になろう ブクマ数予測 / エンジニアの年収予測 / Facebook AI Image Similarity Challenge）、既存の atmaCup・Solafune 各 div に追記。nlp-llm ×20、image-recognition ×13、solutions.md（新設含む）×19、milestones ×9、environment ×9、tabular ×7、events ×6、agent-competition ×7、pytorch ×4、recommendation ×4、audio ×4、competition-hosting ×3、evaluation-validation ×2、optimization ×2、time-series ×2、experiment-management ×1、code-competition ×1、service.md ×2、quickstart.md ×2、graph ×1、mindset ×1 に配分。これで WKN #100 まで遡及し、バックフィルの目標範囲を完了
- 2026-07-14 ingest: WKN #113〜#126（14 号、並列取得バッチ処理）→ 新規 62 件（他媒体で同一内容と判断した対談記事 1 件、時限性の他プラットフォームコンペ告知・入門講義資料など計 3 件はスキップ）。solutions.md に div 3 つ新設（Feedback Prize - Evaluating Student Writing / Happywhale - Whale and Dolphin Identification）、既存の NBME・Jigsaw・JPX・ProbSpace・Solafune 各 div に追記。nlp-llm ×15、image-recognition ×10、tabular ×7、events ×7、mindset ×4、environment ×3、competition-hosting ×3、academic-competition ×1、recommendation ×2、pytorch ×3、audio ×1、optimization ×1、agent-competition ×1、time-series ×1 に配分
- 2026-07-14 ingest: WKN #127〜#141（15 号、並列取得バッチ処理）→ 新規 67 件（時限性のコンペ開始告知・登録締切案内・資本提携ニュース 6 件はスキップ）。solutions.md に div 3 つ新設（Foursquare - Location Matching / Image Matching Challenge 2022 / BirdCLEF 2022）、既存の NBME・USPPPM・H&M・JPX・Nishika 各 div に解法・参加録を追記。nlp-llm ×17、image-recognition ×13、milestones ×5、events ×3、academic-competition ×3、mindset ×2、competition-hosting ×2、optimization ×1、tabular ×2、time-series ×1、graph ×2、agent-competition ×1、service.md ×1 に配分
- 2026-07-14 ingest: WKN #142〜#156（15 号、並列取得バッチ処理）→ 新規 68 件。solutions.md に div 6 つ新設（Mayo Clinic STRIP AI / Feedback Prize Effectiveness / Great Barrier Reef / Nishika 生鮮野菜 / Nishika ボケてコンペ / TPS May 2022）、JPX に追記。nlp-llm ×11、milestones ×9、events ×10、image-recognition ×8、environment ×7、mindset ×5、academic-competition ×5、time-series ×3、tabular ×3、competition-hosting ×4、evaluation-validation ×2、recommendation ×1、optimization ×1、experiment-management ×1 に配分。この時期の号（#147 以前）は HTML が blockquote 形式でなくなるため、抽出スクリプトに旧形式（段落直下のリンク＋直後の段落説明）へのフォールバックを追加した

- 2026-07-14 ingest: WKN #157 → 新規 9 件（solutions.md ×1（div）/ concepts/nlp-llm ×4, recommendation ×2, optimization ×1, experiment-management ×1, tabular ×1, milestones ×1, academic-competition ×1）
- 2026-07-14 ingest: WKN #158 → 新規 5 件（solutions.md ×2（div 新設）/ concepts/tabular, optimization / concepts/competition-hosting）
- 2026-07-14 ingest: WKN #159 → 新規 3 件（concepts/tabular, image-recognition, time-series）
- 2026-07-14 ingest: WKN #160 → 新規 2 件（concepts/nlp-llm / milestones.md）
- 注: 号 #160 のスラッグが weekly-kaggle-news-issue-160-22-12-31 に変更されているのを確認（同名の号が 2 件存在するため slug が特殊化）

- 2026-07-14 ingest: WKN #161 → 新規 3 件（concepts/nlp-llm ×2 / milestones.md）
- 2026-07-14 ingest: WKN #162 → 新規 4 件（concepts/tabular, pytorch, mindset / events.md）
- 2026-07-14 ingest: WKN #163 → 新規 4 件（solutions.md / concepts/nlp-llm, academic-competition, tabular）

- 2026-07-14 ingest: WKN #164 → 新規 2 件（concepts/image-recognition, nlp-llm）
- 2026-07-14 ingest: WKN #165 → 新規 2 件（solutions.md / concepts/tabular）
- 2026-07-14 ingest: WKN #166 → 新規 4 件（concepts/nlp-llm ×2, mindset / events.md）

- 2026-07-14 ingest: WKN #167 → 新規 2 件（concepts/nlp-llm, environment）。ChatGPT チャレンジ開催告知は時限性のためスキップ
- 2026-07-14 ingest: WKN #168 → 新規 4 件（concepts/tabular, environment, recommendation / milestones.md）
- 2026-07-14 ingest: WKN #169 → 新規 3 件（concepts/tabular, optimization / events.md）

- 2026-07-13 ingest: WKN #170 → 新規 2 件（milestones.md / concepts/pytorch）。併設コンペの開催告知 1 件はスキップ
- 2026-07-13 ingest: WKN #171 → 新規 3 件（concepts/experiment-management, nlp-llm, environment）
- 2026-07-13 ingest: WKN #172 → 新規 3 件（solutions.md / concepts/recommendation, agent-competition）

- 2026-07-13 ingest: WKN #173 → 新規 3 件（concepts/image-recognition, competition-hosting, recommendation）
- 2026-07-13 ingest: WKN #174 → 新規 3 件（solutions.md ×2 / concepts/tabular）
- 2026-07-13 ingest: WKN #175 → 新規 2 件（events.md / concepts/nlp-llm）

- 2026-07-13 ingest: WKN #176 → 新規 3 件（solutions.md、Solafune 超解像の div 新設 / milestones.md / concepts/tabular）
- 2026-07-13 ingest: WKN #177 → 新規 4 件（solutions.md ×2、ASL / LECR の div 新設 / concepts/agent-competition）
- 2026-07-13 ingest: WKN #178 → 新規 4 件（concepts/environment, nlp-llm ×2, image-recognition）

- 2026-07-13 ingest: WKN #179 → 新規 3 件（solutions.md / concepts/nlp-llm ×2）
- 2026-07-13 ingest: WKN #180 → 新規 3 件（solutions.md、Stable Diffusion I2P の div 新設 / concepts/academic-competition, nlp-llm）
- 2026-07-13 ingest: WKN #181 → 新規 3 件（solutions.md / concepts/environment, pytorch）

- 2026-07-13 ingest: WKN #182 → 新規 6 件（solutions.md / milestones.md / concepts/image-recognition, pytorch, nlp-llm, tabular）
- 2026-07-13 ingest: WKN #183 → 新規 5 件（milestones.md / events.md / concepts/nlp-llm, image-recognition, environment）
- 2026-07-13 ingest: WKN #184 → 新規 1 件（concepts/tabular）。開催告知 2 件はスキップ

- 2026-07-13 ingest: WKN #185 → 新規 2 件（solutions.md、IMC2023 の div 新設 / concepts/environment）
- 2026-07-13 ingest: WKN #186 → 新規 3 件（solutions.md、PSP の div 新設 / concepts/nlp-llm, time-series）
- 2026-07-13 ingest: WKN #187 → 新規 7 件（recent.md / events.md / concepts/graph, nlp-llm ×3, pytorch）。Keras Core は後継の Keras 3.0 既掲載のためスキップ

- 2026-07-13 ingest: WKN #188 → 新規 4 件（solutions.md、Vesuvius Ink Detection の div 新設 / concepts/tabular, nlp-llm, image-recognition）
- 2026-07-13 ingest: WKN #189 → 新規 3 件（milestones.md / concepts/environment, experiment-management）。ドキュメント多言語化のニュース 1 件はスキップ
- 2026-07-13 ingest: WKN #190 → 新規 2 件（events.md / concepts/ai-agent）

- 2026-07-13 ingest: WKN #191 → 新規 4 件（solutions.md ×2、#15 atmaCup の div 新設 / platform.md / concepts/nlp-llm）
- 2026-07-13 ingest: WKN #192 → 新規 4 件（solutions.md ×2、ICR の div 新設 / milestones.md / concepts/nlp-llm）
- 2026-07-13 ingest: WKN #193 → 新規 2 件（concepts/environment, academic-competition）

- 2026-07-13 ingest: WKN #194 → 新規 1 件（concepts/nlp-llm）。既掲載書籍の URL 変種 1 件はスキップ
- 2026-07-13 ingest: WKN #195 → 新規 3 件（solutions.md / milestones.md / concepts/academic-competition）
- 2026-07-13 ingest: WKN #196 → 新規 4 件（solutions.md、飛行機雲コンペの div 新設 / concepts/tabular ×2, nlp-llm）

- 2026-07-13 ingest: WKN #197 → 新規 2 件（solutions.md / concepts/pytorch）
- 2026-07-13 ingest: WKN #198 → 新規 2 件（concepts/time-series, nlp-llm）
- 2026-07-13 ingest: WKN #199 → 新規 5 件（concepts/academic-competition ×2, competition-hosting, optimization, pytorch）

- 2026-07-13 ingest: WKN #200 → 新規 3 件（events.md / milestones.md / concepts/image-recognition）
- 2026-07-13 ingest: WKN #201 → 新規 5 件（solutions.md ×4 / concepts/competition-hosting）
- 2026-07-13 ingest: WKN #202 → 新規 3 件（solutions.md、RSNA 2023 Abdominal の div 新設 / concepts/evaluation-validation, competition-hosting）

- 2026-07-13 ingest: WKN #203 → 新規 1 件（concepts/audio）。既掲載シリーズの告知と初学者体験記はスキップ
- 2026-07-13 ingest: WKN #204 → 新規 2 件（concepts/nlp-llm, evaluation-validation）
- 2026-07-13 ingest: WKN #205 → 新規 2 件（concepts/image-recognition, nlp-llm）。既掲載シリーズの個別回はスキップ

- 2026-07-12 ingest: WKN #206 → 新規 1 件（concepts/tabular）。既掲載シリーズの個別回と書籍セール告知はスキップ
- 2026-07-12 ingest: WKN #207 → 新規 5 件（solutions.md / events.md / concepts/pytorch, agent-competition, academic-competition）
- 2026-07-12 ingest: WKN #208 → 新規 1 件（solutions.md）。既掲載書籍の URL 変種 1 件はスキップ

- 2026-07-12 ingest: WKN #209 → 新規 3 件（solutions.md / milestones.md / concepts/pytorch）
- 2026-07-12 ingest: WKN #210 → 新規 1 件（concepts/nlp-llm）
- 2026-07-12 ingest: WKN #211 → 新規 5 件（solutions.md ×2、Bengali.AI / Ribonanza の div 新設 / events.md / concepts/evaluation-validation, nlp-llm）。入門まとめの旧版 1 件は新版既掲載のためスキップ

- 2026-07-12 ingest: WKN #212 → 新規 2 件（concepts/nlp-llm, image-recognition）。書籍セールの告知 1 件は時限性のためスキップ
- 2026-07-12 ingest: WKN #213 → 新規 5 件（solutions.md / milestones.md / concepts/time-series, pytorch, nlp-llm）
- 2026-07-12 ingest: WKN #214 → 新規 1 件（concepts/tabular）
- 2026-07-12 ingest: WKN #215 → 新規 5 件（solutions.md ×4 / concepts/recommendation, nlp-llm ×2）。講演ページの URL 変種 1 件はスキップ

- 2026-07-12 ingest: WKN #216 → 新規 4 件（solutions.md / milestones.md / concepts/image-recognition ×2）
- 2026-07-12 ingest: WKN #217 → 新規 5 件（solutions.md ×2、DAIGT の div 新設 / events.md / concepts/experiment-management, image-recognition）
- 2026-07-12 ingest: WKN #218 → 新規 3 件（solutions.md、SenNet+HOA の div 新設 / concepts/image-recognition, academic-competition）

- 2026-07-12 ingest: WKN #219 → 新規 1 件（concepts/competition-hosting）
- 2026-07-12 ingest: WKN #220 → 新規 1 件（concepts/competition-hosting）
- 2026-07-12 ingest: WKN #221 → 新規 4 件（solutions.md、Solafune 太陽光パネルの div 新設 / concepts/mindset, nlp-llm, tabular）
- 2026-07-12 ingest: WKN #222 → 新規 4 件（milestones.md / events.md / concepts/audio, environment）。GPU 抽選企画の告知 1 件はスキップ

- 2026-07-12 ingest: WKN #223 → 新規 1 件（solutions.md、BirdCLEF 2023 の div 新設）
- 2026-07-12 ingest: WKN #224 → 新規 2 件（concepts/mindset, tabular）
- 2026-07-12 ingest: WKN #225 → 新規 2 件（concepts/tabular ×2）。日本代表募集の告知 1 件はスキップ

- 2026-07-12 ingest: WKN #226 → 新規 3 件（events.md / concepts/experiment-management, image-recognition）
- 2026-07-12 ingest: WKN #227 → 新規 3 件（milestones.md / concepts/audio, nlp-llm）
- 2026-07-12 ingest: WKN #228 → 新規 4 件（solutions.md / events.md / concepts/image-recognition, mindset）

- 2026-07-12 ingest: WKN #229 → 新規 3 件（events.md / concepts/nlp-llm, graph）
- 2026-07-12 ingest: WKN #230 → 新規 1 件（concepts/time-series）。イベント告知は #232 掲載分と重複のためスキップ
- 2026-07-12 ingest: WKN #231 → 新規 3 件（concepts/image-recognition, experiment-management, tabular）
- 2026-07-12 ingest: WKN #232 → 新規 5 件（solutions.md ×2、Optiver の div 新設 / events.md / concepts/nlp-llm, image-recognition）

- 2026-07-12 ingest: WKN #233 → 新規 3 件（concepts/ai-agent, environment, nlp-llm）
- 2026-07-12 ingest: WKN #234 → 新規 4 件（solutions.md / concepts/time-series, image-recognition, academic-competition）
- 2026-07-12 ingest: WKN #235 → 新規 0 件（2 件とも既掲載）

- 2026-07-12 ingest: WKN #236 → 新規 3 件（solutions.md、IMC2024 の div 新設 / concepts/pytorch ×2）。イベント URL 変種 1 件はスキップ
- 2026-07-12 ingest: WKN #237 → 新規 3 件（solutions.md ×2、Home Credit 2・DS Dojo #1 の div 新設 / service.md「GitHub Actions」新設）
- 2026-07-12 ingest: WKN #238 → 新規 3 件（milestones.md / concepts/nlp-llm, tabular）

- 2026-07-12 ingest: WKN #239 → 新規 6 件（solutions.md ×2、LLM Prompt Recovery の div 新設 / concepts/recommendation, competition-hosting, nlp-llm, time-series）
- 2026-07-12 ingest: WKN #240 → 新規 0 件（4 件すべて既掲載）
- 2026-07-12 ingest: WKN #241 → 新規 3 件（events.md / concepts/mindset, experiment-management）
- 2026-07-12 ingest: WKN #242 → 新規 3 件（milestones.md / events.md / concepts/time-series）

- 2026-07-12 ingest: WKN #243 → 新規 5 件（solutions.md ×4、HMS / USPTO / 睡眠 / Machine Unlearning の div 新設 / quickstart.md）
- 2026-07-12 ingest: WKN #244 → 新規 2 件（solutions.md、LMSYS の div 新設 / concepts/mindset）

- 2026-07-12 ingest: WKN #245 → 新規 0 件（3 件すべて既掲載）
- 2026-07-12 ingest: WKN #246 → 新規 1 件（solutions.md）
- 2026-07-12 ingest: WKN #247 → 新規 2 件（solutions.md / events.md）
- 2026-07-12 ingest: WKN #248 → 新規 4 件（milestones.md / solutions.md / concepts/image-recognition）。YouTube プレイリストの URL 変種 1 件はスキップ

- 2026-07-12 ingest: WKN #249 → 新規 3 件（solutions.md ×3）
- 2026-07-12 ingest: WKN #250 → 新規 0 件（2 件とも既掲載）
- 2026-07-12 ingest: WKN #251 → 新規 2 件（solutions.md、ISIC 2024 の div 新設 / concepts/nlp-llm）
- 2026-07-12 ingest: WKN #252 → 新規 4 件（events.md ×2 / concepts/image-recognition, mindset）。ho.lc の URL 変種 1 件は既掲載のためスキップ

- 2026-07-12 ingest: WKN #253 → 新規 5 件（solutions.md ×2 / concepts/ai-agent, mindset ×2）
- 2026-07-12 ingest: WKN #254 → 新規 5 件（solutions.md ×4、atmaCup #17 の div 新設 / concepts/environment）
- 2026-07-12 ingest: WKN #255 → 新規 1 件（events.md）
- 2026-07-12 ingest: WKN #256 → 新規 3 件（solutions.md ×3）
- 2026-07-12 ingest: WKN #257 → 新規 2 件（concepts/evaluation-validation, nlp-llm）
- 2026-07-12 ingest: WKN #258 → 新規 3 件（concepts/tabular, nlp-llm, image-recognition）
- 2026-07-12 ingest: WKN #259 → 新規 1 件（concepts/nlp-llm）
- 2026-07-12 ingest: WKN #260 → 新規 2 件（solutions.md / events.md）。開催中コンペの告知 1 件はスキップ
- 2026-07-12 ingest: WKN #261 → 新規 3 件（concepts/image-recognition, academic-competition ×2）。運営メンバー募集の告知 1 件はスキップ
- 2026-07-12 ingest: WKN #262 → 新規 2 件（solutions.md / concepts/image-recognition）

- 2026-07-12 ingest: WKN #263 → 新規 3 件（milestones.md ×2 / concepts/image-recognition）
- 2026-07-12 ingest: WKN #264 → 新規 1 件（milestones.md）。終了済みコンペの告知 1 件はスキップ
- 2026-07-12 ingest: WKN #265 → 新規 1 件（concepts/tabular）。既掲載書籍の URL 変種 1 件はスキップ
- 2026-07-12 ingest: WKN #266 → 新規 2 件（solutions.md）

- 2026-07-12 ingest: WKN #267 → 新規 2 件（concepts/nlp-llm, graph）
- 2026-07-12 ingest: WKN #268 → 新規 1 件（concepts/nlp-llm）
- 2026-07-12 ingest: WKN #269 → 新規 0 件（3 件すべて既掲載）
- 2026-07-12 ingest: WKN #270 → 新規 1 件（concepts/nlp-llm）
- 2026-07-12 ingest: WKN #271 → 新規 1 件（concepts/evaluation-validation）
- 2026-07-12 ingest: WKN #272 → 新規 1 件（events.md）

- 2026-07-12 ingest: WKN #273 → 新規 1 件（solutions.md）。GPU プレゼント企画の告知 1 件は時限性のためスキップ
- 2026-07-12 ingest: WKN #274 → 新規 1 件（concepts/experiment-management）
- 2026-07-12 ingest: WKN #275 → 新規 2 件（events.md / concepts/experiment-management）
- 2026-07-12 ingest: WKN #276 → 新規 1 件（concepts/experiment-management）。資料が 15 件を超えたため「考え方・体制」「ツール・テンプレート」「コード品質・高速化」の小見出しで整理
- 2026-07-12 ingest: WKN #277 → 新規 1 件（solutions.md）
- 2026-07-12 ingest: WKN #278 → 新規 1 件（concepts/nlp-llm）

- 2026-07-12 ingest: WKN #279 → 新規 0 件（7 件すべて既掲載）
- 2026-07-12 ingest: WKN #280 → 新規 2 件（solutions.md / events.md）
- 2026-07-12 ingest: WKN #281 → 新規 2 件（concepts/evaluation-validation, mindset）
- 2026-07-12 ingest: WKN #282 → 新規 1 件（concepts/nlp-llm）
- 2026-07-12 ingest: WKN #283 → 新規 3 件（concepts/competition-hosting, environment, tabular）
- 2026-07-12 ingest: WKN #284 → 新規 1 件（concepts/tabular）

- 2026-07-12 ingest: WKN #285 → 新規 1 件（concepts/academic-competition）
- 2026-07-12 ingest: WKN #286 → 新規 1 件（milestones.md）
- 2026-07-12 ingest: WKN #287 → 新規 0 件（2 件とも既掲載）
- 2026-07-12 ingest: WKN #288 → 新規 1 件（concepts/image-recognition）。ho.lc の URL 変種 1 件は既掲載のためスキップ
- 2026-07-12 ingest: WKN #289 → 新規 0 件（3 件すべて既掲載）
- 2026-07-12 ingest: WKN #290 → 新規 1 件（concepts/agent-competition）
- 2026-07-12 ingest: WKN #291 → 新規 1 件（concepts/nlp-llm）
- 2026-07-12 ingest: WKN #292 → 新規 8 件（concepts/image-recognition, mindset, experiment-management ×2, nlp-llm, evaluation-validation, tabular, ai-agent）。開催告知 2 件は既掲載イベントと重複のためスキップ
- 2026-07-12 ingest: WKN #293 → 新規 1 件（solutions.md。ho.lc の URL は現行のハイフン形式で掲載）
- 2026-07-12 ingest: WKN #294 → 新規 1 件（concepts/experiment-management）
- 2026-07-12 ingest: WKN #295 → 新規 1 件（events.md）
- 2026-07-12 ingest: WKN #296 → 新規 3 件（events.md / concepts/tabular, image-recognition）
- 2026-07-12 ingest: WKN #297 → 新規 3 件（quickstart.md / concepts/experiment-management, nlp-llm）
- 2026-07-12 ingest: WKN #298 → 新規 7 件（第 4 回関東 Kaggler 会の発表資料: milestones.md / events.md / concepts/image-recognition, experiment-management, nlp-llm, ai-agent, mindset）
- 2026-07-12 ingest: WKN #299 → 新規 1 件（solutions.md）
- 2026-07-12 ingest: WKN #300 → 新規 2 件（events.md / concepts/experiment-management）。既掲載論文の URL 変種 1 件はスキップ
- 2026-07-12 ingest: WKN #301 → 新規 1 件（concepts/pytorch）
- 2026-07-12 ingest: WKN #302 → 新規 1 件（concepts/nlp-llm）

- 2026-07-11 ingest: WKN #303 → 新規 3 件（solutions.md / concepts/academic-competition, image-recognition）
- 2026-07-11 ingest: WKN #304 → 新規 2 件（concepts/audio, nlp-llm）。学生プログラムの募集告知 1 件は時限性のためスキップ
- 2026-07-11 ingest: WKN #305 → 新規 2 件（concepts/nlp-llm ×2）
- 2026-07-11 ingest: WKN #306 → 新規 3 件（events.md「沖縄 Kaggler 会」新設 / concepts/environment, nlp-llm）
- 2026-07-11 ingest: WKN #307 → 新規 0 件（2 件とも既掲載）
- 2026-07-11 ingest: WKN #308 → 新規 2 件（events.md）

- 2026-07-11 restructure: 概念マップページ（docs/concept-map.md）を新設。ページ間の相互リンクを力学レイアウトで可視化（データはビルド時に tools/build_graph_data.py が生成）。共通ナビと README 目次から導線を追加

- 2026-07-11 restructure: 文章規約を CLAUDE.md に新設（日本語の地の文は全角括弧。リンクタイトル・URL・コード・HTML は原文のまま）し、全ページの地の文の半角括弧を全角に一括変換（168 行）

- 2026-07-11 restructure: 目次をトップページ（README.md）に統合し docs/materials.md を廃止。ナビ・quickstart・スキーマ（CLAUDE.md の管理境界: README の「目次」「最近の更新」セクションを LLM 管理に）・スキル・検証ツールの参照を更新

- 2026-07-11 restructure: サイト改善を実施。（1） 全リンク横断のサイト内検索（search.md、ビルド時に search.json 生成） （2） 共通ナビゲーション（_layouts/default.html） （3） materials.md に「最近の更新」 （4） 整合性検査を tools/verify_wiki.py に昇格し CI 化、注釈カバレッジ表示を追加 （5） 月次リンク切れ検査ワークフロー（Issue 起票） （6） nlp-llm・image-recognition の資料を小見出しで整理し、15 件超で小見出し整理の規約を CLAUDE.md に追加

- 2026-07-11 ingest: WKN #309 → 新規 3 件（concepts/nlp-llm, experiment-management, environment）
- 2026-07-11 ingest: WKN #310 → 新規 4 件（events.md / concepts/image-recognition ×2, evaluation-validation）
- 2026-07-11 ingest: WKN #311 → 新規 2 件（events.md / concepts/agent-competition）。既掲載イベントの資料公開告知 1 件はスキップ
- 2026-07-11 ingest: WKN #312 → 新規 4 件（solutions.md / concepts/environment, academic-competition, nlp-llm）
- 2026-07-11 ingest: WKN #313 → 新規 3 件（solutions.md / concepts/time-series, mindset）
- 2026-07-11 ingest: WKN #314 → 新規 5 件（solutions.md / concepts/image-recognition ×2, evaluation-validation, audio）
- 2026-07-11 restructure: 最新動向の調査（mlcontests 年次レポート、Kaggle Game Arena 公式発表）を踏まえ、概念ページ「エージェント対戦コンペ」（agent-competition）を新設。ai-agent を「道具としての活用」に位置づけ直し、evaluation-validation に Kaggle のベンチマーク基盤化、nlp-llm に 2025 年のデコーダ型 LLM への移行・テスト時学習の潮流を追記
- 2026-07-11 ingest: WKN #315 → 新規 1 件（concepts/mindset）。他 4 件は既掲載
- 2026-07-11 ingest: WKN #316 → 新規 3 件（concepts/optimization, image-recognition, tabular）
- 2026-07-11 ingest: WKN #317 → 新規 3 件（events.md / concepts/tabular, nlp-llm）
- 2026-07-11 ingest: WKN #318 → 新規 0 件（3 件すべて既掲載）
- 2026-07-11 ingest: WKN #319 → 新規 0 件（4 件すべて既掲載）
- 2026-07-11 ingest: WKN #320 → 新規 4 件（solutions.md ×3 / concepts/environment, experiment-management）
- 2026-07-11 ingest: WKN #321 → 新規 4 件（solutions.md / events.md / concepts/competition-hosting, experiment-management）
- 2026-07-11 ingest: WKN #322 → 新規 2 件（solutions.md / events.md）
- 2026-07-11 ingest: WKN #323 → 新規 2 件（solutions.md）
- 2026-07-11 ingest: WKN #324 → 新規 7 件（solutions.md ×4 / platform.md / concepts/optimization, academic-competition, competition-hosting）。解法動画公開のニュース 2 件はスキップ
- 2026-07-10 ingest: WKN #343 → 新規 3 件（books.md / events.md / concepts/competition-hosting）。Orbit Wars の結果公開ニュースと SIGNATE NEDO Challenge コンテスト2 の開催告知は時限性・資料なしのためスキップ
- 2026-07-10 ingest: WKN #325 → 新規 5 件（solutions.md / events.md / concepts/mindset, nlp-llm, academic-competition）
- 2026-07-10 ingest: WKN #326 → 新規 2 件（milestones.md）
- 2026-07-10 ingest: WKN #327 → 新規 1 件（solutions.md、concepts/ai-agent にも掲載）
- 2026-07-10 ingest: WKN #328 → 新規 6 件（solutions.md ×2 / events.md / concepts/environment, ai-agent, academic-competition）
- 2026-07-10 ingest: WKN #329 → 新規 4 件（solutions.md ×2 / milestones.md / concepts/time-series）。Nishika のコンペサービス終了を platform.md に反映
- 2026-07-10 ingest: WKN #330 → 新規 2 件（solutions.md / events.md）
- 2026-07-10 ingest: WKN #331 → 新規 3 件（events.md / concepts/ai-agent, academic-competition）
- 2026-07-10 ingest: WKN #332 → 新規 2 件（events.md / concepts/competition-hosting）。開催中コンペの告知 1 件はスキップ
- 2026-07-10 ingest: WKN #333 → 新規 1 件（concepts/ai-agent）。終了済み講座の告知 1 件はスキップ
- 2026-07-10 ingest: WKN #334 → 新規 1 件（solutions.md）。行政事業の告知 1 件は時限性のためスキップ
- 2026-07-10 ingest: WKN #335 → 新規 2 件（events.md / concepts/image-recognition）
- 2026-07-10 ingest: WKN #336 → 新規 3 件（solutions.md / concepts/ai-agent, mindset）
- 2026-07-10 ingest: WKN #337 → 新規 4 件（solutions.md ×2 / concepts/image-recognition, mindset）
- 2026-07-10 ingest: WKN #338 → 新規 2 件（solutions.md / events.md）
- 2026-07-10 ingest: WKN #339 → 新規 3 件（solutions.md「Kaggle 公式」/ concepts/nlp-llm, mindset）
- 2026-07-10 ingest: WKN #340 → 新規 2 件（solutions.md / events.md）。学生コンペの開催告知 1 件は時限性のためスキップ
- 2026-07-10 ingest: WKN #341 → 新規 1 件（concepts/nlp-llm）。ハッカソン支援・コンペ開催の告知 2 件は時限性のためスキップ
- 2026-07-10 ingest: WKN #342 → 新規 8 件（solutions.md / books.md / events.md / quickstart.md / service.md / concepts: competition-hosting, audio, academic-competition, mindset, ai-agent）。TabFM は既掲載のためスキップ

- 2026-07-10 restructure: 概念ページ getting-started を quickstart.md（入門者・初学者向けガイド）に統合し削除（定番資料を「定番資料」セクションとして移設）。Q&A（Query ページの資産化機構）を廃止し、materials.md・CLAUDE.md・query / lint スキルから関連記述を除去

- 2026-07-10 restructure: materials.md の目次を単一の話題分類に統合（「用途別一覧」セクションを解消し、一覧ページ 8 本を「学び方」「情報収集・コミュニティ」「データ種別・タスク」の各見出しに配置）。README 冒頭に Kaggler Ja Wiki と比べた特徴（LLM Wiki 運用、Weekly Kaggle News がソース、PR レビューでの反映）を追記し、サイト案内を目次中心に一本化
- 2026-07-10 restructure: 管理境界を変更し用途別一覧ページ 8 本を LLM 管理に移行（CLAUDE.md）。materials.md を「目次」としてサイト全体の入口に再定義し用途別一覧セクションを追加。README のサイト案内を話題別 Wiki 中心に再構成
- 2026-07-10 lint: 概念ページ改名（入門者向け / 自然言語処理コンペ / 音声コンペ / 数理最適化コンペ / 性能評価と検証）に合わせて materials.md の目次と参照ラベルを同期。CLAUDE.md の data-datatype タクソノミーを solutions.md のフィルタ UI と一致する 9 値に修正。相対リンク・孤立ページ・目次同期・solutions.md 形式・URL 重複の検査はすべて問題なし
- 2026-07-10 restructure: 話題別 Wiki と話題別一覧を統合（1 話題 1 ページ化）。概念ページ 8 本を新設（getting-started / pytorch / graph / recommendation / mindset / environment / academic-competition / competition-hosting）し全リンクを概念ページに集約、materials.md を目次化、wiki/index.md を廃止。Weekly Kaggle News 周年記事は recent.md へ移設
- 2026-07-10 fix: ho.lc の URL 形式変更（アンダースコア→ハイフン）に伴うリンク切れを修正（materials.md / solutions.md / milestones.md / service.md / concepts/code-competition.md / concepts/evaluation-validation.md）
- 2026-07-10 ingest: https://research.google/blog/introducing-tabfm-a-zero-shot-foundation-model-for-tabular-data/ → materials.md（表）、concepts/tabular.md
- 2026-07-10 seed: 概念ページ 10 本（tabular / image-recognition / nlp-llm / time-series / audio / optimization / code-competition / experiment-management / ai-agent / evaluation-validation）と index.md を初期構築
