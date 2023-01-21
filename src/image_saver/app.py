import os
import uuid
from pathlib import Path
from typing import Tuple

from fastapi import FastAPI, File, HTTPException, UploadFile
from PIL import Image

ALLOWED_EXTENSIONS = {'jpeg', 'jpg', 'png'}

app = FastAPI()


async def allowed_file(file_name: str) -> Tuple[bool, str]:
    if '.' in file_name:
        ext = file_name.rsplit('.', 1)[1].lower()
        if ext in ALLOWED_EXTENSIONS:
            return True, ext
    return False, ''

@app.post("/images")
async def save_image_to_server(file: UploadFile = File(...)):
    is_valid, ext = await allowed_file(file.filename)
    if not is_valid:
        raise HTTPException(
            status_code=415,
            detail="File extension not allowed,"
                   " only jpeg, jpg, png files are allowed"
        )
    random_id = str(uuid.uuid4())
    file_path = Path.cwd().joinpath(f"images/{random_id}.{ext}")
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    try:
        Image.open(file_path)
    except:
        os.remove(file_path)
        return {"detail": "Invalid image file"}
    return {"id": random_id}
