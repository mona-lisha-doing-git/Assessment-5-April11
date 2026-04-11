from core.base_api import BaseAPI
from utils.config import BASE_URL

class authAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def post_auth(self, payload):
        return self.api.post('/auth', json=payload)