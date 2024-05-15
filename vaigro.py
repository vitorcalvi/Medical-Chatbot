import os

from groq import Groq

client = Groq(
    # This is the default and can be omitted
    api_key="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",
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "you are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)