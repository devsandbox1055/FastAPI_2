from fastapi import FastAPI, Depends
app =  FastAPI()

def verify():
    print("checking authentication")

@app.get("/users", dependencies=[Depends(verify)])
async def get_users():
    return {"users":[]}
