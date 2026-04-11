# from api.update.update_api import updateAPI
# from api.create.create_api import createAPI
# from utils.read_data import read_json
#
# update_api = updateAPI()
# create_api = createAPI()
#
# def test_update(auth_data, headers):
#     payload = read_json('test_data/update_data.json')
#     payloadCreate = read_json('test_data/create_data.json')
#
#     responseCreate = create_api.post_create(payloadCreate)
#     res_json = responseCreate.json()
#     booking_id = res_json['bookingid']
#
#     response = update_api.put_update(booking_id, payload, headers)
#
#     assert response.status_code in [200, 201], response.status_code
#
#     print(response.status_code)