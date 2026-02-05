from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import func

# ----------------------------
# Create a Teacher
# ----------------------------
def create_teacher(db: Session, teacher: schemas.TeacherCreate):
    db_teacher = models.Teacher(**teacher.model_dump())
    db.add(db_teacher)
    db.commit()
    db.refresh(db_teacher)
    return db_teacher

# ----------------------------
# Get all Teachers
# ----------------------------
def get_teachers(db: Session):
    return db.query(models.Teacher).all()

# ----------------------------
# Get Subjects for a Teacher
# ----------------------------
def get_teacher_subjects(db: Session, teacher_id: int):
    return db.query(models.Subject).join(models.TeacherSubject).filter(
        models.TeacherSubject.teacher_id == teacher_id
    ).all()

# ----------------------------
# Teacher Dashboard
# ----------------------------
def get_teacher_dashboard(db: Session):
    total_staff = db.query(func.count(models.Teacher.id)).scalar()
    active_hiring = db.query(models.Hiring).filter(
        models.Hiring.is_active == True
    ).count() > 0
    return schemas.TeacherDashboard(
        total_staff=total_staff,
        active_hiring=active_hiring
    )
