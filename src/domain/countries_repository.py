from abc import ABC, abstractmethod
from typing import List

from src.domain.country import Country
from src.domain.region import Region


class CountriesRepository(ABC):
    @abstractmethod
    def find_countries(self, region: Region | None = None) -> List[Country]:
        raise NotImplementedError

    @abstractmethod
    def find_country(self, country: str) -> Country | None:
        raise NotImplementedError

    @abstractmethod
    def find_country_by_flag(self, flag: str) -> Country | None:
        raise NotImplementedError
