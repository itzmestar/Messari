# Messari


[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-380/)

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
messari = Messari()


```
