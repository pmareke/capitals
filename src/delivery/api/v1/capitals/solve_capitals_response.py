from dataclasses import dataclass


@dataclass
class SolveCapitalsResponse:
    ok: bool
    capital: str | None
