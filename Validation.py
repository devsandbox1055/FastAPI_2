# FastAPI me validation automatically 
# hoti hai using Pydantic models.
# Galat data aayega → request reject → clean error response

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class user(BaseModel):
    name: str
    age: int #agar koi yaha pe koi str daalega to automatic error aa jaayega
    email: str

@app.post("/user")
def create_user(user:User):
    return user


# Field Constraints Validation
#(matlab length kitni hogi string ya int ki)

from pydantic import BaseModel , Field

class userr(BaseModel):
    name: str = Field(..., min_length=3,max_length=20)
    email:str
    age: int = Field(..., gt=0,lt=120) #for Integer Validation

#CUSTOM VALIDATION (IMPORTANT)

from pydantic import BaseModel ,field_validator

class userrr(BaseModel):
    username: str

    @field_validator("username")
    def check_username(cls,v):
        if " " in v:
            raise ValueError("username must not contain space")
        return v
"""cls = Class ko represent karta hai (User class)
v =Actual input value jo user bhej raha hai
"""
    
# Query Parameter Validation

from fastapi import Query

@app.get("/items")
def read_items(limit: int = Query(10, gt=0, le=100)):
    return {"limit": limit}


# Path Parameter Validation

from fastapi import Path

@app.get("/users/{user_id}")
def read_user(user_id: int = Path(..., gt=0)):
    return {"user_id": user_id}

#Strict Types Validation

from pydantic import StrictInt

class Data(BaseModel):
    count: StrictInt
