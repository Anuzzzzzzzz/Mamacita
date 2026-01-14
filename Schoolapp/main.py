from fastapi import FastAPI
import uvicorn
from database import engine, Base

# Import Routers (Correct Way)
from school.router import router as school_router
from student.router import router as student_router
from teacher.router import router as teacher_router

# Import Models (Correct Way)
import school.models
import student.models
import teacher.models

Base.metadata.create_all(bind=engine)

app = FastAPI(title="My School App", version="1.0.0")

@app.get("/")
def read_root():
    return {"message": "System is Online"}

app.include_router(school_router)
app.include_router(student_router)
app.include_router(teacher_router)

if __name__ == "__main__":
    uvicorn.run(app)