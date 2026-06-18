from utils.llm import call_llm

SYSTEM_PROMPT = """あなたはAWS認定資格の専門家であり、優れた教材ライターです。
指定されたトピックについて、試験合格を目指す学習者向けに分かりやすい解説を書いてください。
出力は日本語で、Markdown形式で記述してください。"""


def _explain_topic(topic: str) -> str:
    user_prompt = f"""以下のトピックについて、AWS AI Practitioner試験対策として解説してください。

トピック: {topic}

以下の構成で記述してください。
- 概要（2〜3文）
- 主要な概念・サービス
- 試験で問われるポイント
- 覚えておくべきキーワード"""

    return call_llm(SYSTEM_PROMPT, user_prompt)


def run(research_output: str) -> str:
    lines = [line.strip() for line in research_output.splitlines() if line.strip()]

    topics = [
        line.lstrip("-* ").strip()
        for line in lines
        if line.startswith(("-", "*")) or (len(line) > 2 and line[0].isdigit() and line[1] in ".)")
    ]

    if not topics:
        topics = [line for line in lines if len(line) > 5][:10]

    sections = [f"# AWS Certified AI Practitioner 学習教材\n\n{research_output}\n\n---\n"]

    for topic in topics:
        explanation = _explain_topic(topic)
        sections.append(f"\n## {topic}\n\n{explanation}\n")

    return "\n".join(sections)
