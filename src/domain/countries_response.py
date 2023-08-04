from dataclasses import dataclass
from typing import List


@dataclass
class CountriesResponse:
    flag: str
    countries: List[str]
