# BASIC PYDANTIC MODEL

""" from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str
"""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class user(BaseModel):
    name: str
    age: int

@app.post("/user")
def create_user(user: User):
    return user

"""
{
  "name": "Amit",
  "age": 22
}
"""

# OPTIONAL VALUE agar option mein daalna ho to

from typing import Optional

class Userr(BaseModel):
    name: str
    age:int
    phone:Optional[str] = None
 #Default value bhi bhej skte hai
 
 from typing import Optional

class Userr(BaseModel):
    name: str = "india" # - aise default value dena hai
    age:int 
    phone:Optional[str] = None

#Range de sakte ha kisi value , so that user select one of
#them

from pydantic import BaseModel ,  Field

class userrr(BaseModel):
    age:int = Field(..., gt=0, lt=120)
# now user can select between 0 to 120
# agar galat hua to fastapi apne aap error de dega

#EMAIL VALIDATION bhi hota hai

from pydantic import BaseModel , EmailStr

class Usseer(BaseModel):
    email:EmailStr #Galat email = reject

# PASSWORD VALIDATION

class Register(BaseModel):
    password: str = Field(..., min_length=8)

#NESTED MODEL OR NESTED CLASSES

class Address(BaseModel):
    city:str
    pincode: int

class Useeer(BaseModel):
    name:str
    Address:Address
"""
INPUT
{
  "name": "Devesh",
  "address": {
      "city": "Kanpur",
      "pincode": 208001
  }
}

"""

#COMPLETE EXAMPLE OF PYDANTIC MODEL

class Register(BaseModel):
    username: str
    email: EmailStr
    password: str = Field(..., min_length=8)

@app.post("/register")
def register(user: Register):
    return {"msg": "User registered", "user": user.username}

# Nested Pydantic Model
class Category(BaseModel):
    name:str = Field(
        title= "category name",
        description="the cshvb",
        max_length=50,
        min_length=1
    )
    description:str | None = Field(
        default=None,
        title="vdvsv",
        description="vedvsvs",
        max_length=200
    )
class Product(BaseModel):
    name: str = Field(
        title ="Product Name",
        description="ffff",
        max_length=100,
        min_length=3,
        pattern="^[$#@$@]"

    )
    price: float
    stock: int | None  = None

category:Category | None = Field(
default=None,
title="product category",
description="the category to which the product belong"
)

@app.post("/product")
async def create_product(product:Product):
    return product