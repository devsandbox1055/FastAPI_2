from fastapi import FastAPI , WebSocket, Depends

app =  FastAPI()

async def get_token(websocket:WebSocket):
    token = websocket._query_params.get("token")

    if token != "abc123":
        await websocket.close()
        
    return token

@app.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket,token:str=Depends(get_token)):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Toeken{token} sent message{data}")

""" client connect karega agar token galat hua to connection close
"""