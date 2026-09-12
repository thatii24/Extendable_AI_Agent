import os
import subprocess
from dotenv import load_dotenv

from google import genai
from google.genai import types

load_dotenv()

client = genai.Client()
MODEL = "gemini-3.6-flash"

SYSTEM_PROMPT = """You are a coding agent running in the user's terminal. You can list files, read files, write files, and run shell commands. Use your tools to complete the user's task, then briefly summarize what you did. The working directory is the folder the user launched you from."""


def list_files(path: str = ".") -> str:
    """List the files and directories in a given folder. Folders end with /.

    Args:
        path: Directory path to list, defaults to '.'
    """
    print(f"  [Tool] list_files(path='{path}')")
    try:
        entries = []
        for entry in os.scandir(path):
            entries.append(entry.name + ("/" if entry.is_dir() else ""))
        return "\n".join(sorted(entries)) or "(empty directory)"
    except Exception as error:
        return f"Error listing directory: {error}"


def read_file(path: str) -> str:
    """Read a text file and return its contents.

    Args:
        path: Path of the file to read.
    """
    print(f"  [Tool] read_file(path='{path}')")
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as error:
        return f"Error reading file: {error}"


def write_file(path: str, content: str) -> str:
    """Create or overwrite a text file with the given content.

    Args:
        path: Path of the file to write.
        content: Full text content to write to the file.
    """
    print(f"  [Tool] write_file(path='{path}')")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Saved {path} ({len(content)} characters)"
    except Exception as error:
        return f"Error writing file: {error}"


def run_command(command: str) -> str:
    """Run a shell command in the terminal and return its output.

    Args:
        command: The shell command to run.
    """
    print(f"  [Tool] run_command(command='{command}')")
    answer = input(f" Run '{command}'? [y/n] ")
    if answer.strip().lower() != "y":
        return "The user declined to run this command."
    try:
        result = subprocess.run(
            command, shell=True, capture_output=True, text=True, timeout=120
        )
        output = (result.stdout + result.stderr).strip()
        return output or f"(no output, exit code {result.returncode})"
    except Exception as error:
        return f"Error running command: {error}"


def main():
    chat = client.chats.create(
        model=MODEL,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=[list_files, read_file, write_file, run_command],
        ),
    )
    print("Mini agent ready. Type 'exit' to quit.")
    while True:
        try:
            user_input = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print("\nExiting.")
            break

        if user_input.strip().lower() in ("exit", "quit"):
            break
        if not user_input.strip():
            continue

        try:
            response = chat.send_message(user_input)
            print(f"\nAgent: {response.text}")
        except Exception as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()
