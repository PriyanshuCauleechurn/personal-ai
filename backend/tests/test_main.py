from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_chat():
    response = client.post(
        "/chat",
        json={"message": "Hello AI"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "reply": "You said: Hello AI"
        }

def test_empty():
    response = client.post(
        "/chat",
        json={"message": ""}
    )

    assert response.status_code == 422