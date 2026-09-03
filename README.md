# AI Agent with Google GenAI SDK

An extendable, step-by-step AI Agent project built with Python and the official Google GenAI SDK (`google-genai`).

---

## 🎯 Purpose of this Project

The primary purpose of this project is to provide a **modular, step-by-step learning and development framework** for building autonomous AI agents powered by Google Gemini models.

Modern AI agents progress through clear evolutionary stages:
1. **Direct Generation**: One-shot queries and responses.
2. **Conversational Memory & Streaming**: Interactive, stateful dialogues with streaming outputs.
3. **Tool/Function Calling (Agentic Behavior)**: Enabling the AI model to reason, decide, and execute Python functions (e.g., reading files, interacting with APIs) to solve real-world problems.

This repository serves as a practical, production-ready template to learn, experiment, and extend AI agent capabilities with clean architecture and modern tooling (`uv`, `google-genai`).

---

## 📂 Project Structure

```text
AI_Agent/
├── src/
│   └── ai_agent/
│       ├── __init__.py      # Package entry point
│       ├── notes.txt        # Sample text file used for tool-calling demonstrations
│       ├── step1.py         # Step 1: Single prompt & basic generation
│       ├── step2.py         # Step 2: Multi-turn streaming chat
│       └── step3.py         # Step 3: Tool / Function calling agent (File reader)
├── .env.example             # Template for required environment variables
├── pyproject.toml           # Project dependencies and packaging configuration
├── uv.lock                  # Dependency lockfile
├── LICENSE                  # MIT License
└── README.md                # Project documentation
```

---

## 🚀 Evolutionary Steps & Processes

The project is structured into three progressive steps:

### 1. Step 1: Single Prompt Generation (`step1.py`)
- **Process**: Connects to Gemini using `genai.Client()`, loads environment variables, and executes a one-off `generate_content` call.
- **Concepts**: API initialization, authentication, model selection, prompt dispatch, and response extraction.

### 2. Step 2: Multi-Turn Streaming Chatbot (`step2.py`)
- **Process**: Establishes a stateful chat session using `client.chats.create()` and handles streaming tokens via `send_message_stream()` in a command-line loop.
- **Concepts**: Conversation history management, low-latency streaming responses, user input handling, and clean session termination.

### 3. Step 3: Tool & Function Calling Agent (`step3.py`)
- **Process**: Registers Python functions as tools in `GenerateContentConfig(tools=[...])`. When given a goal requiring external data, the model determines when and how to call the local `read_file` function, executes it, and synthesizes the final answer.
- **Concepts**: Agentic reasoning, schema declaration via Python type hints & docstrings, automatic tool invocation, and grounded response synthesis.

---

## 🛠️ Prerequisites & Tech Stack

- **Python**: `>= 3.12`
- **Package Manager**: [uv](https://docs.astral.sh/uv/) (recommended) or `pip`
- **Key Libraries**:
  - `google-genai`: The official modern Google Gemini SDK.
  - `python-dotenv`: Environment variable management.
- **API Key**: A valid Google AI / Gemini API key from [Google AI Studio](https://aistudio.google.com/).

---

## ⚙️ Installation & Setup

### 1. Clone or Open the Repository
```bash
cd "d:/cursor/Ai projects/01/AI_Agent"
```

### 2. Create and Activate a Virtual Environment

Using **uv** (recommended):
```bash
uv venv
# On Windows PowerShell:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

Or using standard **venv**:
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

Using **uv**:
```bash
uv sync
```

Or using **pip**:
```bash
pip install -e .
```

### 4. Configure Environment Variables

Create a `.env` file in the project root by copying `.env.example`:

```bash
cp .env.example .env
```

Edit `.env` and insert your Gemini API Key:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

## 💻 How to Run

You can run each progressive step directly:

### Run Step 1 (Basic Generation)
```bash
python src/ai_agent/step1.py
```

### Run Step 2 (Interactive Chat)
```bash
python src/ai_agent/step2.py
```
> Type your message to chat with the bot. Type `exit` or `quit` to end the session.

### Run Step 3 (Agent with File Tool)
```bash
python src/ai_agent/step3.py
```
> The agent inspects `notes.txt` using its tool-calling mechanism and provides a summary.

---

## 🔄 Processes to Extend this AI Agent

To build a fully capable autonomous AI assistant from this foundation, follow these recommended development processes:

### 1. Adding New Tools
Define standard Python functions with type annotations and descriptive docstrings. The SDK converts these into tool schemas automatically:
```python
def write_file(path: str, content: str) -> str:
    """Write content to a file at the specified path."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    return f"Successfully wrote {len(content)} bytes to {path}"
```
Pass the function to `tools` in `GenerateContentConfig(tools=[read_file, write_file])`.

### 2. Adding System Instructions & Personas
Configure system guidelines to control agent tone, safety, and constraints:
```python
config = types.GenerateContentConfig(
    system_instruction="You are an expert software developer assistant. Always verify file paths before reading.",
    tools=[read_file],
    temperature=0.2,
)
```

### 3. Implementing Multi-Step Tool Execution Loops
Combine multi-turn chat loops (`step2.py`) with tool calling (`step3.py`) to allow the agent to execute multiple tools in sequence dynamically based on user requests.

### 4. Integrating External Services & RAG
- **Web Search & APIs**: Add tools that fetch weather, search the web, or query REST APIs.
- **RAG (Retrieval-Augmented Generation)**: Add vector embeddings and semantic search tools over large document repositories.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](file:///d:/cursor/Ai%20projects/01/AI_Agent/LICENSE) file for details.

## 👤 Author

- **WIJAYATHUNGA R.S.C.W.M.T.B.K.** ([thatilawijayathunga@gmail.com](mailto:thatilawijayathunga@gmail.com))
