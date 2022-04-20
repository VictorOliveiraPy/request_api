from data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface
from domain.usecases.starships_colector import AbstractStarships
from typing import List, Dict, Type


class StartShipsListColector(AbstractStarships):
    def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
        self._api_consumer = api_consumer

    def get(self, page: int) -> List[Dict]:
        response = self._api_consumer.get_starships(page)
