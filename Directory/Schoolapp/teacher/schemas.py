from pydantic import BaseModel
from datetime import date

class TeacherBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    subject: str
    hire_date: date

class TeacherCreate(TeacherBase):
    school_id: int

class TeacherResponse(TeacherBase):
    id: int
    school_id: int

    class Config:
        from_attributes = True

# TEACHER DASHBOARD
class TeacherDashboard(BaseModel):
    total_staff: int
    active_hiring: bool

class SubjectResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

# --- TEACHER-SUBJECT SCHEMAS ---
from pydantic import BaseModel

class TeacherSubjectCreate(BaseModel):
    teacher_id: int
    subject_id: int

class TeacherSubjectResponse(BaseModel):
    id: int
    teacher_id: int
    subject_id: int

    class Config:
        from_attributes = True
