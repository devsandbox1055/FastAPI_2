# HTTPException tab use karte hai jab Client
# ki galti ho for example
# 1. invalid input , 2. data not found , 3. unauthorized data

# First example of HTTP Expection
# USER NOT FOUND

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/user/{user_id}")
def get_user(user_id: int):
    if user_id != 1:
        raise HTTPException(
            status_code=404,
            detail="user not found"
        )
    return {"user_id": user_id , "name": "Dev"}

# 2. CUSTOM EXPECTION + EXCEPTION HANDLER
# Important hai

from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse

app = FastAPI()

# ab ek custom expection class banate hai
class Invalidageexpection(Exception): #Apni custom error type bana rahe hain
    def __init__(self, age:int): #constructor, to store wrong value of age
        self.age = age

#ab ek exception handler
async def invalidAH(request: Request, exc: Invalidageexpection):
    return JSONResponse (
        status_code= 400,
        content={"message": f"invalid age: {exc.age}. age must be 18 or above"}
    )
    
#ab api ke liye endpoint
@app.get("/vote/{age}")
def vote(age:int):
    if age<18:
        raise Invalidageexpection(age)
    return {"message": "you are eligible to vote"}

# 3. Custom Validation Error Message

from pydantic import BaseModel , Field

class user(BaseModel):
    name: str = Field(..., min_length=3)
    age: int = Field(..., ge=18)


# PRODUCTION STYLE EXAMPLE OF ERROR HANDLING

from fastapi import FastAPI , HTTPException

app = FastAPI()

@app.get("/divide")
def divide(a:int , b:int):
    if b== 0:
        raise HTTPException(400, "Division by zero is not allowed")
    return {"result" : a/b}