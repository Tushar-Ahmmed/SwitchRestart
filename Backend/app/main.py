from fastapi import FastAPI
from router.switch import router as switch_router

app = FastAPI(title="Switch Restart Backend API", version="1.0.0")  

app.include_router(switch_router, prefix="/api")
