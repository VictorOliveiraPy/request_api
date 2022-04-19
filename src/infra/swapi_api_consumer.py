import requests

from config import API_HOST
from exceptions import HttpRequestError


class SwapiApiConsumer:
    def __init__(self):
        self.api_host = API_HOST

    def get_starships(self, page: int) -> dict:
        params = {'page': page}

        response = requests.get(self.api_host, params=params)

        if not response.status_code != 200:
            return response

        raise HttpRequestError(message=response.json())


