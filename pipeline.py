import os
from datetime import datetime
from agents import research_agent, content_agent

OUTPUT_DIR = "output"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "textbook.md")


def run(certification: str) -> list[str]:
    logs = []

    def log(msg: str) -> str:
        entry = f"[{datetime.now().strftime('%H:%M:%S')}] {msg}"
        logs.append(entry)
        return entry

    log(f"Research Agent 開始: {certification}")
    research_output = research_agent.run(certification)
    log("Research Agent 完了")

    log("Content Agent 開始")
    content_output = content_agent.run(research_output)
    log("Content Agent 完了")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content_output)
    log(f"教材を保存しました: {OUTPUT_FILE}")

    return logs, content_output
