from google import genai

client = genai()

response = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages =[
        {"role": "user", "content": "Explain what an AI agent is in one sentence"},
    ],
)

print(response.choices[0].message.content)

