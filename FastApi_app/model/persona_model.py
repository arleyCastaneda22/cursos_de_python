from pydantic import BaseModel


class Personas(BaseModel):
    id_persona: int
    nombre : str
    edad : int

