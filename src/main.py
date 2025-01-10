import openai
from openai import OpenAI
import getpass
key = getpass.getpass("Paste key")
openai.api_key = key


client = OpenAI(api_key=key)
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"you are a helpful assistant"},
        {"role":"user","content":"What is the best resources to learn python in 2025"}
    ]
)
print(response.choices[0].message.content)




