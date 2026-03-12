from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app =  FastAPI()

# ab direct static folder ko mount kar dete hai
app.mount("/static",StaticFiles(directory="static"),name="static")