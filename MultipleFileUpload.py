from fastapi import FastAPI, UploadFile, File
from typing import List

app = FastAPI()

@app.post("/upload-files")
async def upload_files(files: List[UploadFile] = File(...)): # Bas List laga do Multiple upload
    
    file_names = [file.filename for file in files]

    return {
        "total_files": len(files),
        "file_names": file_names
    }
