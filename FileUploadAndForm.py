# Agar form ke saath file bhi upload karni ho to

from fastapi import FastAPI, UploadFile

@app.post("/upload")
async def upload(
    name:str = Form(...),
    profile_pic: UploadFile = File(...)
):
    return {
        "filename": profile_pic.filename,
        "name": name
    }

"""
<form action="http://127.0.0.1:8000/login" method="post">
  <input type="text" name="username">
  <input type="password" name="password">
  <button type="submit">Login</button>
</form>
# Yaha name="username" backend ke 
# parameter name se match hona chahiye.
"""
