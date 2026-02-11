from fastapi import FastAPI , Body
from pydantic import BaseModel
from typing import Annotated

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

#make body optional

@app.post("/product")
async def create_product(product: Product,seller:Seller | None  = None):
    return{"product": product, "seller":seller}


# Singular value in body

@app.post("/product")
async def create_product(product: Product,seller:Seller, sex_key: Annotated[str,Body()]):
    return{"product": product, "seller":seller, "sec_key"}

# without embeded singular body parameter
@app.post("/product")
async def create_product(product: Product):
    return product

#with embeded
@app.post("/product")
async def create_product(product: Annotated[Product,Body(embed=True)]):
    return product
