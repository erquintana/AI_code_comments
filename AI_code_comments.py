#openai.api_key = "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"

import os
import openai

openai.api_key = os.getenv("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")

response = openai.Completion.create(
    model="text-davinci-003",
    prompt="white a poem",
    temperature=0,
    max_tokens=64,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    stop=["\"\"\""]
)