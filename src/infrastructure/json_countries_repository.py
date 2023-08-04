import json
import random

from typing import Dict, List

from src.domain.flag import Flag

from src.domain.countries_repository import CountriesRepository
from src.domain.country import Country


class JsonCountriesRepository(CountriesRepository):

    def __init__(self) -> None:
        self.countries: Dict[str, Country] = self._generate_countries()

    def find_countries(self, total: int = 3) -> List[Country]:
        countries = [c for c in self.countries.values()]
        return random.sample(countries, total)

    def find_country(self, country: str) -> Country:
        return self.countries[country]

    @staticmethod
    def _generate_countries() -> Dict[str, Country]:
        countries:  Dict[str, Country] = {}
        with open("countries.json") as file:
            items = json.load(file)
            for item in items:
                capitals = item["capital"]
                if capitals:
                    name = item["name"]["common"]
                    flag = Flag(item["flags"]["svg"])
                    country = Country(
                        name=name,
                        capital=capitals[0],
                        flag=flag
                    )
                    countries[name] = country
        return countries
