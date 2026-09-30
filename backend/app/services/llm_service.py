import os

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def run_agent(prompt: str):
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert assistant for Agent Space."},
            {"role": "user", "content": prompt},
        ],
    )
    return completion.choices[0].message.content
