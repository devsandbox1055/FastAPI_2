from fastapi import FastAPI
from pydantic import BaseModel

app  = FastAPI()

#Multiple body parameter
class Product(BaseModel):
    name:str
    price:float
    stock:int | None = None

class Seller(BaseModel):
    username:str
    full_name: str | None =  None

@app.post("/product")
async def create_product(product: Product,seller:Seller):
    return{"product": product, "seller":seller}