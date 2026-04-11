from core.base_api import BaseAPI
from utils.config import BASE_URL

class updateAPI:
    def __init__(self):
        self.api = BaseAPI(BASE_URL)

    def put_update(self, booking_id, payload, headers):
        return self.api.put(f'/booking/{booking_id}', json=payload, headers=headers)