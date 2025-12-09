from fastapi import APIRouter
router = APIRouter()

@router.get("/restartsw/{location}")
async def restart_switch(location: str):
    # Logic to restart the switch at the given location
    return {"message": f"Switch at {location} is being restarted."}