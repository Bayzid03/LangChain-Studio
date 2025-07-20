from dotenv import load_dotenv; load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import tools
from schema import ApplicationOutput

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    max_output_tokens=1500,
)

parser = PydanticOutputParser(pydantic_object=ApplicationOutput)

prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are a career assistant that helps tailor resumes and write cover letters for job applications.
    Use the provided resume and job description to:
    1. Understand job requirements
    2. Modify the resume to align with key skills
    3. Generate a professional, personalized cover letter

    Always save the result using the save_application tool.

    Output only valid JSON in this format:
    {format_instructions}
    """),
    ("placeholder", "{chat_history}"), # Injects previous messages so the model remembers what’s already been discussed.
    ("human", "{query}"), # Adds current user question
    ("placeholder", "{agent_scratchpad}"),
]).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt) 
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True) # Initialize Agent Executor

chat_history = []

while True:
    query = input("You: ")
    if query.lower() in ["exit", "quit"]:
        print("Exiting the application.")
        break

    chat_history.append(HumanMessage(content=query))

    response = agent_executor.invoke({
        "query": query,
        "chat_history": chat_history,
    })

    try:
        parsed = parser.parse(response["output"])
        print("\n Job Title:", parsed.job_title)
        print("Cover Letter Preview:\n", parsed.cover_letter[:500], "...")  # Preview first 500 characters
        chat_history.append(AIMessage(content=response["output"]))
    except Exception as e:
        print("Error parsing response:", e)
        print("Raw response:", response["output"])
