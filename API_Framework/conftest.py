import pytest

from api.create.create_api import createAPI
from core.auth import get_auth_data
from utils.read_data import read_json


@pytest.fixture(scope="session")
def auth_data():
    return get_auth_data()

@pytest.fixture(scope="session")
def headers(auth_data):
    return {
        "Cookie": f"token={auth_data}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

@pytest.fixture(scope="session")
def booking_id(headers):
    api = createAPI()
    payload = read_json('test_data/create_data.json')
    response = api.post_create(payload)
    assert response.status_code in [200, 201]
    return response.json()["bookingid"]