from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

SQLAlchemyDatabaseURL = "sqlite:///./blog.db"

engine = create_engine(
    SQLAlchemyDatabaseURL, 
    connect_args={"check_same_thread": False}  # for SQLite + FastAPI
)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()
