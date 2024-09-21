from http.client import BAD_REQUEST

from fastapi import APIRouter, Depends, HTTPException

from src.domain.exceptions import NotFoundCountryException
from src.infrastructure.json_countries_repository import JsonCountriesRepository

from src.delivery.api.v1.countries.solve_countries_request import SolveCountriesRequest
from src.delivery.api.v1.countries.solve_countries_response import (
    SolveCountriesResponse,
)

from src.domain.command_handler import CommandHandler
from src.use_cases.solve_countries_command_handler import (
    SolveCountriesCommand,
    SolveCountriesCommandHandler,
)

solve_countries_router = APIRouter()


async def _solve_countries_command_handler() -> CommandHandler:
    countries_repository = JsonCountriesRepository()
    return SolveCountriesCommandHandler(countries_repository)


@solve_countries_router.post(
    "/api/v1/countries/solve",
    response_model=SolveCountriesResponse,
    response_model_exclude_none=True,
)
def solve_countries(
    solve_countries_request: SolveCountriesRequest,
    handler: SolveCountriesCommandHandler = Depends(_solve_countries_command_handler),
) -> SolveCountriesResponse:
    flag = solve_countries_request.flag
    country = solve_countries_request.country
    command = SolveCountriesCommand(flag, country)

    try:
        response = handler.process(command)
        return SolveCountriesResponse(response.is_solved, response.country)
    except NotFoundCountryException as exception:
        raise HTTPException(
            status_code=BAD_REQUEST, detail=f"The fk is not valid"
        ) from exception
