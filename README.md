# coincheck_api
A simple python library to use CoinCheck API

## Usage

```buildoutcfg
$ pip install git+https://github.com/dakimura/coincheck_api.git
$ python
>>> from coincheck_api import Client
>>> client = Client(access_key="foo", secret="bar")
>>> client.get_account_balance()
{'success': True, 'jpy': '12138750.9387', 'btc': '0.0', 'eth': '62.367956', 'etc': '0', 'dao': '0', 'lsk': '0', 'fct': '6153.247', 'xmr': '0', 'rep': '0.0', 'xrp': '1957390.0', 'zec': '0', 'xem': '0.0', 'ltc': '0', 'dash': '0.18622', 'bch': '0', 'jpy_reserved': '0.0', 'btc_reserved': '0', 'eth_reserved': '0', 'etc_reserved': '0', 'dao_reserved': '0', 'lsk_reserved': '0', 'fct_reserved': '0', 'xmr_reserved': '0', 'rep_reserved': '0', 'xrp_reserved': '0', 'zec_reserved': '0', 'xem_reserved': '0', 'ltc_reserved': '0', 'dash_reserved': '0', 'bch_reserved': '0', 'jpy_lend_in_use': '0.0', 'btc_lend_in_use': '0.0', 'eth_lend_in_use': '0.0', 'etc_lend_in_use': '0.0', 'dao_lend_in_use': '0.0', 'lsk_lend_in_use': '0.0', 'fct_lend_in_use': '0.0', 'xmr_lend_in_use': '0.0', 'rep_lend_in_use': '0.0', 'xrp_lend_in_use': '0.0', 'zec_lend_in_use': '0.0', 'xem_lend_in_use': '0.0', 'ltc_lend_in_use': '0.0', 'dash_lend_in_use': '0.0', 'bch_lend_in_use': '0.0', 'jpy_lent': '0.0', 'btc_lent': '0.0', 'eth_lent': '0.0', 'etc_lent': '0.0', 'dao_lent': '0.0', 'lsk_lent': '0.0', 'fct_lent': '0.0', 'xmr_lent': '0.0', 'rep_lent': '0.0', 'xrp_lent': '0.0', 'zec_lent': '0.0', 'xem_lent': '0.0', 'ltc_lent': '0.0', 'dash_lent': '0.0', 'bch_lent': '0.0', 'jpy_debt': '0.0', 'btc_debt': '0.0', 'eth_debt': '0.0', 'etc_debt': '0.0', 'dao_debt': '0.0', 'lsk_debt': '0.0', 'fct_debt': '0.0', 'xmr_debt': '0.0', 'rep_debt': '0.0', 'xrp_debt': '0.0', 'zec_debt': '0.0', 'xem_debt': '0.0', 'ltc_debt': '0.0', 'dash_debt': '0.0', 'bch_debt': '0.0'}
```