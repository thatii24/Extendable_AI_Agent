from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client()

def read_file(path: str) -> str:
    """Read a text file and return its contents."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Map of tool functions
available_tools = {
    "read_file": read_file,
}

# 1. Your messages history
messages = [
    types.Content(
        role="user",
        parts=[types.Part.from_text(text="What is the inside notes.txt? Summarize it in one line.")]
    )
]

# 2. Your Agent While-Loop
while True:
    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[read_file],
        ),
    )

    # If the model didn't call any tools, print the final answer and exit
    if not response.function_calls:
        print(response.text)
        break

    # If the model requested tool calls, execute them
    for function_call in response.function_calls:
        tool_name = function_call.name
        tool_args = function_call.args
        print(f"Model want to run : {tool_name} ({dict(tool_args)})")

        tool_func = available_tools[tool_name]
        result = tool_func(**tool_args)

        # Append model's tool call to history
        messages.append(response.candidates[0].content)

        # Append tool result back to history
        messages.append(
            types.Content(
                role="tool",
                parts=[
                    types.Part.from_function_response(
                        name=tool_name,
                        response={"result": result},
                    )
                ],
            )
        )
