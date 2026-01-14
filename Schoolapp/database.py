from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# 1. The Connection String (Where the file is)
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

# 2. The Engine (The car that drives the data back and forth)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# 3. The Session (The temporary workspace)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. The Base (The template for all Models)
class Base(DeclarativeBase):
    pass

# 5. The Dependency (The tool we give to Routers)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()