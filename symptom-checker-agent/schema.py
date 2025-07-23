from pydantic import BaseModel, Field

class StructureOutput(BaseModel):
  probable_cause: str = Field(..., description = "What could be causing this symptom")
  severity: str = Field(..., description = "Severity Level: mild / moderate / severe")
  advice: str = Field(..., description = "Advice for next step")
  log_status: str = Field(default = "", description = "Status of logging")
