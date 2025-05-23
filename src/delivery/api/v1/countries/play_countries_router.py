from fastapi import APIRouter, Depends
from src.domain.countries_response import CountriesResponse

from src.domain.command_handler import CommandHandler
from src.domain.region import Region
from src.infrastructure.json_countries_repository import JsonCountriesRepository
from src.use_cases.play_countries_command_handler import (
    PlayCountriesCommand,
    PlayCountriesCommandHandler,
)

play_countries_router = APIRouter()


async def _play_countries_command_handler() -> CommandHandler:
    countries_repository = JsonCountriesRepository()
    return PlayCountriesCommandHandler(countries_repository)


@play_countries_router.get("/api/v1/countries/play", response_model=CountriesResponse)
def play_countries(
    region: Region | None = None,
    handler: PlayCountriesCommandHandler = Depends(_play_countries_command_handler),
) -> CountriesResponse:
    command = PlayCountriesCommand(region)
    response = handler.process(command)
    flag = response.flag.image
    countries = response.countries
    return CountriesResponse(flag, countries)
