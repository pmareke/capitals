import json
import random

from collections import defaultdict
from typing import Dict, List

from src.domain.flag import Flag

from src.domain.countries_repository import CountriesRepository
from src.domain.country import Country
from src.domain.region import Region


class JsonCountriesRepository(CountriesRepository):
    TOTAL_NUMBER_OF_COUNTRIES = 3

    def __init__(self) -> None:
        self.countries: Dict[str, Country] = self._generate_countries()
        self.countries_by_region: Dict[str, List[Country]] = self._generate_countries_by_region()

    def find_countries(self, region: Region | None = None) -> List[Country]:
        if region:
            countries = self.countries_by_region[region.value]
        else:
            countries = [country for country in self.countries.values()]
        return random.sample(countries, self.TOTAL_NUMBER_OF_COUNTRIES)

    def find_country(self, country: str) -> Country | None:
        return self.countries.get(country)

    def find_country_by_flag(self, flag: str) -> Country | None:
        for country in self.countries.values():
            if country.flag.image == flag:
                return country
        return None

    @staticmethod
    def _generate_countries() -> Dict[str, Country]:
        countries: Dict[str, Country] = {}
        with open("countries.json") as file:
            items = json.load(file)
            for item in items:
                capitals = item["capital"]
                if capitals:
                    name = item["name"]["common"]
                    capital = capitals[0]
                    flag = Flag(item["flags"]["svg"])
                    region = item["region"].lower()
                    country = Country(name, capital, flag, region)
                    countries[name] = country
        return countries

    def _generate_countries_by_region(self,) -> Dict[str, List[Country]]:
        countries_by_region: Dict[str, List[Country]] = defaultdict(list)
        for country in self.countries.values():
            countries_by_region[country.region].append(country)
        return countries_by_region
