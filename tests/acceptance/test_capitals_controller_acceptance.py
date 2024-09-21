from expects import equal, expect, have_key, have_len
from http.client import BAD_REQUEST, OK
from main import app
from fastapi.testclient import TestClient


class TestCapitalsControllerAcceptance:
    def test_plays_capitals_game(self) -> None:
        client = TestClient(app)

        response = client.get("/api/v1/capitals/play")

        expect(response.status_code).to(equal(OK))
        expect(response.json()).to(have_key("country"))
        expect(response.json()["capitals"]).to(have_len(3))

    def test_plays_capitals_game_in_europe(self) -> None:
        client = TestClient(app)

        response = client.get("/api/v1/capitals/play?region=europe")

        expect(response.status_code).to(equal(OK))
        expect(response.json()).to(have_key("country"))
        expect(response.json()["capitals"]).to(have_len(3))

    def test_wins_capitals_game(self) -> None:
        client = TestClient(app)
        payload = {"country": "Spain", "capital": "Madrid"}

        response = client.post("/api/v1/capitals/solve", json=payload)

        expect(response.status_code).to(equal(OK))
        expect(response.json()).to(equal({"ok": True}))

    def test_loses_capitals_game(self) -> None:
        client = TestClient(app)
        payload = {"country": "Spain", "capital": "Barcelona"}

        response = client.post("/api/v1/capitals/solve", json=payload)

        expect(response.status_code).to(equal(OK))
        expect(response.json()).to(equal({"ok": False, "capital": "Madrid"}))

    def test_send_invalid_payload(self) -> None:
        client = TestClient(app)
        payload = {"country": "non-existing-country", "capital": "Barcelona"}

        response = client.post("/api/v1/capitals/solve", json=payload)

        expect(response.status_code).to(equal(BAD_REQUEST))
