from fastapi import APIRouter, Depends
from src.infrastructure.json_countries_repository import JsonCountriesRepository

from src.domain.command_handler import CommandHandler
from src.domain.capitals_response import CapitalsResponse, CountryResponse
from src.domain.region import Region
from src.use_cases.play_capitals_command_handler import PlayCapitalsCommand, PlayCapitalsCommandHandler, PlayCapitalsCommandResponse

play_capitals_router = APIRouter()


async def _play_capitals_command_handler() -> CommandHandler:
    countries_repository = JsonCountriesRepository()
    return PlayCapitalsCommandHandler(countries_repository)


@play_capitals_router.get("/api/v1/capitals/play", response_model=CapitalsResponse)
def play_capitals(region: Region | None = None, handler: PlayCapitalsCommandHandler = Depends(
    _play_capitals_command_handler)) -> CapitalsResponse:
    enum_region = Region(region) if region else None
    command = PlayCapitalsCommand(enum_region)
    response = handler.process(command)
    country_response = CountryResponse(response.country.name,
                                       response.country.flag)
    capitals = response.capitals
    return CapitalsResponse(country_response, capitals)
