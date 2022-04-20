from typing import List, Dict

import pytest

from infra.swapi_api_consumer import SwapiApiConsumer


class TestSwapiApiConsumer:
    def test_should_return_a_starship_list_dictionary_when_status_code_is_200(self) -> List[Dict]:
        page: int = 1

        instance = SwapiApiConsumer()
        response = instance.get_starships(page=page)

        assert response.json()

    def test_should_raise_error_for_status_different_than_200(self) -> int:
        instance = SwapiApiConsumer()
        response = instance.get_starships(page=1)

        assert response.status_code == 200

    @pytest.mark.skip
    def test_when_a_page_does_not_exist(self):
        instance = SwapiApiConsumer()
        response = instance.get_starships(page=500)

    @pytest.mark.skip
    def test_when_the_status_code_is_different_from_200(self, requests_mock):
        requests_mock.get("https://swapi.dev/api/starships/", status_code=404, json="raise exception")

        instance = SwapiApiConsumer()
        response = instance.get_starships(page=1)
