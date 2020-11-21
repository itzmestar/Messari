# Messari


[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)
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
resp = messari.get_all_assets()

# Get basic metadata for an asset.
resp = messari.get_asset(asset_key='btc')

# Get all of our qualitative information for an asset.
resp = messari.get_asset_profile(asset_key='btc')

# Get all of our quantitative metrics for an asset.
resp = messari.get_asset_metrics(asset_key='btc')

# Get the latest market data for an asset.
resp = messari.get_asset_market_data(asset_key='btc')

# Lists all of the available timeseries metric IDs for assets.
resp = messari.list_asset_timeseries_metric_ids()

# Retrieve historical timeseries data for an asset.
resp = messari.get_asset_timeseries(asset_key='bitcoin', metric_id='price')

# Get the list of all exchanges and pairs that our WebSocket-based
# market real-time market data API supports.
resp = messari.get_all_markets()

# Retrieve historical timeseries data for a market.
resp = messari.get_market_timeseries(market_key='binance-btc-usdt', metric_id='price')

# Get the latest (paginated) news and analysis for all assets.
resp = messari.get_all_news()

# Get the latest (paginated) news and analysis for all assets.
resp = messari.get_news_for_asset(asset_key='btc')
```
