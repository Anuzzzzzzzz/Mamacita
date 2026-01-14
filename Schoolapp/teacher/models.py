from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from database import Base

# -------------------------
# TEACHER MODEL
# -------------------------
class Teacher(Base):
    __tablename__ = "teachers"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    school_id: Mapped[int] = mapped_column(ForeignKey("schools.id"))

    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    subject: Mapped[str] = mapped_column(String(100))
    hire_date: Mapped[date] = mapped_column()  # Python type, no SQLAlchemy type here

    # Relationships
    school = relationship("School", back_populates="teachers")
    subjects = relationship(
        "Subject",
        secondary="teacher_subjects",
        back_populates="teachers"
    )

# -------------------------
# SUBJECT MODEL
# -------------------------
class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100), unique=True)

    # Relationship
    teachers = relationship(
        "Teacher",
        secondary="teacher_subjects",
        back_populates="subjects"
    )

# -------------------------
# ASSOCIATION TABLE (MANY-TO-MANY)
# -------------------------
class TeacherSubject(Base):
    __tablename__ = "teacher_subjects"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    teacher_id: Mapped[int] = mapped_column(ForeignKey("teachers.id"))
    subject_id: Mapped[int] = mapped_column(ForeignKey("subjects.id"))

# -------------------------
# HIRING MODEL (for dashboard)
# -------------------------
class Hiring(Base):
    __tablename__ = "hirings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    is_active: Mapped[bool] = mapped_column(default=True)
