from dotenv import load_dotenv; load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parser import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage
from prompts import SYSTEM_PROMPT
from tools import tools
from schema import AnalysisOutput

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

# Parse model output using Pydantic schema
parser = PydanticOutputParser(pydantic_object=AnalysisOutput)

# Prompt template with placeholders and formatting instructions
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),          # It sets the AI's role using System Prompt
    ("placeholder", "{chat_history}"),  # Injects previous messages so the model remembers what's already been discussed.
    ("human", "{query}"),               # Adds the current user QS.
    ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions()) # Adds format instructions based on 'AnalysisOutput' schema.

# Create the tool-calling agent
agent = create_tool_calling_agent(llm, prompt, tools)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# Start interactive CLI loop
chat_history = []
print("AI data analyst (Type 'exit' to quit)")
while True:
    q = input("\nYou: ")
    if q.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=q))  # Adds user question to the 'chat_history' list as a HumanMessage.
    
    response = executor.invoke({"query": q, "chat_history": chat_history})
    
    try:
        ans = parser.parse(response["output"])
        print("\nInsights:", ans.answer) #  Prints the AI's main answer.
        if ans.chart_path:
            print("Chart Saved:", ans.chart_path)
        chat_history.append(AIMessage(content=ans.answer))   # Adds the AI's answer to the 'chat_history' list as an AIMessage.
    except Exception as e:
        print("Parse Error:", e, "\nRaw:", response["output"])


# Key notes:
# {agent_scratchpad} is the agent's internal memory where it tracks its reasoning steps, tool usage, and intermediate outputs during multi-turn interactions.
