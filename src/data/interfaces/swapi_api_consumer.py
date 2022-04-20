from abc import ABC, abstractmethod


class SwapiApiConsumerInterface(ABC):
    @abstractmethod
    def get_starships(self, page: int) -> dict:
        raise NotImplemented

