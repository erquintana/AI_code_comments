
import os
import openai

openai.api_key = os.getenv("A")

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