# File: FastApi/databases.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the Database URL (using SQLite)
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Create the Engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create the SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the Base class
Base = declarative_base()

# Define the get_db dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()