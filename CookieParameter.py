from fastapi import FastAPI, Cookie
from typing import Annotated

app = FastAPI()

@app.get("/products/recom")
async def get_recom(session_id: Annotated[str | None,Cookie()] =  None):
    if session_id:
        return{"message": f"Recommendations for session {session_id}", "session_id": session_id}
    return {"message": "No session id provided , showing defauly id"}