from fastapi import APIRouter, UploadFile, File, HTTPException

router = APIRouter(prefix="/upload", tags=["PDF"])

@router.post("/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files allowed")

    content = await file.read()

    if len(content) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File too large")

    return {
        "filename": file.filename,
        "size": len(content),
        "message": "Upload successful"
    }
