@app.middleware("http")
async def middleware1(request: Request,call_next):
    print("middleware 1 before")

    response = await call_next(request)

    print("middleware 1 after ")
    return response


@app.middleware("http")
async def middleware2(request: Request,call_next):
    print("middleware 2 before")

    response = await call_next(request)

    print("middleware 2 after")
    return response


"""
OUTPUT
middleware2 before
middleware1 before
endpoint
middleware1 after
middleware2 after

//last added middleware runs first

"""
