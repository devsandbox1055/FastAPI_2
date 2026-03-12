from fastapi import FastAPI, WebSocket

app =  FastAPI()

@app.websocket("/ws") #websocket route
async def websocket_endpoint(websocket:WebSocket): #endpoint function

    await websocket.accept() #server , client connection accept karta hai
    while True: #infinite loop...for endless connection
        data = await websocket.receive_text() #client jo msg bhejega
        await websocket.send_text(f"Message Recieved: {data}") #server jo client ko msg bhejega