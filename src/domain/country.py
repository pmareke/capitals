from dataclasses import dataclass

from src.domain.flag import Flag


@dataclass
class Country:
    name: str
    capital: str
    flag: Flag
    region: str
