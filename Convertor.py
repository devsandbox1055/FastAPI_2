from fastapi import FastAPI

app  = FastAPI()

# PATH CONVERTOR - URL ke path se dynamic value lena
# we can also type define

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

"""OUTPUT
if /users/5 then it will be ok , kyu ki (INT) type define kiya hai
if /users/abc - ye str hai..fastapi automatically validate kar deta hai 
"""