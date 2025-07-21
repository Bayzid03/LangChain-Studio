from langchain.tools import Tool
from datetime import datetime
from pathlib import Path

def save_plan(plan: str, location: str) -> str:
    """
    Save the travel plan to a timestamped file.
    
    Args:
        plan (str): The travel plan to save.
        location (str): The location for which the plan is made.
    
    Returns:
        str: Confirmation message with the file path.
    """
    plans_dir = Path("plans")
    plans_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_location = location.replace(" ", "_").lower()
    filename = plans_dir / f"{safe_location}_{timestamp}.txt"

    filename.write_text(plan, encoding="utf-8")
    return f"Plan saved to {filename}"

def suggest_trip(city: str):
    return f"""
    Top 5 things to do in city:
    1. Visit Historical Areas.
    2. Try Traditional Cuisine.
    3. Explore museum or art districts
    4. Go hiking or sightseeing
    5. Experience local nightlife or music
    """

tools = [
    Tool(name=save_plan, func = save_plan, description= "save the generated itinerary to a file"),
    Tool(name=suggest_trip, func = suggest_trip, descripton= "Suggest activities and attractions for a city")
]
