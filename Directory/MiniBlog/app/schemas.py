from pydantic import BaseModel
from typing import Optional

# 1. Define the Data Model
class BlogCreate(BaseModel):
    Title: str
    content: str
    author: Optional[str] = "Anonymous"

class BlogResponse(BaseModel):
    id: int
    title: str
    content: str
    author: str

    class Config:
        orm_mode = True