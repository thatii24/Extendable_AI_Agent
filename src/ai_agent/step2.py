from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client()

chat = client.chats.create(model="gemini-3.5-flash-lite")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ("exit", "quit"):
        break

    print("Bot: ", end="", flush=True)
    for chunk in chat.send_message_stream(user_input):
        print(chunk.text, end="", flush=True)
    print()
