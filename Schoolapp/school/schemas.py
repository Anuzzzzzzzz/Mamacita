from pydantic import BaseModel
from datetime import datetime

# 1. Base Schema (Shared fields)
class SchoolBase(BaseModel):
    name: str
    address: str | None = None
    phone: str | None = None
    email: str | None = None

# 2. Create Schema (What user sends to us)
class SchoolCreate(SchoolBase):
    pass

# 3. Response Schema (What we send back - includes ID)
class SchoolResponse(SchoolBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# 4. DASHBOARD SCHEMA (The Report Card)
class SchoolDashboard(BaseModel):
    total_schools: int
    total_students: int
    total_teachers: int