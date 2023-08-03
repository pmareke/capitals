from expects import equal, expect, have_key, have_len
from http import HTTPStatus
from main import app
from fastapi.testclient import TestClient


class TestCapitalsControllerAcceptance:

    def test_find_play_capitals_game(self) -> None:
        client = TestClient(app)

        response = client.get("/api/v1/play")

        expect(response.status_code).to(equal(HTTPStatus.OK))
        expect(response.json()).to(have_key("countries"))
        expect(response.json()["countries"]).to(have_len(3))
