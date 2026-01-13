# FastApi/models.py
from sqlalchemy import Column, Integer, String
from .databases import Base

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author = Column(String, nullable=True)

    def __repr__(self):
        return f"<Blog(id={self.id}, title='{self.title}', author='{self.author}')>"
