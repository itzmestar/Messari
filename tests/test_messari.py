import pytest
from messari.messari import Messari
from time import sleep


@pytest.fixture(scope='module')
def messari():
    return Messari()


@pytest.mark.usefixtures('messari')
class TestMessari:
    """
    Test Messari class
    """

    @staticmethod
    def teardown_method():
        sleep(3)  # Avoid rate limit: 20 requests per minute

    def test_get_all_assets(self, messari):
        response = messari.get_all_assets()
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
    def test_get_asset(self, messari, asset_key, expected_key, expected_val):
        response = messari.get_asset(asset_key)
        assert type(response) == dict
        if 'data' in response:
            assert expected_key in response['data']
            assert expected_val == response['data'][expected_key]
        else:
            assert expected_key in response['status']
            assert expected_val == response['status'][expected_key]

    def test_get_asset_profile(self, messari):
        fields = 'symbol,name,profile/general/overview/project_details'
        response = messari.get_asset_profile(asset_key='btc', fields=fields)
        assert type(response) == dict
        if 'data' in response:
            assert type(response['data']) == dict
            assert "id" not in response['data']
            assert "symbol" in response['data']
            assert "name" in response['data']
            assert "slug" not in response['data']
            assert "metrics" not in response['data']
            assert "profile" in response['data']
            assert "project_details" in response['data']['profile']['general']['overview']
            assert "is_verified" not in response['data']['profile']['general']['overview']
            assert "contributors" not in response['data']['profile']
        else:
            assert "error_code" in response
            assert "error_message" in response

    def test_get_asset_metrics(self, messari):
        fields = 'id,slug,symbol,market_data/price_usd,all_time_high/price,blockchain_stats_24_hours/transaction_volume'
        response = messari.get_asset_metrics(asset_key='btc', fields=fields)
        assert type(response) == dict
        if 'data' in response:
            assert type(response['data']) == dict
            assert "id" in response['data']
            assert "symbol" in response['data']
            assert "slug" in response['data']

            assert "name" not in response['data']
            assert "metrics" not in response['data']
            assert "profile" not in response['data']
            assert "supply" not in response['data']

            assert "market_data" in response['data']
            assert "price_usd" in response['data']['market_data']
            assert "price_btc" not in response['data']['market_data']
            assert "volume_last_24_hours" not in response['data']['market_data']

            assert "all_time_high" in response['data']
            assert "price" in response['data']['all_time_high']
            assert "days_since" not in response['data']['all_time_high']

            assert "blockchain_stats_24_hours" in response['data']
            assert "transaction_volume" in response['data']['blockchain_stats_24_hours']
            assert "sum_of_fees" not in response['data']['blockchain_stats_24_hours']
        else:
            assert "error_code" in response
            assert "error_message" in response

    def test_get_asset_market_data(self, messari):
        fields = 'id,slug,symbol,market_data/price_usd,market_data/volume_last_24_hours'
        response = messari.get_asset_market_data(asset_key='btc', fields=fields)
        assert type(response) == dict
        if 'data' in response:
            assert type(response['data']) == dict
            assert "id" in response['data']
            assert "symbol" in response['data']
            assert "name" not in response['data']
            assert "slug" in response['data']
            assert "metrics" not in response['data']
            assert "profile" not in response['data']
            assert "market_data" in response['data']
            assert "price_usd" in response['data']['market_data']
            assert "volume_last_24_hours" in response['data']['market_data']
            assert "price_btc" not in response['data']['market_data']
            assert "supply" not in response['data']
            assert "all_time_high" not in response['data']
        else:
            assert "error_code" in response
            assert "error_message" in response

    def test_list_asset_timeseries_metric_ids(self, messari):
        response = messari.list_asset_timeseries_metric_ids()
        assert type(response) == dict
        if 'data' in response:
            assert type(response['data']) == dict
            assert "metrics" in response['data']
            assert type(response['data']['metrics']) == list
            if len(response['data']['metrics']) > 0:
                assert 'metric_id' in response['data']['metrics'][0]
                assert 'description' in response['data']['metrics'][0]
                assert 'values_schema' in response['data']['metrics'][0]
                assert 'minimum_interval' in response['data']['metrics'][0]
                assert 'source_attribution' in response['data']['metrics'][0]
        else:
            assert "error_code" in response
            assert "error_message" in response

    def test_get_asset_timeseries(self, messari):
        query_params = {
            'start': '2021-01-01',
            'end': '2021-02-01',
            'interval': '1d',
            'columns': 'open,close',
            'order': 'ascending',
            'format': 'json',
            'timestamp-format': 'rfc3339'
        }
        response = messari.get_asset_timeseries(asset_key='bitcoin', metric_id='price', **query_params)
        assert type(response) == dict
        if 'data' in response:
            # TODO
            pass
        else:
            assert "error_code" in response
            assert "error_message" in response

    def test_get_all_markets(self, messari):
        # TODO
        assert True

    def test_get_market_timeseries(self, messari):
        # TODO
        assert True

    def test_get_all_news(self, messari):
        # TODO
        assert True

    def test_get_news_for_asset(self, messari):
        # TODO
        assert True
