from utils.llm import call_llm

SYSTEM_PROMPT = """あなたはAWS認定資格の専門家です。
指定された資格試験のドメイン構成と主要トピックを、正確かつ体系的に整理してください。
出力は日本語で、Markdown形式で記述してください。"""


def run(certification: str) -> str:
    user_prompt = f"""「{certification}」試験について、以下を整理してください。

1. 試験の概要（目的・対象者）
2. ドメイン一覧（ドメイン名と配点比率）
3. 各ドメインの主要トピック一覧

公式試験ガイドの内容をベースに、受験者が学習計画を立てられる粒度で出力してください。"""

    return call_llm(SYSTEM_PROMPT, user_prompt)
