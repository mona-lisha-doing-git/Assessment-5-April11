from api.update.update_api import updateAPI
from utils.read_data import read_json

update_api = updateAPI()

def test_update(headers,booking_id):
    payload = read_json('test_data/update_data.json')

    response = update_api.put_update(booking_id, payload, headers=headers)
    assert response.status_code == 200 , response.json()

    print(response.status_code)