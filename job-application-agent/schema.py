from pydantic import BaseModel
from typing import List

class ApplicationOutput(BaseModel):
    job_title: str
    resume: str
    cover_letter: str