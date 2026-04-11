import pytest
from core.auth import get_auth_data

@pytest.fixture(scope="session")
def auth_data():
    return get_auth_data()

@pytest.fixture(scope="session")
def headers(auth_data):
    return {
        "Cookie": f"{auth_data['token']}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
