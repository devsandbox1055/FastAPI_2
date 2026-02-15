# return type  = API response ka data type kya hoga.
""""
FastAPI mein hum generally 3 tareeke se return type define karte hain:
Normal Python return (dict, list, str)
Type hints
response_model
"""

#Simple return

from fastapi import FastAPI

app  = FastAPI()

@app.get("/")
def home():
    return {"message": "hello world"} #yaha ham dict return kar rahe hai


#Return type with TYPE HINT

@app.get("/square")
def square(num: int) -> int:
    return num + num # -> int ka mtln return type integer hai

#Return type with response model

@app.get("/user")
def get_user():
    return{
        "name": "devesh",
        "age": 21,
        "password":"secret123" #iss mein problen ye hai ki
        #password bhi client ko chala gaya issliye ham log pydantic ke saath
        #use karte hai

    }

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.get("/user", response_model=User)
def get_user():
    return{
        "name": "devesh",
        "age": 21,
        "password": "secret123" # ab response mein password nahi jaayega    
}

#list return type
from typing import List

@app.get("/users", response_model=List[User])
def get_users():
    return [
        {"name": "Aman", "age": 22},
        {"name": "Rohit", "age": 25}
    ]

# custom response type
#if we want to send raw response

from fastapi.responses import HTMLResponse

@app.get("/html", response_class=HTMLResponse)
def get_html():
    return "<h1> hello devesh</h1>"

# real example of pydantic response model
class UserOut(BaseModel):
    id:int
    name: str
    email: str

@app.get("/user/{user_id}", response_model=UserOut)
def get_user(uder_id: int):
    user  = get_user_from_db(user_id)
    return user
