@router.get("/")
def get_user():
    return {"users":[]}

@router.get("/{id}")
def get_user(id:int):
    return{"user":id}

""""
FLOW
/users
/users/1
dono pe verify_token run hoga
"""

"""
INTERNAL FLOW
1.Request receive
2 Dependencies resolve
3 Agar exception → stop
4 Endpoint run
5 Response return
"""
    