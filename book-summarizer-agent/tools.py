from pathlib import Path
from datetime import datetime
from langchain.tools import Tool

# Directory for saving summaries
SUMMARY_DIR = Path("summaries")
SUMMARY_DIR.mkdir(exist_ok=True)

def save_summary(text: str, title: str = "summary") -> str:
    """Save a summary to a timestamped file in the summaries directory."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_title = title.replace(" ", "_").lower()
    filename = SUMMARY_DIR / f"{safe_title}_{timestamp}.txt"
    filename.write_text(text, encoding="utf-8")
    return f"Summary saved to {filename}"

def load_summary(title: str) -> str:
    """Load the latest summary file matching the title prefix."""
    safe_title = title.replace(" ", "_").lower()
    files = sorted(SUMMARY_DIR.glob(f"{safe_title}_*.txt"), reverse=True)

    if not files:
        return f"No summaries found for '{title}'."
    
    return files[0].read_text(encoding="utf-8")

tools = [
    Tool(
        name="save_summary",
        func=save_summary,
        description="Save the summary with the given title"
    ),
    Tool(
        name="load_summary",
        func=load_summary,
        description="Load the most recent summary by title"
    )
]
