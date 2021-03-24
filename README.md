# Messari

[![Python 3.5](https://img.shields.io/badge/python-3.5-blue.svg)](https://www.python.org/downloads/release/python-350/)
[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

![Build](https://github.com/itzmestar/Messari/workflows/Build/badge.svg)


-------

### Unofficial [Messari's Crypto Data API](https://messari.io/) client in python
The library can be used for crypto prices, market data metrics, on-chain metrics, and qualitative information (asset profile).
For more information, see [Messari API Documentation](https://messari.io/api/docs)

### Installation:
use pip to install:
``` 
pip install messari
```
-----------

### Authentication:

Most endpoints are accessible without an API key.

Pass API key in object initialization if required.

-----------

### Example usage:
```
from messari import Messari

# initialize api client
# API Key is optional
messari = Messari(key='xxxxxxxxxxxxxxx')

# Get the paginated list of all assets and their metrics and profiles.
response = messari.get_all_assets()

# Use query parameters
query = {
    'with-profiles': True,
    'with-metrics': True,
    'fields': 'id,slug,symbol,metrics/market_data/price_usd'
}
response = messari.get_all_assets(**query)

# set filter fields
fields='symbol,name,slug'

# Get basic metadata for an asset.
response = messari.get_asset(asset_key='btc', fields=fields)

# Get all of our qualitative information for an asset.
fields='symbol,name,profile/general/overview/project_details'
response = messari.get_asset_profile(asset_key='btc', fields=fields)

# Get all of our quantitative metrics for an asset.
fields = 'id,slug,symbol,market_data/price_usd,market_data/volume_last_24_hours'
response = messari.get_asset_metrics(asset_key='btc', fields=fields)

# Get the latest market data for an asset.
fields = 'id,slug,symbol,market_data/price_usd,market_data/volume_last_24_hours'
response = messari.get_asset_market_data(asset_key='btc', fields=fields)

# Lists all of the available timeseries metric IDs for assets.
response = messari.list_asset_timeseries_metric_ids()

# Retrieve historical timeseries data for an asset.
query_params = {
    'start': '2020-01-01',
    'end': '2020-02-01',
    'interval': '1d',
    'columns': 'open,close',
    'order': 'ascending',
    'format': 'json',
    'timestamp-format': 'rfc3339'
}
response = messari.get_asset_timeseries(asset_key='bitcoin', metric_id='price', **query_params)

# Get the list of all exchanges and pairs that our WebSocket-based
# market real-time market data API supports.
fields = 'exchange_name,pair,last_trade_at'
response = messari.get_all_markets(fields=fields)

# Retrieve historical timeseries data for a market.
query_params = {
    'start': '2020-01-01',
    'end': '2020-03-01',
    'interval': '1d',
    'columns': 'open,close',
    'order': 'ascending',
    'format': 'json',
    'timestamp-format': 'rfc3339'
}
response = messari.get_market_timeseries(market_key='binance-btc-usdt', metric_id='price', **query_params)

# Get the latest (paginated) news and analysis for all assets.
fields='title,content'
response = messari.get_all_news(fields=fields)

# Get the latest (paginated) news and analysis for all assets.
fields='title,content'
response = messari.get_news_for_asset(asset_key='btc', fields=fields)
```
