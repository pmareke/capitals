from typing import List
import uuid

from src.domain.command import Command
from src.domain.command_handler import CommandHandler
from src.domain.command_response import CommandResponse
from src.domain.countries_repository import CountriesRepository
from src.domain.country import Country


class PlayCapitalsCommand(Command):

    def __init__(self) -> None:
        super().__init__(uuid.uuid1())


class PlayCapitalsCommandResponse(CommandResponse):

    def __init__(self, countries: List[Country]) -> None:
        self.countries = countries


class PlayCapitalsCommandHandler(CommandHandler):

    def __init__(self, repository: CountriesRepository):
        self.repository = repository

    def process(self,
                _command: PlayCapitalsCommand) -> PlayCapitalsCommandResponse:
        countries = self.repository.find_countries()
        return PlayCapitalsCommandResponse(countries)
