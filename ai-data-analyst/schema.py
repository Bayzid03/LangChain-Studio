from pydantic import BaseModel, Field
from typing import List, Dict, Optional

class AnalysisOutput(BaseModel):
    answer: str
    chart_path: Optional[str] = ""
    query_sql: Optional[str] = ""
    data_preview: List[Dict] = Field(default_factory=list)