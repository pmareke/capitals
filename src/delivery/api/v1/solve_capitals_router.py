from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException

from src.domain.exceptions import NotFoundCountryException
from src.infrastructure.json_countries_repository import JsonCountriesRepository

from src.delivery.api.v1.solve_capitals_request import SolveCapitalsRequest
from src.delivery.api.v1.solve_capitals_response import SolveCapitalsResponse

from src.domain.command_handler import CommandHandler
from src.use_cases.solve_capitals_command_handler import SolveCapitalsCommand, SolveCapitalsCommandHandler

solve_capitals_router = APIRouter()


async def _solve_capitals_command_handler() -> CommandHandler:
    countries_repository = JsonCountriesRepository()
    return SolveCapitalsCommandHandler(countries_repository)


@solve_capitals_router.post("/api/v1/capitals/solve",
                            response_model=SolveCapitalsResponse,
                            response_model_exclude_none=True)
def solve_capitals(
    solve_capitals_request: SolveCapitalsRequest,
    handler: SolveCapitalsCommandHandler = Depends(
        _solve_capitals_command_handler)
) -> SolveCapitalsResponse:
    country = solve_capitals_request.country
    capital = solve_capitals_request.capital
    command = SolveCapitalsCommand(country, capital)

    try:
        response = handler.process(command)
        return SolveCapitalsResponse(response.is_solved, response.capital)
    except NotFoundCountryException as exception:
        raise HTTPException(status_code=HTTPStatus.BAD_REQUEST,
                            detail=f"The country is not valid") from exception
