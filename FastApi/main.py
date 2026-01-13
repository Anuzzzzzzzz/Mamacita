# File: FastApi/main.py
import uvicorn
from fastapi import FastAPI
from databases import engine, Base
from router import api_router

# 1. Create Database Tables (Automatically!)
Base.metadata.create_all(bind=engine)

# 2. Initialize App
app = FastAPI(
    title="My Super Cool API",
    description="A professional CRUD API with Users and Items",
    version="2.0.0"
)

# 3. Include the Router
app.include_router(api_router)

@app.get("/", tags=["General"])
def root():
    return {"message": "API is running! Go to /docs to see the magic."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)