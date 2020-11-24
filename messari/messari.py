# -*- coding: utf-8 -*- #
import requests

# --------- Constants --------- #

BASE_URL = "https://data.messari.io"

# --------- Constants --------- #


class Messari:
    """
    Messari class to act as Messari's Crypto Data API client.
    All the requests can be made through this class.
    """

    def __init__(self, key=None):
        """
        Initialize the object
        :param key: API key
        """
        self.key = key
        self.session = requests.Session()
        if self.key:
            self.session.headers.update({'x-messari-api-key': key})

    def _send_message(self, method, endpoint, params=None, data=None):
        """
        Send API request.
        :param method: HTTP method (get, post, delete, etc.)
        :param endpoint: Endpoint (to be added to base URL)
        :param params: HTTP request parameters
        :param data: JSON-encoded string payload for POST
        :return: dict/list: JSON response
        """
        url = BASE_URL + endpoint
        r = self.session.request(method, url, params=params,
                                 data=data, timeout=30)
        return r.json()

    def _get(self, endpoint, params=None):
        """
        Get API request
        :param endpoint: Endpoint (to be added to base URL)
        :param params: HTTP request parameters
        :return:
        """
        return self._send_message('GET', endpoint, params=params)

    def get_all_assets(self, **query_params):
        """
        Get the paginated list of all assets and their metrics and profiles.
        Endpoint: GET /api/v2/assets

        :param query_params: dict of query parameters to filter the list
        :return: JSON response
        """
        path = '/api/v2/assets'
        if query_params.get('with-profiles', False) and query_params.get('with-metrics', False):
            path += '?with-metrics&with-profiles'
        elif query_params.get('with-profiles', False):
            path += '?with-profiles'
        elif query_params.get('with-metrics', False):
            path += '?with-metrics'

        if 'with-metrics' in query_params:
            del query_params['with-metrics']
        if 'with-profiles' in query_params:
            del query_params['with-profiles']

        return self._get(path, params=query_params)

    def get_asset(self, asset_key, fields=None):
        """
        Get basic metadata for an asset.
        Endpoint: GET /api/v1/assets/{assetKey}

        :param asset_key: This "key" can be the asset's ID (unique), slug (unique), or symbol (non-unique)
        :param fields: string: pare down the returned fields (comma , separated, drill down with a slash /)
                        example: fields='id,slug,symbol,metrics/market_data/price_usd'
        :return: JSON response
        """
        path = '/api/v1/assets/{}'.format(asset_key)
        param = {
            'fields': fields
        }
        return self._get(path, params=param)

    def get_asset_profile(self, asset_key, fields=None):
        """
        Get all of our qualitative information for an asset.
        Endpoint: GET /api/v2/assets/{assetKey}/profile

        :param asset_key: This "key" can be the asset's ID (unique), slug (unique), or symbol (non-unique)
        :param fields: string: pare down the returned fields (comma , separated, drill down with a slash /)
                        example: fields='id,slug,symbol,metrics/market_data/price_usd'
        :return: JSON response
        """
        path = '/api/v2/assets/{}/profile'.format(asset_key)

        param = {
            'fields': fields
        }

        return self._get(path, params=param)

    def get_asset_metrics(self, asset_key, fields=None):
        """
        Get all of our quantitative metrics for an asset.
        Endpoint: GET /api/v1/assets/{assetKey}/metrics

        :param asset_key: This "key" can be the asset's ID (unique), slug (unique), or symbol (non-unique)
        :param fields: string: pare down the returned fields (comma , separated, drill down with a slash /)
                        example: fields='id,slug,symbol,metrics/market_data/price_usd'
        :return: JSON response
        """
        path = '/api/v1/assets/{}/metrics'.format(asset_key)
        param = {
            'fields': fields
        }

        return self._get(path, params=param)

    def get_asset_market_data(self, asset_key, fields=None):
        """
        Get the latest market data for an asset.
        This data is also included in the metrics endpoint,
        but if all you need is market-data, use this.
        Endpoint: GET /api/v1/assets/{assetKey}/metrics/market-data

        :param asset_key: This "key" can be the asset's ID (unique), slug (unique), or symbol (non-unique)
        :param fields: string: pare down the returned fields (comma , separated, drill down with a slash /)
                        example: fields='id,slug,symbol,metrics/market_data/price_usd'
        :return: JSON response
        """
        path = '/api/v1/assets/{}/metrics/market-data'.format(asset_key)
        param = {
            'fields': fields
        }

        return self._get(path, params=param)

    def list_asset_timeseries_metric_ids(self):
        """
        Lists all of the available timeseries metric IDs for assets.
        Endpoint: GET https://data.messari.io/api/v1/assets/metrics

        :return: JSON response
        """
        path = '/api/v1/assets/metrics'
        return self._get(path)

    def get_asset_timeseries(self, asset_key, metric_id, **query_params):
        """
        Retrieve historical timeseries data for an asset.
        You can specify the range of what points will be returned
        using (begin, end, start, before, after) query parameters.
        All range parameters are inclusive of the specified date.

        Endpoint: GET /api/v1/assets/{assetKey}/metrics/{metric_id}/time-series

        :param asset_key: This "key" can be the asset's ID (unique), slug (unique), or symbol (non-unique)
        :param metric_id: specifies which timeseries will be returned.
        :param query_params: dict of query parameters to filter the list
        :return: JSON response
        """
        path = '/api/v1/assets/{}/metrics/{}/time-series'.format(asset_key, metric_id)
        return self._get(path, params=query_params)

    def get_all_markets(self, fields=None):
        """
        Get the list of all exchanges and pairs that our WebSocket-based
        market real-time market data API supports.
        Endpoint: GET /api/v1/markets

        :param fields: string: pare down the returned fields (comma , separated, drill down with a slash /)
                        example: fields='id,slug,symbol,metrics/market_data/price_usd'
        :return: JSON response
        """
        path = '/api/v1/markets'
        param = {
            'fields': fields
        }

        return self._get(path, params=param)

    def get_market_timeseries(self, market_key, metric_id, **query_params):
        """
        Retrieve historical timeseries data for a market.

        Endpoint: GET /api/v1/markets/{assetKey}/metrics/{metric_id}/time-series

        :param market_key: This "key" can be the asset's ID (unique), slug (unique), or symbol (non-unique)
        :param metric_id: The metricID is a unique identifier which determines which columns are returned
                            by time-series endpoints. For a list of valid metric ids, check the API response
                            at https://data.messari.io/api/assets/metrics.
        :param query_params: dict of query parameters to filter the list
        :return: JSON response
        """
        path = '/api/v1/markets/{}/metrics/{}/time-series'.format(market_key, metric_id)
        return self._get(path, params=query_params)

    def get_all_news(self, page=None, fields=None):
        """
        Get the latest (paginated) news and analysis for all assets.

        Endpoint: GET /api/v1/news

        :param page: Page number, starts at 1. Increment to paginate through results (until result is empty array)
        :param fields: string: pare down the returned fields (comma , separated, drill down with a slash /)
                        example: fields='id,slug,symbol,metrics/market_data/price_usd'
        :return: JSON response
        """
        path = '/api/v1/news'
        params = {
            'fields': fields
        }
        if page:
            params['page'] = page

        return self._get(path, params=params)

    def get_news_for_asset(self, asset_key, page=None, fields=None):
        """
        Get the latest (paginated) news and analysis for all assets.

        Endpoint: GET /api/v1/news/{asset_key}

        :param asset_key: This "key" can be the asset's ID (unique), slug (unique), or symbol (non-unique)
        :param page: Page number, starts at 1. Increment to paginate through results (until result is empty array)
        :param fields: string: pare down the returned fields (comma , separated, drill down with a slash /)
                        example: fields='id,slug,symbol,metrics/market_data/price_usd'
        :return: JSON response
        """
        path = '/api/v1/news/{}'.format(asset_key)
        params = {
            'fields': fields
        }
        if page:
            params['page'] = page

        return self._get(path, params=params)
