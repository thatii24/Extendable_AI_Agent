import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

def run() -> None:
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents="Explain what an AI agent is in one sentence",
    )

    print(response.text)

if __name__ == "__main__":
    run()