from fastapi import FastAPI
from memory.routers import router
app = FastAPI()
app.include_router(router)
