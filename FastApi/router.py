# File: FastApi/router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Import our tools
from databases import get_db
import schemas

# Create a Router (like a mini-app)
api_router = APIRouter()

# --- USER ROUTES ---

@api_router.post("/users/", response_model=schemas.UserResponse, tags=["Users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 1. Check if email exists
    db_user = db.query(schemas.User).filter(schemas.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # 2. Create new user (Fake hash for simplicity)
    fake_hashed_password = user.password + "notreallyhashed"
    new_user = schemas.User(email=user.email, hashed_password=fake_hashed_password)
    
    # 3. Save to DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@api_router.get("/users/", response_model=List[schemas.UserResponse], tags=["Users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(schemas.User).offset(skip).limit(limit).all()
    return users

@api_router.get("/users/{user_id}", response_model=schemas.UserResponse, tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(schemas.User).filter(schemas.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# --- ITEM ROUTES ---

@api_router.post("/users/{user_id}/items/", response_model=schemas.ItemResponse, tags=["Items"])
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    # Check if user exists first
    db_user = db.query(schemas.User).filter(schemas.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    # Create item linked to user
    new_item = schemas.Item(**item.dict(), owner_id=user_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@api_router.get("/items/", response_model=List[schemas.ItemResponse], tags=["Items"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(schemas.Item).offset(skip).limit(limit).all()
    return items