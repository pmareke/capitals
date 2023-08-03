from fastapi import APIRouter, Depends
from src.delivery.api.v1.solve_capitals_request import SolveCapitalsRequest
from src.delivery.api.v1.solve_capitals_response import SolveCapitalsResponse

from src.domain.command_handler import CommandHandler
from src.infrastructure.http_countries_client import HttpCountriesClient
from src.infrastructure.sql_countries_repository import SqlCountriesRepository
from src.use_cases.solve_capitals_command_handler import SolveCapitalsCommand, SolveCapitalsCommandHandler

solve_capitals_router = APIRouter()


async def _solve_capitals_command_handler() -> CommandHandler:
    countries_client = HttpCountriesClient()
    countries_repository = SqlCountriesRepository(countries_client)
    return SolveCapitalsCommandHandler(countries_repository)


@solve_capitals_router.post("/api/v1/solve", response_model=SolveCapitalsResponse)
def solve_capitals(solve_capitals_request: SolveCapitalsRequest, handler: SolveCapitalsCommandHandler = Depends(
    _solve_capitals_command_handler)) -> SolveCapitalsResponse:
    country = solve_capitals_request.country
    capital = solve_capitals_request.capital
    command = SolveCapitalsCommand(country, capital)
    response = handler.process(command)
    return SolveCapitalsResponse(response.is_solved)
