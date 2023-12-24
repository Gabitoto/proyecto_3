from fastapi import APIRouter #recordemos que al agregar APIRouter permitimos que esto sea una extension de la API

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses={404:{"message":"No encontrado"}}) #agregamos un prefijo lo cual nos ayuda a no tener que agregar en cada operacion un prefijo.

products_list = ["producto_1","producto_2","producto_3","producto_4","producto_5"]

@router.get("/")
async def products():
    return products_list

@router.get("/{id}")
async def products(id:int):
    return products_list[id]