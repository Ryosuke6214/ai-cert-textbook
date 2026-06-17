# MVP 実装計画

## 概要

AWS Certified AI Practitioner向けの教材を自動生成するシステムのMVPを実装する。

- 言語: Python
- UI: Streamlit
- AIエージェント: Research / Content / Review の3エージェント（逐次実行）
- 出力: Markdown ファイル

---

## タスク一覧

### Phase 1: 環境構築

- [ ] **T1** ディレクトリ構造を作成する
  - `agents/`, `utils/`, `output/` フォルダを作成
  - エントリポイント `app.py` を置くトップレベル構成にする

- [ ] **T2** `requirements.txt` を作成する
  - `streamlit` — UI
  - `anthropic` — Claude API クライアント
  - `requests` / `beautifulsoup4` — Web スクレイピング
  - `python-dotenv` — APIキー管理

- [ ] **T3** `.env.example` を作成する
  - `ANTHROPIC_API_KEY` のテンプレートを用意する

---

### Phase 2: 共通基盤

- [ ] **T4** `utils/llm.py` を実装する
  - Claude API を呼び出す共通関数を作る
  - モデル: `claude-sonnet-4-6`（デフォルト）
  - システムプロンプトとユーザープロンプトを受け取り、テキストを返す

- [ ] **T5** `utils/web.py` を実装する
  - URLを受け取りテキストを取得するスクレイピング関数を作る
  - `requests` + `BeautifulSoup` で本文テキストを抽出する

---

### Phase 3: エージェント実装

- [ ] **T6** `agents/research_agent.py` を実装する
  - 入力: 資格名（例: "AWS Certified AI Practitioner"）
  - 処理:
    1. AWS 公式の試験ガイドURLから試験範囲テキストを取得する
    2. Claude に「この試験のドメインと主要トピック一覧を整理して」と依頼する
  - 出力: ドメイン・トピック一覧（テキスト）

- [ ] **T7** `agents/content_agent.py` を実装する
  - 入力: Research Agent の出力（トピック一覧）
  - 処理:
    1. トピックごとに Claude に「解説を書いて」と依頼する（ループ）
    2. 各解説を結合して1つの教材テキストにまとめる
  - 出力: Markdown 形式の教材本文

- [ ] **T8** `agents/review_agent.py` を実装する
  - 入力: Content Agent の出力（教材本文）
  - 処理:
    1. Claude に「この教材のレビューをして改善点を指摘して」と依頼する
    2. Claude に「改善点を反映した改訂版を出力して」と依頼する
  - 出力: レビュー済み Markdown 教材

---

### Phase 4: パイプライン統合

- [ ] **T9** `pipeline.py` を実装する
  - Research → Content → Review の順に各エージェントを呼び出す
  - 実行ログ（各ステップの開始・完了）を返す
  - 最終出力を `output/textbook.md` に保存する

---

### Phase 5: Streamlit UI

- [ ] **T10** `app.py` を実装する
  - 資格名入力フォームを表示する
  - 「生成開始」ボタンを押すと `pipeline.py` を呼び出す
  - 各ステップの進行状況を `st.status` または `st.spinner` で表示する
  - 完成した教材を画面にプレビュー表示する
  - Markdown ファイルとしてダウンロードできるボタンを表示する

---

### Phase 6: 動作確認

- [ ] **T11** エンドツーエンドで実行する
  - `streamlit run app.py` で起動して画面が表示されることを確認する
  - "AWS Certified AI Practitioner" を入力して教材が生成されることを確認する
  - `output/textbook.md` に Markdown ファイルが保存されることを確認する

---

## ファイル構成（目標）

```
ai-cert-textbook/
├── app.py               # Streamlit エントリポイント
├── pipeline.py          # エージェントの逐次実行
├── agents/
│   ├── research_agent.py
│   ├── content_agent.py
│   └── review_agent.py
├── utils/
│   ├── llm.py           # Claude API ラッパー
│   └── web.py           # Webスクレイピング
├── output/              # 生成した Markdown の保存先
├── requirements.txt
├── .env.example
└── .env                 # gitignore に追加
```

---

## 依存関係

```
T1 → T2 → T3
T4, T5 は T1 の後に並行して実装可能
T6 は T4, T5 が完了してから
T7 は T4 が完了してから（T6 と並行可能）
T8 は T4 が完了してから（T6, T7 と並行可能）
T9 は T6, T7, T8 が完了してから
T10 は T9 が完了してから
T11 は T10 が完了してから
```
