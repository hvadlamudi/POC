# Example: reuse your existing OpenAI setup
from openai import OpenAI
from langchain_openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")

completion = client.chat.completions.create(
  model="lmstudio-community/Meta-Llama-3-8B-Instruct-GGUF",
  messages=[
    {"role": "system", "content": "Always answer in bollywood actor Sharukh Khan's way."},
    {"role": "user", "content": "tell me about python programming."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message.content)