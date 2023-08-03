from typing import List
import uuid
import random

from src.domain.command import Command
from src.domain.command_handler import CommandHandler
from src.domain.command_response import CommandResponse
from src.domain.countries_repository import CountriesRepository
from src.domain.country import Country


class PlayCapitalsCommand(Command):

    def __init__(self) -> None:
        super().__init__(uuid.uuid1())


class PlayCapitalsCommandResponse(CommandResponse):

    def __init__(self, country: Country, capitals: List[str]) -> None:
        self.country = country
        self.capitals = capitals


class PlayCapitalsCommandHandler(CommandHandler):

    def __init__(self, repository: CountriesRepository):
        self.repository = repository

    def process(self, _command: PlayCapitalsCommand) -> PlayCapitalsCommandResponse:
        countries = self.repository.find_countries()
        country: Country = random.sample(countries, 1)[0]
        capitals = [country.capital for country in countries]
        return PlayCapitalsCommandResponse(country, capitals)
