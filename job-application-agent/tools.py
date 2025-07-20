from langchain.tools import Tool
from datetime import datetime
from pathlib import Path

def read_file(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    return path.read_text(encoding="utf-8")

def save_application(resume: str, cover_letter: str, job_title: str):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    
    folder = Path("applications")
    folder.mkdir(exist_ok=True)

    base_name = f"{job_title.replace(' ', '_')}_{timestamp}" # Generate a safe base filename
    
    (folder / f"{base_name}_resume.txt").write_text(resume, encoding="utf-8") # Write resume
    (folder / f"{base_name}_cover_letter.txt").write_text(cover_letter, encoding="utf-8") #Write cover letter

    return f"Saved application for {job_title} with resume and cover letter."
