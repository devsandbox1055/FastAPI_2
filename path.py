#get user id from user

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return{"user_id": user_id}

@app.get("/product/{pid}")
def product(pid: int):
    return("product_id" : pid)

@app.get("/order/{order_id}")
def getoid(order_id: int):
    return("your order is": order_id)