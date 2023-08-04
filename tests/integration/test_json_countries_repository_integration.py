from expects import be_none, equal, expect, have_len
from src.infrastructure.json_countries_repository import JsonCountriesRepository


class TestJsonCountriesRepositoryIntegration:

    def test_find_countries(self) -> None:
        countries_repository = JsonCountriesRepository()

        countries = countries_repository.find_countries(total=3)

        expect(countries).to(have_len(3))
        expect(countries[0].name).not_to(be_none)
        expect(countries[0].capital).not_to(be_none)
        expect(countries[0].flag).not_to(be_none)

    def test_find_country(self) -> None:
        countries_repository = JsonCountriesRepository()

        country = countries_repository.find_country("Spain")

        expect(country.capital).to(equal("Madrid"))
