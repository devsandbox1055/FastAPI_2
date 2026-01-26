from flask import Flask

@app.get("/user")
def get_user():
    return {
        "id": 1,
        "name": "Rahul",
        "email": "rahul@gmail.com",
        "password": "12345"
    }
