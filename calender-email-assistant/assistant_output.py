from pydantic import BaseModel, Field
from typing import Optional

class AssistantOutput(BaseModel):
    action: str
    details: Optional[str] = Field(default="")