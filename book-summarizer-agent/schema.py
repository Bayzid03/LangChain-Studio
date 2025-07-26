class StructureOutput(BaseModel):
    summary: str = Field(..., description="Condensed summary of the input")
    title: str = Field(..., description="Title of the book or chapter")
    saved_path: str = Field(default="", description="Where the summary was saved")
