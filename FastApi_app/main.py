from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing import Optional
import pydantic
from routes.persona_routes import router

app = FastAPI()


app.include_router(router)

# app.title = "Aprendiendo FastApi"

# class lista(BaseModel):
#     id: Optional[int]
#     nombre: str
#     cualidades: list



# @app.get("/")
# async def hello():
#     return {"message": "Hello word"}


# @app.get("/all")
# async def get_all():
#     return {"message": "Obtuve todo"}


# lista_de_que_busco=[
#         {
#             "id": 1,
#             "Nombre": "The words person",
#             "Cualidades" : ["buena", 10, 90, 30]
#         }, 
#         {
#             "id": 2,
#             "Nombre": "Lost in translation",
#             "Cualidades" : ["Me revive", 60, 90, 30]
#         }
#     ]

# @app.get("/loquebusco")
# async def get_woman(id :int):
#     filtro_por_id =list(filter(lambda lista :lista["id"] ==id, lista_de_que_busco))
#     return filtro_por_id 

# @app.get("/loquebusco/{id}")
# async def get_uno(id: int):
#     todo_data =next(x for x in lista_de_que_busco if x["id"]==id)
#     return todo_data


# @app.post("/loquebusco")
# async def create_busco(data: lista):
#     lista_de_que_busco.append(data)
    
#     return data






