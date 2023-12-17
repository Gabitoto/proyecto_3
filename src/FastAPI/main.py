from fastapi import FastAPI
from typing import Union

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/url")
async def read_root():
    return {"url_curso":"https://replit.com/"}

#aca hasta ahora hiciste algunos "get" que te permiten obtener datos de un servidor y mostrarlo basicamente. 
