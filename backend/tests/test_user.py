from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_register():
    response = client.post("/api/user/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "display_name": "Test User",
        "password": "123456"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "testuser"