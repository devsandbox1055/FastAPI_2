"""Concept

Client request karta hai → server response de deta hai
 → uske baad background task run hota hai.
 """

from fastapi import FastAPI, BackgroundTasks

app  = FastAPI()

# ye background function hai
def write_log(message:str):
    with open("log.txt","a") as f:
        f.write(message+"/n")

@app.get("/send")
def send_data(background_tasks: BackgroundTasks):

    #ab background task add kar rahe hai
    background_tasks.add_task(write_log,"user visited / send endpoint")

    return{"message": "request recieved"}