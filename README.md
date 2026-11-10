# Chatbot-Langraph

A simple conversational chatbot built with LangGraph and the free, locally running Qwen model through Ollama. No paid model API key is required.

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com/) installed and running

## Setup

1. Download the Qwen model (the default is a compact 3B model):
   ```bash
   ollama pull qwen2.5:3b
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\\Scripts\\activate      # Windows
   ```

3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the chatbot:
   ```bash
   python chatbot.py
   ```

Ollama must be running locally. On most installations its background service starts automatically; otherwise run `ollama serve` in another terminal.

## Change the model

Set `OLLAMA_MODEL` to another model available in Ollama, for example:

```bash
OLLAMA_MODEL=qwen2.5:7b python chatbot.py
```

Pull that model first with `ollama pull qwen2.5:7b`. Larger models generally require more memory.

Type `exit`, `quit`, or `bye` to end the chat. Conversation state is retained during the current session.
