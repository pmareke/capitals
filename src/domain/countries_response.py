from dataclasses import dataclass
from typing import List

from src.domain.flag import Flag


@dataclass
class CountryResponse:
    name: str
    flag: Flag


@dataclass
class CountriesResponse:
    countries: List[CountryResponse]
