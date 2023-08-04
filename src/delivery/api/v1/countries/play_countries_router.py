from fastapi import APIRouter, Depends
from src.domain.countries_response import CountriesResponse

from src.domain.command_handler import CommandHandler
from src.domain.capitals_response import CapitalsResponse
from src.infrastructure.json_countries_repository import JsonCountriesRepository
from src.use_cases.play_countries_command_handler import PlayCountriesCommand, PlayCountriesCommandHandler, PlayCountriesCommandResponse

play_countries_router = APIRouter()


async def _play_countries_command_handler() -> CommandHandler:
    countries_repository = JsonCountriesRepository()
    return PlayCountriesCommandHandler(countries_repository)


@play_countries_router.get("/api/v1/countries/play", response_model=CountriesResponse)
def play_countries(handler: PlayCountriesCommandHandler = Depends(
    _play_countries_command_handler)) -> CountriesResponse:
    command = PlayCountriesCommand()
    response = handler.process(command)
    flag = response.flag.image
    countries = response.countries
    return CountriesResponse(flag, countries)
