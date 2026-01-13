# File: FastApi/main.py
import uvicorn
from fastapi import FastAPI
from databases import engine
import models
from router import api_router

# 1. Create Database Tables
models.Base.metadata.create_all(bind=engine)

# 2. Initialize App
app = FastAPI(
    title="Professional User System",
    description="Full CRUD system with Users, Items, and Login check",
    version="1.0.0"
)

# 3. Include the Router
app.include_router(api_router)

@app.get("/", tags=["General"])
def root():
    return {"message": "System Online. Go to /docs to use the API."}

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)