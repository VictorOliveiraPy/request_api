import requests

from config import API_HOST
from data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface


class SwapiApiConsumer(SwapiApiConsumerInterface):
    def __init__(self):
        self.api_host = API_HOST

    def get_starships(self, page: int):
        params = {'page': page}

        response = requests.get(self.api_host, params=params)

        return response



