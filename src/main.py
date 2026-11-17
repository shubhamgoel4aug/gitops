from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/healthz")
async def healthz():
    return {"message": "Service is up."}

@app.get("/api/hello")
async def hello():
    return {"message": "Hello World"}

@app.get("/api/time")
async def time():
    return {"message": datetime.now()}