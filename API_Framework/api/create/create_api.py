from core.base_api import BaseAPI
from utils.config import BASE_URL

class createAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def post_create(self, payload):
        return self.api.post(f'/booking', json=payload)