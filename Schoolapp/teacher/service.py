from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas

def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    db_teacher = models.Teacher(**teacher.model_dump())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

def get_teachers(db: Session):
    return db.query(models.Teacher).all()

def get_teacher_dashboard(db: Session):
    count = db.query(func.count(models.Teacher.id)).scalar()
    return {
        "total_staff": count,
        "active_hiring": True # Hardcoded for now, but in real life could come from DB
    }