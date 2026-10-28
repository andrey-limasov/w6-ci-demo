from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_version() -> None:
    response = client.get("/version")
    assert response.status_code == 200
    assert response.json() == {"version": "0.1.0"}


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
