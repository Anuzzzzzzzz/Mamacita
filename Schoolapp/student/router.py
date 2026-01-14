from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from . import schemas, service

router = APIRouter(prefix="/student", tags=["student"])

# REAL DASHBOARD
@router.get("/dashboard", response_model=schemas.StudentDashboard)
def get_dashboard(db: Session = Depends(get_db)):
    return service.get_student_dashboard(db)

@router.post("/create_student", response_model=schemas.StudentResponse)
def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
    return service.create_student(db, student)

@router.get("/get_students", response_model=list[schemas.StudentResponse])
def read_students(db: Session = Depends(get_db)):
    return service.get_students(db)