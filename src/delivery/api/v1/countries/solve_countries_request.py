from dataclasses import dataclass


@dataclass
class SolveCountriesRequest:
    flag: str
    country: str
