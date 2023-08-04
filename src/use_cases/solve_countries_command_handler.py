import uuid

from src.domain.command import Command
from src.domain.command_handler import CommandHandler
from src.domain.command_response import CommandResponse
from src.domain.countries_repository import CountriesRepository
from src.domain.exceptions import NotFoundCountryException


class SolveCountriesCommand(Command):

    def __init__(self, flag: str, country: str) -> None:
        self.flag = flag
        self.country = country
        super().__init__(uuid.uuid1())


class SolveCountriesCommandResponse(CommandResponse):

    def __init__(self, is_solved: bool, country: str | None) -> None:
        self.is_solved = is_solved
        self.country = country


class SolveCountriesCommandHandler(CommandHandler):

    def __init__(self, repository: CountriesRepository):
        self.repository = repository

    def process(self, command: SolveCountriesCommand) -> SolveCountriesCommandResponse:
        country = self.repository.find_country(command.country)
        if not country:
            raise NotFoundCountryException()
        country_by_flag = self.repository.find_country_by_flag(command.flag)
        if not country_by_flag:
            raise NotFoundCountryException()
        is_solved = country.flag.image == command.flag
        valid_country = None if is_solved else country_by_flag.name
        return SolveCountriesCommandResponse(is_solved, valid_country)
