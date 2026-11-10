# Chatbot-Langraph

A simple conversational chatbot built with LangGraph and the OpenAI chat model.

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/macOS
   .venv\\Scripts\\activate      # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key in the environment or copy `.env.example` to `.env` and add it there:
   ```env
   OPENAI_API_KEY=your_api_key_here
   ```

4. Start the chatbot:
   ```bash
   python chatbot.py
   ```

Type `exit`, `quit`, or `bye` to end the chat. Conversation state is retained during the current session.
