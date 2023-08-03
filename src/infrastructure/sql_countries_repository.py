import random
import sqlite3

from sqlite3 import Cursor
from typing import Dict, List
from src.domain.countries_client import CountriesClient
from src.domain.countries_repository import CountriesRepository
from src.domain.country import Country


class SqlCountriesRepository(CountriesRepository):

    def __init__(self, countries_client: CountriesClient) -> None:
        self.countries_client = countries_client
        self.countries_cache: Dict[str, Country] = {}

    def find_countries(self, total: int = 3) -> List[Country]:
        if not self.countries_cache:
            self.countries_cache = self._find_countries()
        countries: List[Country] = [
            country for country in self.countries_cache.values()
        ]
        return random.sample(countries, total)

    def _find_countries(self) -> Dict[str, Country]:
        con = sqlite3.connect("countries.db")
        cursor = con.cursor()
        countries = self.countries_client.find_all()
        cursor.execute("DROP TABLE IF EXISTS countries")
        cursor.execute(
            "CREATE TABLE countries(name, capital, flag_url, flag_alt)")
        self._insert_countries_into_db(cursor, countries)
        return {country.name: country for country in countries}

    def _insert_countries_into_db(self, cursor: Cursor,
                                  countries: List[Country]) -> None:
        values = [(country.name, country.capital, country.flag.image,
                   country.flag.alt) for country in countries]
        cursor.executemany(
            f"INSERT INTO countries(name, capital, flag_url, flag_alt) VALUES (?, ?, ?, ?)",
            values)
