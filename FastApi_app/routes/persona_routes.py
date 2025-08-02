
from fastapi import APIRouter
from controller.persona_controller import create_personal
from model.persona_model import Personas

router = APIRouter()

@router.post("/persona")
async def crear_persona(data: Personas):
    return await create_personal(data)



