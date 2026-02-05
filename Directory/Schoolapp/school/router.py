from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from . import schemas, service

router = APIRouter(prefix="/school", tags=["school"])

# REAL DASHBOARD ENDPOINT
@router.get("/dashboard", response_model=schemas.SchoolDashboard)
def get_dashboard(db: Session = Depends(get_db)):
    return service.get_school_dashboard(db)

@router.post("/create_school", response_model=schemas.SchoolResponse)
def create_school(school: schemas.SchoolCreate, db: Session = Depends(get_db)):
    return service.create_school(db, school)

@router.get("/get_schools", response_model=list[schemas.SchoolResponse])
def read_schools(db: Session = Depends(get_db)):
    return service.get_all_schools(db)