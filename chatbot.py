import os
from typing import Annotated, TypedDict

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages

load_dotenv()


class ChatState(TypedDict):
    messages: Annotated[list, add_messages]


def build_chatbot():
    llm = ChatOpenAI(model=os.getenv("OPENAI_MODEL", "gpt-4o-mini"), temperature=0.7)

    def chatbot_node(state: ChatState):
        response = llm.invoke(state["messages"])
        return {"messages": [response]}

    workflow = StateGraph(ChatState)
    workflow.add_node("chatbot", chatbot_node)
    workflow.set_entry_point("chatbot")
    workflow.add_edge("chatbot", END)
    return workflow.compile()


def main():
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY is not set. Add it to your environment or .env file.")

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
            print(f"Chatbot request failed: {exc}")
            conversation["messages"].pop()
            continue

        conversation = {"messages": result["messages"]}
        print(f"Bot: {result['messages'][-1].content}")


if __name__ == "__main__":
    main()
