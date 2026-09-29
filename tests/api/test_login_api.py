import pytest


@pytest.mark.api
def test_login_success_redirects_to_welcome(client):
    response = client.post("/login", data={"username": "admin", "password": "admin123"})
    assert response.status_code == 302
    assert "/welcome" in response.headers["Location"]

@pytest.mark.api
def test_login_failure_shows_error(client):
    response = client.post("/login", data={"username": "admin", "password": "wrong"})
    assert response.status_code == 200
    assert b"Invalid username or password" in response.data

@pytest.mark.api
def test_welcome_requires_login(client):
    response = client.get("/welcome")
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]
