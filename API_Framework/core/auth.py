from api.auth.auth_api import authAPI
from utils.read_data import read_json

auth_api = authAPI()

def get_auth_data():
    payload = read_json('test_data/auth_data.json')

    response = auth_api.post_auth(payload)
    assert response.status_code == 200
    res_json = response.json()
    token = res_json['token']

    print("STATUS:", response.status_code)
    print("RESPONSE: ", response.json())

    return token