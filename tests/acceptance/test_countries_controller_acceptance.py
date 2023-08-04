from expects import equal, expect, have_key, have_len
from http import HTTPStatus
from main import app
from fastapi.testclient import TestClient


class TestCountriesControllerAcceptance:

    def test_find_play_countries_game(self) -> None:
        client = TestClient(app)

        response = client.get("/api/v1/countries/play")

        expect(response.status_code).to(equal(HTTPStatus.OK))
        expect(response.json()).to(have_key("flag"))
        expect(response.json()["countries"]).to(have_len(3))

    def test_wins_countries_game(self) -> None:
        client = TestClient(app)
        payload = {"flag": "https://flagcdn.com/es.svg", "country": "Spain"}

        response = client.post("/api/v1/countries/solve", json=payload)

        expect(response.status_code).to(equal(HTTPStatus.OK))
        expect(response.json()).to(equal({"ok": True}))

    def test_loses_countries_game(self) -> None:
        client = TestClient(app)
        payload = {"flag": "https://flagcdn.com/es.svg", "country": "France"}

        response = client.post("/api/v1/countries/solve", json=payload)

        expect(response.status_code).to(equal(HTTPStatus.OK))
        expect(response.json()).to(equal({"ok": False, "country": "Spain"}))

    def test_send_invalid_payload(self) -> None:
        client = TestClient(app)
        payload = {"flag": "https://flagcdn.com/es.svg", "country": "any-non-existing-country"}

        response = client.post("/api/v1/countries/solve", json=payload)

        expect(response.status_code).to(equal(HTTPStatus.BAD_REQUEST))
