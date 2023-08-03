from expects import be_empty, be_none, expect
from src.infrastructure.http_countries_client import HttpCountriesClient


class TestHttpCountriesClientIntegration:

    def test_find_all_countries(self) -> None:
        countries_client = HttpCountriesClient()

        countries = countries_client.find_all()

        expect(countries).not_to(be_empty)
        expect(countries[0].name).not_to(be_none)
        expect(countries[0].capital).not_to(be_none)
        expect(countries[0].flag).not_to(be_none)
