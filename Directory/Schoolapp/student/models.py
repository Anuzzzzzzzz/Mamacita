from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import date
from database import Base

class Student(Base):
    __tablename__ = "students"
    
    __table_args__ = {'extend_existing': True}

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    school_id: Mapped[int] = mapped_column(ForeignKey("schools.id")) # Links to School Table

    first_name: Mapped[str] = mapped_column(String(100))
    last_name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(255), unique=True)
    grade: Mapped[str] = mapped_column(String(20))
    enrollment_date: Mapped[date]

    # Links back to the School model
    school = relationship("School", back_populates="students")