# Design

## Architecture

- Language: Python
- UI: Streamlit
- Output: Markdown
- Agent Style: Simple sequential agents

## Agents

### Research Agent

試験範囲と関連情報を調査する

### Content Agent

収集した情報をもとに教材本文を作成する

### Review Agent

教材内容を確認し、改善点を出す

## Processing Flow

1. 資格名を入力する
2. 試験範囲を取得する
3. Webから情報を収集する
4. 教材本文を生成する
5. 内容をレビューする
6. Markdownとして保存する

## Initial Target

AWS Certified AI Practitioner