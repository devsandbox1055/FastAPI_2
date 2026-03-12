#upload file in background
from fastapi import FastAPI,UploadFile,BackgroundTasks
app = FastAPI()

def save_file(file:UploadFile):

    with open(file.filename,"wb") as f:
        content  = file.file.read()
        f.write(content)

@app.post("/upload")
async def upload_file(file:UploadFile,background_task:BackgroundTasks):
    background_task.add_task(save_file,file)
    return{"message": "file upload started in background"}

"""
client - upload file
api - revieve file
background task schedule
client gets response
file save in background
"""