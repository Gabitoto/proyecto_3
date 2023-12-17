from fastapi import FastAPI
from pydantic import BaseModel

#iniciar server: uvicorn user:app --reload

app = FastAPI()

# entidad user
class User(BaseModel):
    id: int
    name: str
    surname: str
    url: str
    age: int

user_list = [User(id= 1, name = "Lucas", surname = "Gabirondo", url = "https://github.com/Gabitoto", age = 24),
             User(id= 2, name = "Martin", surname = "Varano", url = "https://github.com/Gabi", age = 26),
             User(id= 3, name = "Maximilian", surname = "Della Rovere", url = "https://github.com/Gatoto", age = 27)]

@app.get("/usersjso")
async def usersjso():
    return [{"name":"Lucas","surname":"Gabirondo","url":"https://github.com/Gabitoto"},
            {"name":"Martin","surname":"Varano","url":"https://github.com/Gabitoto"},
            {"name":"Maximiliano","surname":"Di Crotone","url":"https://github.com/Gabitoto"}]

@app.get("/users")
async def users():
    return user_list

#PATH

@app.get("/users/{id}")
async def user(id: int):
    return search_user(id)
    
#acabamos de mejorar el codigo viendo que era un PATH en la misma encontramos la informacion que queremos dentro de los datos que ya poseemos    

#QUERY
    
@app.get("/userquery/")
async def user(id: int):
    return search_user(id)
    
    
def search_user(id : int):
    users = filter(lambda user : user . id == id , user_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "No se a encontrado el usuario"}

#entonces dentro del GET tenemos estas dos formas de llamar a la informacion a traves del PATH o el QUERY.
