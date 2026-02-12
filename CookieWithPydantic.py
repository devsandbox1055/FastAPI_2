from fastapi import FastAPI, Cookie,Body
from typing import Annotated
from pydantic import BaseModel ,Field

app = FastAPI()

class ProductCookies(BaseModel):
    session_id: str
    preferred_category: str | None = None
    tracking_id: str | None = None

@app.get("/product/recom")
async def get_recom(cookies: Annotated[ProductCookies,Cookie()]):
    response = {"session_id": cookies.session_id}
    if cookies.preferred_category:
        response["message"] = f"Recom for {cookies.preferred_category} product"
    else:
        response["message"] = f"Default recom for session{cookies.session_id}"
    if cookies.tracking_id:
        response["tracking_id"] = cookies.tracking_id
    return response
