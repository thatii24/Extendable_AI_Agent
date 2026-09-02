from google import genai
from dotenv import load_dotenv
import os


load_dotenv()

client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents="Explain what an AI agent is in one sentence",
)

print(response.text)
