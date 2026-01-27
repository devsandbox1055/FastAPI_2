#Request Body = HTTP request ke andar bheja gaya data

from fastapi import FastAPI
from pydantic import BaseModeln

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

def login(data: Login):
    return {"username": data.username}

# for signup api

class Signup(BaseModel):
    name: str
    email: str
    password: str

@app.post("/signup")
def signup(user: Signup):
    return {"msg": "Signup success"}

#Product Add API
class Product(BaseModel):
    name: str
    price: int
    stock: int

@app.post("/product")
def add_product(p: Product):
    return p

@app.get("n/product/{product_id}")
def pid(p:float):
    return p

#Nested Request Body (important)

class Address(Basemodel):
    city: str
    pincode: int

class user(Basemodel):
    name: str
    pincode: int
    address: Address

@app.post("/user")
def Create_user(user: User):
    return user

""" OUTPUT IN JSON
{
  "name": "Dev",
  "age": 21,
  "address": {
    "city": "Varanasi",
    "pincode": 221001
  }
}
"""

#List Inside Request body

class Order(BaseModel):
    item:list[str]
    total:int

@app.post("/order")
def order(data: order):
    return data

"""
{
  "items": ["pizza", "burger", "coke"],
  "total": 500
}
"""

#PATH + QUERY + BODY

@app.post("/user/{user_id}")
def update_user(id:int,active:bool, user: User):
    return {
        "id":id,
        "active": active,
        "date": user
    }
# URL = /user/5?active=true
