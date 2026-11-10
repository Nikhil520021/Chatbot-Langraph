import os
from typing import Annotated, TypedDict

from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages


class ChatState(TypedDict):
    messages: Annotated[list, add_messages]


def build_chatbot():
    model_name = os.getenv("OLLAMA_MODEL", "qwen2.5:3b")
    llm = ChatOllama(model=model_name, temperature=0.7)

    def chatbot_node(state: ChatState):
        response = llm.invoke(state["messages"])
        return {"messages": [response]}

    workflow = StateGraph(ChatState)
    workflow.add_node("chatbot", chatbot_node)
    workflow.set_entry_point("chatbot")
    workflow.add_edge("chatbot", END)
    return workflow.compile()


def main():
    chatbot = build_chatbot()
    conversation = {"messages": []}

    print("Chatbot-Langraph is ready. Type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit", "bye"}:
            print("Goodbye!")
            break

        if not user_input:
            continue

        conversation["messages"].append(HumanMessage(content=user_input))
        try:
            result = chatbot.invoke(conversation)
        except Exception as exc:
            print(
                "Could not reach Ollama. Make sure Ollama is running and the model "
                f"is installed (ollama pull {os.getenv('OLLAMA_MODEL', 'qwen2.5:3b')}).\n"
                f"Details: {exc}"
            )
            conversation["messages"].pop()
            continue

        conversation = {"messages": result["messages"]}
        print(f"Bot: {result['messages'][-1].content}")


if __name__ == "__main__":
    main()
