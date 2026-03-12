#CONNECTION MANAGER

from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

class ConnectionManager: # iss client ka kaam - add , remove , broadcast karna
    def __init__(self): #creating list to store all connected client
        self.active_connections = []

    async def connect(self, websocket:WebSocket):
        await websocket.accept()

        self.active_connections.append(websocket) 
        #Client websocket object list me add ho rahe hai
        #KYU - taaki server ko pata rahe kaun kaun connect hai

    def disconnect(self, websocekt:WebSocket):
        self.active_connections.remove(websocekt)
        
    async def broadcast(self, message:str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager  =  ConnectionManager()

@app.websocket("/ws")
async def websocket_endpoint(websocket:WebSocket):
    await manager.connect(websocket)

    try:
        while True:
            data  =  await websocket.receive_text()
            await manager.broadcast(f"Client says: {data}")

    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(" A client left the chat")