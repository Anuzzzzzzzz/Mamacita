from database import Base, engine, SessionLocal
import models  # important: import models to register tables
from models import Blog

# 1. Create tables in the database
Base.metadata.create_all(bind=engine)

# 2. Create a new blog entry
db = SessionLocal()
new_blog = Blog(title="First Post", content="This is my first blog post!")
db.add(new_blog)
db.commit()
db.refresh(new_blog)
print(f"Blog added with ID: {new_blog.id}")
db.close()
