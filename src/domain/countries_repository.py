from abc import ABC, abstractmethod
from typing import List

from src.domain.country import Country


class CountriesRepository(ABC):

    @abstractmethod
    def find_countries(self, region: str | None = None) -> List[Country]:
        raise NotImplementedError

    @abstractmethod
    def find_country(self, country: str) -> Country | None:
        raise NotImplementedError

    @abstractmethod
    def find_country_by_flag(self, country: str) -> Country:
        raise NotImplementedError
