import pytest
from messari.messari import Messari
from time import sleep


@pytest.fixture(scope='module')
def client():
    return Messari()


@pytest.mark.usefixtures('client')
class TestMessari:
    """
    Test Messari class
    """

    @staticmethod
    def teardown_method():
        sleep(3)  # Avoid rate limit: 20 requests per minute

    def test_get_all_assets(self, client):
        response = client.get_all_assets()
        assert type(response) == dict
        if 'data' in response:
            assert type(response['data']) == list
            if len(response['data']) > 0:
                assert type(response['data'][0]) == dict
                assert "id" in response['data'][0]
                assert "symbol" in response['data'][0]
                assert "name" in response['data'][0]
                assert "slug" in response['data'][0]
                assert "profile" in response['data'][0]
                assert "metrics" in response['data'][0]
        else:
            assert "error_code" in response
            assert "error_message" in response

    test_data = [
        (None, 'error_code', 404),
        ('btc1111', 'error_code', 404),
        ('btc', 'symbol', 'BTC')
    ]

    @pytest.mark.parametrize("asset_key,expected_key,expected_val", test_data)
    def test_get_asset(self, client, asset_key, expected_key, expected_val):
        response = client.get_asset(asset_key)
        assert type(response) == dict
        if 'data' in response:
            assert expected_key in response['data']
            assert expected_val == response['data'][expected_key]
        else:
            assert expected_key in response['status']
            assert expected_val == response['status'][expected_key]

    def test_get_asset_profile(self, client):
        # TODO
        assert True

    def test_get_asset_metrics(self, client):
        # TODO
        assert True

    def test_get_asset_market_data(self, client):
        # TODO
        assert True

    def test_list_asset_timeseries_metric_ids(self, client):
        # TODO
        assert True

    def test_get_asset_timeseries(self, client):
        # TODO
        assert True

    def test_get_all_markets(self, client):
        # TODO
        assert True

    def test_get_market_timeseries(self, client):
        # TODO
        assert True

    def test_get_all_news(self, client):
        # TODO
        assert True

    def test_get_news_for_asset(self, client):
        # TODO
        assert True
