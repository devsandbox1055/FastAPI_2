from fastapi import FastAPI

app  = FastAPI()

# SINGLE QUERY PARAMETER

@app.get("/product")
async def product(category:str):
    return {"status":"OK" ,"category":category}


# MULTIPLE QUERY PARAMETER

@app.get("/product")
async def product(category:str, limit:int):
    return {"status":"OK" ,"category":category, "limit":limit}

# Optional Query Parameter

@app.get("/product")
async def get_product(category: str | None = None):
    return {"category": category}
""" 
/items
/items?category=mobile   dpno chalega
"""

# DEFAULT value query
@app.get("/product")
async def get_product(limit int  = 10):
    return {"limit": limit}

"""
default mein 10 hi chalega agar user koi aur limit na de
for example (5)
"""