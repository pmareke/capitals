from dataclasses import dataclass
from typing import List

from src.domain.flag import Flag


@dataclass
class CountryResponse:
    name: str
    flag: Flag


@dataclass
class CapitalsResponse:
    country: CountryResponse
    capitals: List[str]
