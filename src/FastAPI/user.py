from fastapi import FastAPI
from pydantic import BaseModel

#iniciar server: uvicorn users:app --reload

app = FastAPI()

# entidad user
class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int

user_list = [User(name = "Lucas", surname = "Gabirondo", url = "https://github.com/Gabitoto", age = 24),
             User(name = "Martin", surname = "Varano", url = "https://github.com/Gabi", age = 26),
             User(name = "Maximilian", surname = "Della Rovere", url = "https://github.com/Gatoto", age = 27)]

@app.get("/usersjso")
async def usersjso():
    return [{"name":"Lucas","surname":"Gabirondo","url":"https://github.com/Gabitoto"},
            {"name":"Martin","surname":"Varano","url":"https://github.com/Gabitoto"},
            {"name":"Maximiliano","surname":"Di Crotone","url":"https://github.com/Gabitoto"}]

@app.get("/users")
async def users():
    return user_list