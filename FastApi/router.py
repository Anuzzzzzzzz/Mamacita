# File: FastApi/router.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

# Import our separated files
from databases import get_db
import models
import schemas

api_router = APIRouter()

# ==========================
# USER OPERATIONS
# ==========================

@api_router.post("/users/", response_model=schemas.UserResponse, tags=["Users"])
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 1. Check if email already exists
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=400, 
            detail="Error: This email is already registered. Try logging in."
        )
    
    # 2. Create the user
    fake_hashed_password = user.password + "notreallyhashed"
    new_user = models.User(email=user.email, hashed_password=fake_hashed_password)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@api_router.get("/users/", response_model=List[schemas.UserResponse], tags=["Users"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = db.query(models.User).offset(skip).limit(limit).all()
    return users

@api_router.get("/users/{user_id}", response_model=schemas.UserResponse, tags=["Users"])
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# ==========================
# LOGIN SIMULATION
# ==========================
@api_router.post("/login/", tags=["Auth"])
def login(user_credentials: schemas.UserLogin, db: Session = Depends(get_db)):
    # Find user
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    
    if not user:
        raise HTTPException(status_code=404, detail="Invalid Credentials: User not found")
    
    # Check password (simple check)
    expected_hash = user_credentials.password + "notreallyhashed"
    if user.hashed_password != expected_hash:
        raise HTTPException(status_code=401, detail="Invalid Credentials: Wrong password")
        
    return {"message": "Login Successful", "user_id": user.id, "email": user.email}

# ==========================
# ITEM OPERATIONS
# ==========================

@api_router.post("/users/{user_id}/items/", response_model=schemas.ItemResponse, tags=["Items"])
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    # Check if user exists first
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="Cannot add item: User ID not found")

    new_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item

@api_router.get("/items/", response_model=List[schemas.ItemResponse], tags=["Items"])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = db.query(models.Item).offset(skip).limit(limit).all()
    return items

# ==========================
# DELETE OPERATIONS
# ==========================

@api_router.delete("/items/{item_id}", tags=["Items"])
def delete_item(item_id: int, db: Session = Depends(get_db)):
    # 1. Find the item
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    
    # 2. Check if it exists
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    # 3. Delete it
    db.delete(item)
    db.commit()
    
    return {"message": "Item deleted successfully", "item_id": item_id}