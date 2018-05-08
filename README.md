# coincheck_api
A simple python library to use CoinCheck API.

## Install
`$ pip install coincheck_api`

```buildoutcfg
# or
# $  pip install git+https://github.com/dakimura/coincheck_api.gi
```
 - if you want to use [Private Api](https://coincheck.com/ja/documents/exchange/api#private), [create an API key(accessKey, secret)](https://coincheck.com/ja/api_settings) first.
 - [Private Api](https://coincheck.com/ja/documents/exchange/api#private)を使う場合は、先に[API key(accessKey, secret)を作成](https://coincheck.com/ja/api_settings)してください。

## Usage

```buildoutcfg
$ python
>>> from coincheck_api import Client
>>> client = Client(access_key="foo", secret="bar")
>>>
>>> # examples
>>> 
>>> # 口座の残高を取得します
>>> client.get_account_balance()
{'success': True, 'jpy': '12138750.9387', 'btc': '0.0', 'eth': '62.367956', 'etc': '0', 'dao': '0', 'lsk': '0', 'fct': '6153.247', 'xmr': '0', 'rep': '0.0', 'xrp': '1957390.0', 'zec': '0', 'xem': '0.0', 'ltc': '0', 'dash': '0.18622', 'bch': '0', 'jpy_reserved': '0.0', 'btc_reserved': '0', 'eth_reserved': '0', 'etc_reserved': '0', 'dao_reserved': '0', 'lsk_reserved': '0', 'fct_reserved': '0', 'xmr_reserved': '0', 'rep_reserved': '0', 'xrp_reserved': '0', 'zec_reserved': '0', 'xem_reserved': '0', 'ltc_reserved': '0', 'dash_reserved': '0', 'bch_reserved': '0', 'jpy_lend_in_use': '0.0', 'btc_lend_in_use': '0.0', 'eth_lend_in_use': '0.0', 'etc_lend_in_use': '0.0', 'dao_lend_in_use': '0.0', 'lsk_lend_in_use': '0.0', 'fct_lend_in_use': '0.0', 'xmr_lend_in_use': '0.0', 'rep_lend_in_use': '0.0', 'xrp_lend_in_use': '0.0', 'zec_lend_in_use': '0.0', 'xem_lend_in_use': '0.0', 'ltc_lend_in_use': '0.0', 'dash_lend_in_use': '0.0', 'bch_lend_in_use': '0.0', 'jpy_lent': '0.0', 'btc_lent': '0.0', 'eth_lent': '0.0', 'etc_lent': '0.0', 'dao_lent': '0.0', 'lsk_lent': '0.0', 'fct_lent': '0.0', 'xmr_lent': '0.0', 'rep_lent': '0.0', 'xrp_lent': '0.0', 'zec_lent': '0.0', 'xem_lent': '0.0', 'ltc_lent': '0.0', 'dash_lent': '0.0', 'bch_lent': '0.0', 'jpy_debt': '0.0', 'btc_debt': '0.0', 'eth_debt': '0.0', 'etc_debt': '0.0', 'dao_debt': '0.0', 'lsk_debt': '0.0', 'fct_debt': '0.0', 'xmr_debt': '0.0', 'rep_debt': '0.0', 'xrp_debt': '0.0', 'zec_debt': '0.0', 'xem_debt': '0.0', 'ltc_debt': '0.0', 'dash_debt': '0.0', 'bch_debt': '0.0'}
>>>
>>> # 指値5000円で0.1bitcoinの買い注文を出します
>>> client.buy(rate=5000, btc_amount=0.1)
{'success': True, 'id': 903090581, 'amount': '0.1', 'rate': '5000.0', 'order_type': 'buy', 'pair': 'btc_jpy', 'created_at': '2018-05-08T00:13:26.231Z', 'market_buy_amount': None, 'stop_loss_rate': None}
>>>
```

- Returned value of each function of `coincheck_api.Client` is a json-deserialized API response.
For more information of the API responses, please refer [official API documents](https://coincheck.com/ja/documents/exchange/api) 
