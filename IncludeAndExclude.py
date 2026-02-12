"""FastAPI mein include aur exclude fields ka concept 
mostly response_model ke saath use hota hai , especially jab ham
sensitive yaa unnecessary data ko hide karna chaahte hai
"""

#for exmaple
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class user(BaseModel):
    id: int
    name: str
    email: str
    password: str

#let say ham password hide karna chaate hai

@app.get("/user", response_model=User, response_class_exclude={"password"})
def get_user():
    return{
        "id": 1,
        "name":"devesh",
        "email":"dev2gmail;.com",
        "password":"secret123"
    }
#ab response mein password nahi aayega

#ab agar hame selected field hi dikhaane hai mtlb INCLUDE
#karna hai to
@app.get("/user", response_model=User, response_model_include={"name","email"})
def get_user():
    return {
        "id": 1,
        "name":"devesh",
        "email":"dev2gmail;.com",
        "password":"secret123"
    }

#AGAR NESTED MODEL MEIN include ya exclude karna ho to
class Profile(BaseModel):
    bio: str
    location: str

class User(BaseModel):
    id: int
    name: str
    profile: Profile

@app.get(
    "/user",
    response_model=User,
    response_model_include={"name", "profile": {"bio"}}
)
def get_user():
    return {
        "id": 1,
        "name": "Devesh",
        "profile": {
            "bio": "Cloud Learner",
            "location": "India"
        }
    }

#MODEL SEPERATE KARNA

class UserBase(BaseModel):
    name:str
    email: str

class UserIn(UserBase):
        password:str

class UserOut(UserBase):
     id: int    
