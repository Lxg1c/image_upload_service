from fastapi import FastAPI, File, UploadFile
from pathlib import Path

app = FastAPI()
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename
    with file_path.open("wb") as buffer:
        buffer.write(await file.read())
    return {"filename": file.filename, "path": str(file_path)}
