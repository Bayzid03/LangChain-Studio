import os
import gradio as gr
from dotenv import load_dotenv; load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import tools
from schema import TravelPlan
from prompts import SYSTEM_PROMPT
from typing import List

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY environment variable is not set")

# Initialize the LLM and agent
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2, api_key=api_key)
parser = PydanticOutputParser(pydantic_object=TravelPlan)

# Create the agent
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),
]).partial(format_instructions=parser.get_format_instructions())

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

def process_message(history: List[List[str]], message: str) -> tuple:
    """Process a user message and generate a response."""
    try:
        # Convert chat history to the format expected by the agent
        chat_history = []
        for user_msg, bot_msg in history:
            chat_history.append(HumanMessage(content=user_msg))
            if bot_msg:  # Only add bot message if it's not empty
                chat_history.append(AIMessage(content=bot_msg))
        
        # Get response from agent
        response = agent_executor.invoke({
            "chat_history": chat_history,
            "query": message,
        })
        
        try:
            # Try to parse as TravelPlan
            plan = parser.parse(response["output"])
            output = f" Itinerary Created!\n\n Itinerary:\n{plan.itinerary}\n\n Highlights:\n{plan.highlights}"
            if plan.saved_path:
                output += f"\n\n Saved to: {plan.saved_path}"
        except:
            # If parsing fails, use the raw output
            output = response["output"]
            
        return output
    except Exception as e:
        return f"Error processing your request: {str(e)}"

def create_chat_interface():
    """Create the Gradio chat interface."""
    with gr.Blocks(theme=gr.themes.Soft()) as demo:
        gr.Markdown(
            """
            #  Travel Planner Assistant
            Plan your perfect trip with AI! Ask me to create an itinerary, suggest activities, or save your travel plans.
            """
        )
        
        # Chat interface
        chatbot = gr.Chatbot(
            height=500,
            bubble_full_width=False,
            avatar_images=(
                "https://i.imgur.com/5mHQq2O.png",  # User avatar
                "https://i.imgur.com/7UQq3Yj.png"   # Bot avatar
            )
        )
        
        with gr.Row():
            msg = gr.Textbox(
                label="Message",
                placeholder="Where would you like to go?",
                scale=4,
                container=False,
            )
            submit = gr.Button("Send", variant="primary", scale=1)
        
        # Example inputs
        gr.Examples(
            examples=[
                "Plan a 3-day trip to Tokyo",
                "Suggest activities in Paris",
                "Create a weekend itinerary for New York City"
            ],
            inputs=msg,
            label="Try these examples:",
            examples_per_page=3,
        )
        
        # Handle message submission
        def respond(message: str, chat_history: List[List[str]]) -> tuple:
            bot_message = process_message(chat_history, message)
            chat_history.append((message, bot_message))
            return "", chat_history
        
        # Connect the UI components
        msg.submit(respond, [msg, chatbot], [msg, chatbot])
        submit.click(respond, [msg, chatbot], [msg, chatbot])
    
    return demo

if __name__ == "__main__":
    demo = create_chat_interface()
    demo.launch(debug=True, share=True)
