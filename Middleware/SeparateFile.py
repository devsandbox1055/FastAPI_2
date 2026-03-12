from fastapi import Request

async def log_middleware(request: Request, call_next):
    print("request path" , request.url.path)
    response =  await call_next(request)

    print("response status",  response.status_code)
    return response


""" main.py file

from fastapi import FastAPI
from app.middleware.logger import log_middleware

app = FastAPI()

app.middleware("http")(log_middleware)

@app.get("/")
async def home():
    return {"msg" : "hello"}
"""

# this is how you separate middleware file to  main.py
