from infra.swapi_api_consumer import SwapiApiConsumer


class TestSwapiApiConsumer:
    def test_when_you_do_a_get_and_return_answer(self):
        page: int = 1

        req = SwapiApiConsumer()
        response = req.get_starships(page=page)

        print(response)
