import pytest

from infra.swapi_api_consumer import SwapiApiConsumer


class TestSwapiApiConsumer:
    def test_when_you_do_a_get_and_return_answer(self):
        page: int = 1

        instance = SwapiApiConsumer()
        response = instance.get_starships(page=page)

        assert response.json()

    def test_when_it_does_a_get_and_return_status_code_200(self):
        instance = SwapiApiConsumer()
        response = instance.get_starships(page=1)

        assert response.status_code == 200

    @pytest.mark.skip
    def test_when_the_status_code_is_different_from_200(self, requests_mock):
        requests_mock.get("https://swapi.dev/api/starships/", status_code=404, json="raise exception")

        instance = SwapiApiConsumer()
        response = instance.get_starships(page=1)

