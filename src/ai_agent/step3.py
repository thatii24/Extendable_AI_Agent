from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client()

def read_file(path: str) -> str:
    """Read a text file and return its contents.

    Args:
        path: Path of the file to read.
    """
    print(f"Model want to run : read_file (path='{path}')")
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Create chat session with tools enabled (Google's recommended method)
chat = client.chats.create(
    model="gemini-3.5-flash-lite",
    config=types.GenerateContentConfig(
        tools=[read_file],
    ),
)

prompt = "What is the inside notes.txt? Summarize it in one line."
response = chat.send_message(prompt)

print(response.text)
