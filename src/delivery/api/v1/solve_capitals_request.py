from dataclasses import dataclass


@dataclass
class SolveCapitalsRequest:
    country: str
    capital: str
