# MVP 実装計画

## 概要

AWS Certified AI Practitioner向けの教材を自動生成するシステムのMVPを実装する。

- 言語: Python
- UI: Streamlit
- AIエージェント: Research / Content の2エージェント（逐次実行）
- 出力: Markdown ファイル

---

## 今回のスコープ外

以下は今回のMVPでは実装しない。一連のAI駆動開発を経験することを優先する。

- Review Agent（教材レビュー・改訂）
- 本格的なWebスクレイピング（OpenAIの知識で代替）
- DB（ファイル保存のみ）
- ログイン機能
- 複数資格対応

---

## タスク一覧

### Phase 1: 環境構築

- [x] **T1** ディレクトリ構造を作成する
  - `agents/`, `utils/`, `output/` フォルダを作成
  - エントリポイント `app.py` を置くトップレベル構成にする

- [ ] **T2** `requirements.txt` を作成する
  - `streamlit` — UI
  - `openai` — OpenAI API クライアント
  - `python-dotenv` — APIキー管理

- [ ] **T3** `.env.example` を作成する
  - `OPENAI_API_KEY` のテンプレートを用意する

---

### Phase 2: 共通基盤

- [ ] **T4** `utils/llm.py` を実装する
  - OpenAI API を呼び出す共通関数を作る
  - モデル: `gpt-4o`（デフォルト）
  - システムプロンプトとユーザープロンプトを受け取り、テキストを返す

---

### Phase 3: エージェント実装

- [ ] **T5** `agents/research_agent.py` を実装する
  - 入力: 資格名（例: "AWS Certified AI Practitioner"）
  - 処理:
    1. OpenAI に「この試験のドメインと主要トピック一覧を整理して」と依頼する
    2. ※Webスクレイピングは行わず、OpenAIの知識を活用する
  - 出力: ドメイン・トピック一覧（テキスト）

- [ ] **T6** `agents/content_agent.py` を実装する
  - 入力: Research Agent の出力（トピック一覧）
  - 処理:
    1. トピックごとに OpenAI に「解説を書いて」と依頼する（ループ）
    2. 各解説を結合して1つの教材テキストにまとめる
  - 出力: Markdown 形式の教材本文

---

### Phase 4: パイプライン統合

- [ ] **T7** `pipeline.py` を実装する
  - Research → Content の順に各エージェントを呼び出す
  - 実行ログ（各ステップの開始・完了）を返す
  - 最終出力を `output/textbook.md` に保存する

---

### Phase 5: Streamlit UI

- [ ] **T8** `app.py` を実装する
  - 資格名入力フォームを表示する
  - 「生成開始」ボタンを押すと `pipeline.py` を呼び出す
  - 各ステップの進行状況を `st.status` または `st.spinner` で表示する
  - 完成した教材を画面にプレビュー表示する
  - Markdown ファイルとしてダウンロードできるボタンを表示する

---

### Phase 6: 動作確認

- [ ] **T9** エンドツーエンドで実行する
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
│   └── content_agent.py
├── utils/
│   └── llm.py           # OpenAI API ラッパー
├── output/              # 生成した Markdown の保存先
├── requirements.txt
├── .env.example
└── .env                 # gitignore に追加
```

---

## 依存関係

```
T1 → T2 → T3
T4 は T1 の後に実装
T5, T6 は T4 が完了してから（並行可能）
T7 は T5, T6 が完了してから
T8 は T7 が完了してから
T9 は T8 が完了してから
```
