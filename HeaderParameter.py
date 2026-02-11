#Header = Server ko di gayi extra information 
# jo request ke baare me batati hai.

"""
GET /product HTTP/1.1
Host: example.com
User-Agent: Chrome
Authorization: Bearer 123abc
Content-Type: application/json
"""
# Ye sab lines (GET ke neeche wali) = Headers

# Important Headers =  UserAgent(ex - chrome, firefox, mobileapp) 2.Authorization(login token bhejne ke liye
# use hota hai) 3. Content-Type(json, form data, text)

from fastapi import FastAPI , Header
from typing import Annotated

app  = FastAPI()

# Header Parameter
@app.get("/product")
async def get_product(user_agent: Annotated[str | None, Header()] = None):
    return user_agent

#handling duplicate header
@app.get("/product")
async def get_product(x_product_token: Annotated[list[str] | None, Header()] = None):
    return {
        "x_product_token": x_product_token or []
    }
