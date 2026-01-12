# app/main.py
from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from . import models, schemas, databases as database

# Create DB tables
models.Base.metadata.create_all(bind=database.engine)

# FastAPI app
app = FastAPI(title="MiniBlog 2.0 🚀")

# Dependency to get DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------- ROUTES -------------------

@app.post("/blogs/", response_model=schemas.BlogResponse)
def create_blog(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    db_blog = models.Blog(title=blog.title, content=blog.content, author=blog.author)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    print(f"📝 Blog created: {db_blog}")
    return db_blog

@app.get("/blogs/", response_model=list[schemas.BlogResponse])
def get_blogs(db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).all()
    print(f"📄 Fetching all blogs: {blogs}")
    return blogs

@app.get("/blogs/author/{author_name}", response_model=list[schemas.BlogResponse])
def get_blogs_by_author(author_name: str, db: Session = Depends(get_db)):
    blogs = db.query(models.Blog).filter(models.Blog.author == author_name).all()
    if not blogs:
        raise HTTPException(status_code=404, detail=f"No blogs found for author {author_name}")
    print(f"🔍 Blogs by {author_name}: {blogs}")
    return blogs
