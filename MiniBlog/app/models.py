# app/models.py
from sqlalchemy import Column, Integer, String, Text
from .databases import Base # Ensure this matches your project structure

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    author = Column(String(100), nullable=False)
    def __repr__(self):
        return f"<Blog(id={self.id}, title='{self.title}', author='{self.author}')>"
    