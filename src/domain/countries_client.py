from abc import ABC, abstractmethod
from typing import List

from src.domain.country import Country


class CountriesClient(ABC):

    @abstractmethod
    def find_all(self) -> List[Country]:
        raise NotImplementedError
