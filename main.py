from fastapi import FastAPI

from src.delivery.api.v1.status_router import status_router
from src.delivery.api.v1.capitals.play_capitals_router import play_capitals_router
from src.delivery.api.v1.capitals.solve_capitals_router import solve_capitals_router
from src.delivery.api.v1.countries.play_countries_router import play_countries_router
from src.delivery.api.v1.countries.solve_countries_router import solve_countries_router

app = FastAPI()

app.include_router(status_router)
app.include_router(play_capitals_router)
app.include_router(solve_capitals_router)
app.include_router(play_countries_router)
app.include_router(solve_countries_router)
