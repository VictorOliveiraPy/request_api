import requests

from config import API_HOST
from data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface
from exceptions import HttpRequestError


class SwapiApiConsumer(SwapiApiConsumerInterface):
    def __init__(self):
        self.api_host = API_HOST

    def get_starships(self, page: int) -> dict:
        params = {'page': page}

        response = requests.get(self.api_host, params=params)

        if not response.status_code != 200:
            return response

        raise HttpRequestError(message=response.json())


