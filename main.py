from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

class Login(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(data: Login):
    return {
        "msg": f"your username is {data.username} and your password is {data.password}"
    }

@app.get("/login")
def get_detail():
    return {"msg": "Hi user"}

@app.post("/user")
def create_user(user: User):
    return {"msg": "User created", "user": user}

@app.get("/user")
def get_user_info():
    return {"msg": "Use POST method to create user"}

@app.get("/")
def home():
    return {"msg": "Server running 🔥"}

@app.get("/")
def root():
    return {"message": "FastAPI is running 🔥"}

@app.get("/item/{Item}")
def path_func(Item: str):
    return {"path variable": Item}

