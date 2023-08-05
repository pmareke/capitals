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

        assert country
        expect(country.capital).to(equal("Madrid"))

    def test_find_non_existing_country(self) -> None:
        countries_repository = JsonCountriesRepository()

        country = countries_repository.find_country("non-existing")

        expect(country).to(be_none)

    def test_find_country_by_flag(self) -> None:
        countries_repository = JsonCountriesRepository()

        country = countries_repository.find_country_by_flag("https://flagcdn.com/es.svg")

        assert country
        expect(country.name).to(equal("Spain"))

    def test_find_non_existing_country_by_flag(self) -> None:
        countries_repository = JsonCountriesRepository()

        country = countries_repository.find_country_by_flag("non-existing")

        expect(country).to(be_none)
