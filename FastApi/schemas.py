from pydantic import BaseModel
from typing import Optional

# 1. Define the Data Model
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

class UserProfile(BaseModel):
    username: str
    email: str
    age: int
    is_active: bool = True  
    bio: Optional[str] = None