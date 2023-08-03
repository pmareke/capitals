from expects import equal, expect, have_key, have_len
from http import HTTPStatus
from main import app
from fastapi.testclient import TestClient


class TestCapitalsControllerAcceptance:

    def test_find_play_capitals_game(self) -> None:
        client = TestClient(app)

        response = client.get("/api/v1/play")

        expect(response.status_code).to(equal(HTTPStatus.OK))
        expect(response.json()).to(have_key("country"))
        expect(response.json()["capitals"]).to(have_len(3))

    def test_wins_capitals_game(self) -> None:
        client = TestClient(app)
        payload = {"country": "Spain", "capital": "Madrid"}

        response = client.post("/api/v1/solve", json=payload)

        expect(response.status_code).to(equal(HTTPStatus.OK))
        expect(response.json()).to(equal({"ok": True}))

    def test_loses_capitals_game(self) -> None:
        client = TestClient(app)
        payload = {"country": "Spain", "capital": "Barcelona"}

        response = client.post("/api/v1/solve", json=payload)

        expect(response.status_code).to(equal(HTTPStatus.OK))
        expect(response.json()).to(equal({"ok": False, "capital": "Madrid"}))
