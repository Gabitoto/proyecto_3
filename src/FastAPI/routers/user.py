from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

#iniciar server: uvicorn user:app --reload

router = APIRouter()

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

@router.get("/usersjso")
async def usersjso():
    return [{"name":"Lucas","surname":"Gabirondo","url":"https://github.com/Gabitoto"},
            {"name":"Martin","surname":"Varano","url":"https://github.com/Gabitoto"},
            {"name":"Maximiliano","surname":"Di Crotone","url":"https://github.com/Gabitoto"}]

@router.get("/users")
async def users():
    return user_list

#PATH

@router.get("/users/{id}")
async def user(id: int):
    return search_user(id)
    
#acabamos de mejorar el codigo viendo que era un PATH en la misma encontramos la informacion que queremos dentro de los datos que ya poseemos    

#QUERY
    
@router.get("/userquery/")
async def user(id: int):
    return search_user(id)
    
@router.post("/user/", status_code= 201)
async def user(user: User):
    if type(search_user(user.id)) == User:
         raise HTTPException (status_code= 204, detail= "El usuario ya existe")
    else:
        user_list.append(user)
        return user

@router.put ("/user/") 
async def user(user:User):

    found = False

    for index,saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True
    
    if not found:
        return {"Error": "No se a actualizado el usuario"}
    else:
        return user 


@router.delete("/user/{id}") # DELETE para borrar datos
async def user(id: int):
    found = False
    for index,saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True
    if not found:
        return {"Error": "No se a eliminado el usuario"}



def search_user(id : int):
    users = filter(lambda user : user . id == id , user_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "No se a encontrado el usuario"}

# Entonces dentro del GET tenemos estas dos formas de llamar a la informacion a traves del PATH o el QUERY.
# Debemos ver las operaciones POST para agregar datos 
# Y las PUT para actualizar datos

