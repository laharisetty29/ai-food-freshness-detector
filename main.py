from fastapi import FastAPI, UploadFile, File
import shutil
import os
from detect import detect_freshness

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.get("/")
def home():
    return {"message": "Food Freshness Detector API Running"}


@app.post("/analyze")
async def analyze(image: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, image.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    result = detect_freshness(file_path)

    return {
        "filename": image.filename,
        "prediction": result
    }