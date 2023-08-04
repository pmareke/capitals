from dataclasses import dataclass


@dataclass
class SolveCountriesResponse:
    ok: bool
    country: str | None
