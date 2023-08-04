from typing import List
import uuid
import random

from src.domain.flag import Flag

from src.domain.command import Command
from src.domain.command_handler import CommandHandler
from src.domain.command_response import CommandResponse
from src.domain.countries_repository import CountriesRepository
from src.domain.country import Country


class PlayCountriesCommand(Command):

    def __init__(self) -> None:
        super().__init__(uuid.uuid1())


class PlayCountriesCommandResponse(CommandResponse):

    def __init__(self, flag: Flag, countries: List[str]) -> None:
        self.flag = flag
        self.countries = countries


class PlayCountriesCommandHandler(CommandHandler):

    def __init__(self, repository: CountriesRepository):
        self.repository = repository

    def process(self, _command: PlayCountriesCommand) -> PlayCountriesCommandResponse:
        countries = self.repository.find_countries()
        flag: Flag = random.sample(countries, 1)[0].flag
        countries_names = [country.name for country in countries]
        return PlayCountriesCommandResponse(flag, countries_names)
