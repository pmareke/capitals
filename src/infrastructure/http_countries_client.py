import requests

from typing import Dict, List
from src.domain.countries_client import CountriesClient
from src.domain.country import Country
from src.domain.flag import Flag


class HttpCountriesClient(CountriesClient):

    def find_all(self) -> List[Country]:
        response = requests.get(
            "https://restcountries.com/v3.1/all?fields=name,capital,flags")
        json_response = response.json()
        countries: List[Country] = []
        for item in json_response:
            if item["capital"]:
                country = self._generate_country(item)
                countries.append(country)
        return countries

    @staticmethod
    def _generate_country(item: Dict) -> Country:
        name = item["name"]["common"]
        capital = item["capital"][0]
        flag = Flag(item["flags"]["svg"], item["flags"]["alt"])
        return Country(name, capital, flag)
