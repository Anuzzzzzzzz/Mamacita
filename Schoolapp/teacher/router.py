from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import get_db
from . import schemas, service

router = APIRouter(prefix="/teacher", tags=["teacher"])

# ---------- API ROUTES ----------
@router.get("/dashboard", response_model=schemas.TeacherDashboard)
def get_dashboard(db: Session = Depends(get_db)):
    return service.get_teacher_dashboard(db)


@router.post("/create_teacher", response_model=schemas.TeacherResponse)
def create_teacher(teacher: schemas.TeacherCreate, db: Session = Depends(get_db)):
    return service.create_teacher(db, teacher)


@router.get("/get_teachers", response_model=list[schemas.TeacherResponse])
def read_teachers(db: Session = Depends(get_db)):
    return service.get_teachers(db)


@router.get("/api/get_teacher_subjects/{teacher_id}",
            response_model=list[schemas.SubjectResponse])
def get_teacher_subjects_api(teacher_id: int, db: Session = Depends(get_db)):
    return service.get_teacher_subjects(db, teacher_id)


# ---------- HTML ROUTE ----------
@router.get("/get_teacher_subjects/{teacher_id}", response_class=HTMLResponse)
def get_teacher_subjects_page(teacher_id: int, db: Session = Depends(get_db)):
    subjects = service.get_teacher_subjects(db, teacher_id)

    return f"""
    <html>
    <head><title>Teacher Subjects</title></head>
    <body>
        <h1>Teacher Subjects</h1>
        <ul>
            {''.join(f'<li>{s.name}</li>' for s in subjects)}
        </ul>
    </body>
    </html>
    """
