
from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def read_root():
    return {"Hello" : "Hello World, this is first FAST API"}