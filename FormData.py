# first insall multipart dependency
# "pip install python-multipart"

#SIMPLE LOGIN FORM

from fastapi import FastAPI, Form

app = FastAPI()

@app.post("/login")
async def login(
    username: str = Form(...),
    password: int = Form(...) #ye sab required field hai
):
    return{
        "username": username,
        "password": password
    }

#OPTIONAL FIELD
@app.post("/register")
async def register(
    name: str = Form(...),
    email: str = Form(...),
    age: int = Form(None) #yaha pe age optional hai
):
    return {
        "name": name,
        "email": email,
        "age": age
    }

#MULTIPE FORM FIELDS
@app.post("/signup")
async def signup(
    name:str =Form(...),
    email:str  = Form(...),
    password:str = Form(...),
    phone: int = Form(...)
):
    return{"message": "User Created"}

