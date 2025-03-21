from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Папка для хранения загруженных файлов
UPLOAD_DIR = "./uploads"

# Убедимся, что директория для загрузок существует
os.makedirs(UPLOAD_DIR, exist_ok=True)


# Роут для загрузки файла
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)

    # Открываем файл и записываем данные
    with open(file_location, "wb") as buffer:
        # Читаем данные из UploadFile и записываем их в файл
        content = await file.read()
        buffer.write(content)

    return {"filename": file.filename, "message": "Файл загружен успешно"}


# Роут для скачивания файла
@app.get("/files/{filename}")
async def get_file(filename: str):
    file_location = os.path.join(UPLOAD_DIR, filename)
    if os.path.exists(file_location):
        return FileResponse(file_location)
    return {"error": "Файл не найден"}
