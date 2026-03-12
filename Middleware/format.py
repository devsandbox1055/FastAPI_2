from fastapi import FastAPI , Request

app = FastAPI()

@app.middleware("http")
async def my_middleware(request:Request,call_next):

    print("before request")

    response = await call_next(request)

    print("after request")

    return response

@app.get("/")
def home():
    return { "message":"Hello"}