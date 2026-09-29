import pytest

from app import USERS


@pytest.mark.unit
def test_valid_user_exists():
    assert "admin" in USERS
    assert USERS["admin"] == "admin123"

@pytest.mark.unit
def test_invalid_user_not_in_store():
    assert "hacker" not in USERS

@pytest.mark.unit
def test_all_passwords_are_non_empty():
    for username, password in USERS.items():
        assert password, f"Empty password for {username}"
