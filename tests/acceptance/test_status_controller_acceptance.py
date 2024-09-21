from expects import equal, expect
from http.client import OK
from main import app
from fastapi.testclient import TestClient


class TestStatusControllerAcceptance:
    def test_status(self) -> None:
        client = TestClient(app)

        response = client.get("/api/v1/status")

        expect(response.status_code).to(equal(OK))
