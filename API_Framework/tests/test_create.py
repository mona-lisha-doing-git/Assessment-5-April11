from api.create.create_api import createAPI
from utils.read_data import read_json

create_api = createAPI()

def test_create():
    payload = read_json('test_data/create_data.json')

    response = create_api.post_create(payload)

    assert response.status_code in [200, 201], response.status_code

    print(response.status_code)

def test_create_invalid():
    payload = read_json('test_data/create_data_nv.json')
    response = create_api.post_create(payload)
    assert response.status_code not in [200,201], response.status_code