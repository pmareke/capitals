from expects import be_none, expect, have_len

from src.infrastructure.http_countries_client import HttpCountriesClient
from src.infrastructure.sql_countries_repository import SqlCountriesRepository


class TestSqlCountriesRepositoryIntegration:

    def test_find_countries(self) -> None:
        countries_client = HttpCountriesClient()
        countries_repository = SqlCountriesRepository(countries_client)

        countries = countries_repository.find_countries(total=3)

        expect(countries).to(have_len(3))
        expect(countries[0].name).not_to(be_none)
        expect(countries[0].capital).not_to(be_none)
        expect(countries[0].flag).not_to(be_none)
