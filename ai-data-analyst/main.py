from dotenv import load_dotenv; load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parser import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.messages import HumanMessage, AIMessage

from tools import tools
from schema import AnalysisOutput

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)
parser = PydanticOutputParser(pydantic_objec=AnalysisOutput)