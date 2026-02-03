
from fastapi import FastAPI
from Pdf_Reader.Api.pdf_routes import router

app = FastAPI(title="Docu-Mind API")

# Include your router
app.include_router(router)

# --- NEW: Root Endpoint to fix 404 error ---
@app.get("/")
def read_root():
    return {"message": "Docu-Mind API is running!"}