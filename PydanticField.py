from fastapi import FastAPI , Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()

# Pydantic Field
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

    @app.post("/product")
    async def create_product(product: Product):
        return product