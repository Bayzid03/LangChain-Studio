from dotenv import load_dotenv; load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor

from tools import tools
from prompts import SYSTEM_PROMPT
from schema import StructureOutput

# Set up LLM and parser
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.4,
    max_output_tokens=1200
)

parser = PydanticOutputParser(pydantic_object=StructureOutput)

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())

# Agent setup
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Chat loop
chat_history = []
print("📚 Book Summarizer Agent (type 'exit' to quit)\n")

while True:
    query = input("You: ")
    if query.lower() == "exit":
        print("📕 Session ended.")
        break

    chat_history.append(HumanMessage(content=query))
    result = executor.invoke({"query": query, "chat_history": chat_history})

    try:
        response = parser.parse(result["output"])
        print(f"\n📌 Title: {response.title}")
        print(f"📝 Summary:\n{response.summary}\n")
        print(f"💾 Saved to: {response.saved_path}")
        chat_history.append(AIMessage(content=response.summary))
    except Exception as e:
        print("\n⚠️ Error parsing response:", e)
        print("🔍 Raw output:\n", result["output"])
