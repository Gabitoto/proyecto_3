from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/url")
async def read_root():
    return {"url_curso":"https://replit.com/"}

