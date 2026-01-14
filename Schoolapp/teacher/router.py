from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from . import schemas, service

router = APIRouter(prefix="/teacher", tags=["teacher"])

# REAL DASHBOARD
@router.get("/dashboard", response_model=schemas.TeacherDashboard)
def get_dashboard(db: Session = Depends(get_db)):
    return service.get_teacher_dashboard(db)

@router.post("/", response_model=schemas.TeacherResponse)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return service.create_teacher(db, teacher)

@router.get("/", response_model=list[schemas.TeacherResponse])
def read_teachers(db: Session = Depends(get_db)):
    return service.get_teachers(db)