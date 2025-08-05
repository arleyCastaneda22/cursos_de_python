from model.persona_model import Personas
from fastapi import HTTPException


lista_de_personas=[]

async def create_personal(data: Personas):

    try:

        lista_de_personas.append(data)
        return data

    except:
        raise HTTPException(
        status_code=404,
        detail="No funciona está mierda"
    )