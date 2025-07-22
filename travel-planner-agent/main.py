from dotenv import load_dotenv; load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import tools
from pathlib import Path
from datetime import datetime
from prompts import SYSTEM_PROMPT

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)
parser = PydanticOutputParser(pydantic_object=TravelPlan)

prompt= ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
]).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

chat_history = []
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting the travel planner. Goodbye!")
        break

    chat_history.append(HumanMessage(content=user_input))
    
    response = agent_executor.invoke({
        "chat_history": chat_history,
        "query": user_input,
    })
    try:
        output = parser.parse(response["output"])
        print("Itinerary:", output.itinerary)
        print("Highlights:", output.highlights)
        print("Saved Path:", output.saved_path)
        chat_history.append(AIMessage(content=str(output)))
    except Exception as e:
        print("Error parsing response:", e)
        print("Response:", response["output"])
