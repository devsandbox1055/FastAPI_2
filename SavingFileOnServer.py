from fastapi import FastAPI, UploadFile, File
from typing import List #multiple file upload allow karta hai
import os #folder create karne ke liye
# SHUTIL = file and folder operation ka module hai(copy, move delete,zip/unzip) 
# jaise kaam karta hai
import shutil #file ko ek jagah se dusri jagah copy karne ke liye

app = FastAPI()

@app.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)): # ... ka mtlb hai required input

    os.makedirs("uploads", exist_ok=True)
    """
"uploads" naam ka folder banao
Agar already hai → error mat do (exist_ok=True) """

    saved_files = []  # ye filename store karegi jo save ho chuki hai
    for file in files:
        file_path = f"uploads/{file.filename}"

        with open(file_path, "wb") as buffer: # WB = write brinary mode , BUFFER ek container hai jissmein data 
            # likha jaayega, iski jagah kuch bhi likh sakte hai
            """ image, pdf, videos text nahi hote hai
            vo raw brinary data hote hai
            agar w use karenge instead of wb
            to file corrupt ho sakti hai"""
            shutil.copyfileobj(file.file, buffer)

        saved_files.append(file.filename)

    return {
        "message": "Files uploaded successfully",
        "saved_files": saved_files
    }

