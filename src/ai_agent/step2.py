from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client()

messages = []

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ("exit", "quit"):
        break
    

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completion.create(
        model="gemini-3.6-flash",
        messages=messages,
    )

    reply = response.choices[0].messages.content
    messages.append({"role": "assistant", "content": reply})
    print("Bot: ", reply)
