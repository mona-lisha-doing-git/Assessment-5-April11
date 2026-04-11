import requests

class BaseAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoints, headers=None, params=None):
        return self.session.get(f'{self.base_url}{endpoints}', headers=headers, params=params, verify=False)

    def post(self, endpoints, headers=None, json=None):
        return self.session.post(f'{self.base_url}{endpoints}', headers=headers, json=json, verify=False)

    def put(self, endpoints, headers=None, json=None):
        return self.session.put(f'{self.base_url}{endpoints}', headers=headers, json=json, verify=False)
