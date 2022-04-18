import requests


class SwapiApiConsumer:
    def __int__(self):
        self.api_host = "https://swapi.dev/api/starships/"

    def get_starships(self, page: int) -> any:
        params = {'page': page}

        response = requests.get("https://swapi.dev/api/starships/", params=params)
        response = response.json()

        return response
