# File: FastApi/schemas.py
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from typing import List, Optional
from databases import Base

# ==========================================
# PART 1: DATABASE TABLES (SQLAlchemy)
# ==========================================

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    # Relationship: One User has many Items
    items = relationship("Item", back_populates="owner")

class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    owner_id = Column(Integer, ForeignKey("users.id"))

    # Relationship: An Item belongs to one User
    owner = relationship("User", back_populates="items")


# ==========================================
# PART 2: DATA VALIDATION (Pydantic)
# ==========================================

# --- Item Schemas ---
class ItemBase(BaseModel):
    title: str
    description: Optional[str] = None
    price: float

class ItemCreate(ItemBase):
    pass

class ItemResponse(ItemBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True  # Allows reading from ORM objects

# --- User Schemas ---
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    is_active: bool
    items: List[ItemResponse] = [] # Returns the user's items too!

    class Config:
        from_attributes = True  # Allows reading from ORM objects