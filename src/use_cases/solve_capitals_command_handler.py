from typing import List
import uuid

from src.domain.command import Command
from src.domain.command_handler import CommandHandler
from src.domain.command_response import CommandResponse
from src.domain.countries_repository import CountriesRepository


class SolveCapitalsCommand(Command):

    def __init__(self, country: str, capital: str) -> None:
        self.country = country
        self.capital = capital
        super().__init__(uuid.uuid1())


class SolveCapitalsCommandResponse(CommandResponse):

    def __init__(self, is_solved: bool, capital: str | None) -> None:
        self.is_solved = is_solved
        self.capital = capital


class SolveCapitalsCommandHandler(CommandHandler):

    def __init__(self, repository: CountriesRepository):
        self.repository = repository

    def process(self,
                command: SolveCapitalsCommand) -> SolveCapitalsCommandResponse:
        country = self.repository.find_country(command.country)
        is_solved = country.capital == command.capital
        capital = None if is_solved else country.capital
        return SolveCapitalsCommandResponse(is_solved, capital)
