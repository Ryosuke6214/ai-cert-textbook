from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

_client = OpenAI()


def call_llm(system_prompt: str, user_prompt: str, model: str = "gpt-4o") -> str:
    response = _client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content
