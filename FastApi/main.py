from fastapi import FastAPI
app = FastAPI()

app.title = "Aprendiendo FastApi"


@app.get("/")
async def hello():
    return {"message": "Hello word"}


@app.get("/all")
async def get_all():
    return {"message": "Obtuve todo"}


lista_de_que_busco=[
        {
            "id": 1,
            "Nombre": "The words person",
            "Cualidades" : ["buena", 10, 90, 30]
        }, 
        {
            "id": 2,
            "Nombre": "Lost in translation",
            "Cualidades" : ["Me revive", 60, 90, 30]
        }
    ]

@app.get("/loquebusco")
async def get_woman(id :int):
    filtro_por_id =list(filter(lambda lista :lista["id"] ==id, lista_de_que_busco))
    return filtro_por_id 



