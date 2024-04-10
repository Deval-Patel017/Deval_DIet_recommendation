# import the OpenAI Python library for calling the OpenAI API
import json
from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("<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>"))
# Example OpenAI Python library request
MODEL = "gpt-3.5-turbo-0125"
# example with a system message
response = client.chat.completions.create(
    model=MODEL,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain asynchronous programming in the style of the pirate Blackbeard."},
    ],
    temperature=0,
)

print(response.choices[0].message.content)

