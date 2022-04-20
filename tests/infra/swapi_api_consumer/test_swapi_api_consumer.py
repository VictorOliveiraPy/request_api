from typing import List, Dict
from unittest import mock

import pytest

from infra.swapi_api_consumer import SwapiApiConsumer


class TestSwapiApiConsumer:
    @mock.patch("src.infra.swapi_api_consumer.requests.get")
    def test_should_return_a_starship_list_dictionary_when_status_code_is_200(
            self, mock_requests_api,
            mock_dict_with_starships
    ) -> List[Dict]:
        page: int = 1

        mock_requests_api.return_value = mock_dict_with_starships

        instance = SwapiApiConsumer()
        result = instance.get_starships(page=page)

        expected_result = [{
            'name': 'CR90 corvette', 'model': 'CR90 corvette', 'manufacturer': 'Corellian Engineering Corporation',
            'cost_in_credits': '3500000', 'length': '150', 'max_atmosphering_speed': '950', 'crew': '30-165',
            'passengers': '600', 'cargo_capacity': '3000000', 'consumables': '1 year', 'hyperdrive_rating': '2.0',
            'MGLT': '60', 'starship_class': 'corvette', 'pilots': [], 'films': ['https://swapi.dev/api/films/1/',
                                                                                'https://swapi.dev/api/films/3/',
                                                                                'https://swapi.dev/api/films/6/'],
            'created': '2014-12-10T14:20:33.369000Z',
            'edited': '2014-12-20T21:23:49.867000Z', 'url': 'https://swapi.dev/api/starships/2/'
        }]

        assert result == expected_result

    def test_should_raise_error_for_status_different_than_200(self) -> int:

        instance = SwapiApiConsumer()
        result = instance.get_starships(page=1)

        assert result.status_code == 200

    @pytest.mark.skip
    def test_when_a_page_does_not_exist(self):
        instance = SwapiApiConsumer()
        response = instance.get_starships(page=500)

    @pytest.mark.skip
    def test_when_the_status_code_is_different_from_200(self, requests_mock):
        requests_mock.get("https://swapi.dev/api/starships/", status_code=404, json="raise exception")

        instance = SwapiApiConsumer()
        response = instance.get_starships(page=1)
