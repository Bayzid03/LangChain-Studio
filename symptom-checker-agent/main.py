import os
from dotenv import load_dotenv; load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.messages import HumanMessage, AIMessage
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import tools
from schema import StructureOutput

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.3,
    max_output_tokens=1000,
)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

parser = PydanticOutputParser(pydantic_object=StructureOutput)

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())

# Agent & Executor
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Chat Session
chat_history = []
print("🧺 Medical Symptom Checker (type 'exit' to quit)\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        print("Session ended.")
        break

    chat_history.append(HumanMessage(content=query))
    result = executor.invoke({"query": query, "chat_history": chat_history})

    try:
        response = parser.parse(result["output"])
        print(f"\n🧺 Possible Cause: {response.probable_cause}")
        print(f"🧺 Severity Level: {response.severity}")
        print(f"🧺 Advice: {response.advice}")
        print(f"🧺 Log: {response.log_status}")
        chat_history.append(AIMessage(content=response.probable_cause))
    except Exception as e:
        print("\n⚠️ Error parsing response:", e)
        print("Raw output:\n", result["output"])

