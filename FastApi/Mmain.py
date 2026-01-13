# FastApi/Mmain.py
from .databases import Base, engine, SessionLocal
from .models import Blog

print("🟢 Creating database tables...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created successfully!")

# Open DB session
db = SessionLocal()

# Seed some blogs
blogs_to_add = [
    Blog(title="First Post", content="This is the first blog post!", author="Anuj"),
    Blog(title="Second Post", content="Learning SQLAlchemy + FastAPI", author="Aakriti"),
    Blog(title="Third Post", content="Databases are fun!", author="Anuj"),
]

for blog in blogs_to_add:
    db.add(blog)
db.commit()

# Fetch all blogs for display
all_blogs = db.query(Blog).all()
print("📄 Current blogs in database:")
for b in all_blogs:
    print(b)

db.close()
print("✅ Database setup & seeding completed!")
