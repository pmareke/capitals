from fastapi import FastAPI
from src.delivery.api.v1.status_router import status_router

app = FastAPI()

app.include_router(status_router)
