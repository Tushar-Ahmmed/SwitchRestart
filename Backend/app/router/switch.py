from fastapi import APIRouter
from services.switch import switch_restart_service
router = APIRouter()

@router.get("/restartsw/{location}")
async def restart_switch(location: str):
    return switch_restart_service(location)