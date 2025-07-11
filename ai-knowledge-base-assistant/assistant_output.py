from pydantic import BaseModel, Field
from typing import Optional

class AssistantOutput(BaseModel):
    answer: str
    sources: Optional[str] = Field(default="")