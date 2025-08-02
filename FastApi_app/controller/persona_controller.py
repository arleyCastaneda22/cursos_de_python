from model.persona_model import Personas


lista_de_personas=[]

async def create_personal(data: Personas):
    lista_de_personas.append(data)
    return data