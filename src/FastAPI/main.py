from fastapi import FastAPI
from routers import products,user #recordemos agregar los scripts es decir los routers
from fastapi.staticfiles import StaticFiles 

app = FastAPI()

# http://127.0.0.1:8000 servidor

#routers

app.include_router(products.router)
app.include_router(user.router)
app.mount("/static",StaticFiles(directory= "static"), name= "static") #con esto llamamos al recurso statico


@app.get("/")
async def root():
    return "hola fastapi!"

@app.get ("/url")
async def url():
    return {"url" : "https://github.com/Gabitoto"}