"""
Main script to run the Calendar & Email Assistant using LangChain, Gemini, and custom tools.
"""

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage

from tools import tools
from assistant_output import AssistantOutput

load_dotenv()

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

# Parser to enforce structured output
parser = PydanticOutputParser(pydantic_object=AssistantOutput)

# Define the system prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", """
    You are an AI calendar and email assistant.
    You help users manage meetings and emails using the tools provided.
    Always return a valid JSON response with the following fields:
    - action
    - details
    {format_instructions}
    """),
    ("placeholder", "{chat_history}"),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}")
]).partial(format_instructions=parser.get_format_instructions())

# Create agent and executor
agent = create_tool_calling_agent(llm=llm, prompt=prompt, tools=tools)
executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def main():
    chat_history = []

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("Exiting the assistant. Goodbye!")
            break

        # Add user input to chat history
        chat_history.append(HumanMessage(content=user_input))

        # Run agent executor
        response = executor.invoke({
            "input": user_input,
            "chat_history": chat_history
        })

        # Debug: print raw response if needed
        # print("Raw response:", response)

        try:
            structured_response = parser.parse(response.get("output"))
            print(f"\n{structured_response.action.capitalize()}:\n{structured_response.details}\n")
            # Add assistant reply to chat history
            chat_history.append(AIMessage(content=structured_response.details))
        except Exception as e:
            print("\nError parsing response:", e)
            print("Response:", response.get('output'))

if __name__ == "__main__":
    main()
