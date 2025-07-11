from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage

from tools import tools
from assistant_output import AssistantOutput

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

parser = PydanticOutputParser(pydantic_object=AssistantOutput)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are an AI Knowledge Base Assistant.
    Help users by answering questions from loaded company documents.
    Use tools to load documents or retrieve answers.
    Always return JSON with:
    - answer
    - sources
    {format_instructions}
    """),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def main():
    chat_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("Exiting. Goodbye!")
            break

        chat_history.append(HumanMessage(content=user_input))

        response = executor.invoke({
            "input": user_input,
            "chat_history": chat_history
        })

        try:
            structured = parser.parse(response.get("output"))
            print(f"\n📌 Answer:\n{structured.answer}\n📄 Sources: {structured.sources}\n")
            chat_history.append(AIMessage(content=structured.answer))
        except Exception as e:
            print("Error parsing response:", e)
            print("Raw output:", response.get("output"))

if __name__ == "__main__":
    main()
