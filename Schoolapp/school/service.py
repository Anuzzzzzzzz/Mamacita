from sqlalchemy.orm import Session
from sqlalchemy import func
from . import models, schemas


def create_school(db: Session, school: schemas.SchoolCreate):
    db_school = models.School(**school.model_dump())
    db.add(db_school)
    db.commit()
    db.refresh(db_school)
    return db_school

def get_all_schools(db: Session):
    return db.query(models.School).all()

def get_school_dashboard(db: Session):
    # This prevents the "Table already defined" error
    import student.models
    import teacher.models
    
    # Count rows in database
    s_count = db.query(func.count(models.School.id)).scalar()
    stu_count = db.query(func.count(student.models.Student.id)).scalar()
    t_count = db.query(func.count(teacher.models.Teacher.id)).scalar()
    
    return {
        "total_schools": s_count,
        "total_students": stu_count,
        "total_teachers": t_count
    }

def get_school(db: Session, school_id: int):
    return db.query(models.School).filter(models.School.id == school_id).first()