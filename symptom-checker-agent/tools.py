from pathlib import Path
from datetime import datetime
from langchain.tools import Tool

def log_symptom_entry(entry: str) -> str:
    """
    Log a symptom entry to a timestamped file.

    Args:
        entry (str): Symptom description provided by the user.

    Returns:
        str: Confirmation message with the timestamp.
    """
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    filename = logs_dir / f"symptoms_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"

    filename.write_text(f"{timestamp} {entry}\n", encoding="utf-8")
    return f"Symptom logged at {timestamp}"

tools = [
    Tool(
        name="log_symptom_entry",
        func=log_symptom_entry,
        description="Log a symptom description to a timestamped file"
    ),
]
