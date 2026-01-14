from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Student(**student.model_dump())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

def get_students(db: Session):
    return db.query(models.Student).all()

def get_student_dashboard(db: Session):
    # Count only students
    count = db.query(func.count(models.Student.id)).scalar()
    return {
        "total_students_enrolled": count,
        "message": "System Active"
    }