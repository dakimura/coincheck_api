# -*- coding:utf-8 -*-
import json
from logging import getLogger

import requests

import coincheck_api.auth
from coincheck_api.exception import CoinCheckApiException

logger = getLogger(__name__)


class Client:
    """
    In order to use private APIs (e.g. Order, Account balance check)
    You should create an API key in advance.
    https://coincheck.com/ja/documents/exchange/api#auth
    """
    base_url = "https://coincheck.com"

    def __init__(self, access_key, secret):
        self.access_key = access_key
        self.secret = secret

    def get_btc_ticker(self):
        """
        get ticker information of Bitcoin
        :return: ticker information of Bitcoin
        """
        return self.execute_api("/api/ticker", "GET", is_private=False)

    def get_trades(self, pair="btc_jpy"):
        """
        get latest information about trades of certain currency pair.
        :param pair: currency pair joined by underscore. At the timing of 2018/05,
        only "btc_jpy" is supported.
        :return:
        """
        return self.execute_api("/api/trades?pair={}".format(pair), "GET", is_private=False)

    def get_order_books(self):
        """
        get order books of bitcoin
        :return: order books of bitcoin
        """
        return self.execute_api("/api/order_books", "GET", is_private=False)

    def get_exchange_rate(self, order_type, amount=None, price=None, pair="btc_jpy"):
        """
        get exchange rate of certain currency pair.
        :param order_type: "sell" or "buy"
        :param pair: currency pair joined by underscore. At the timing of 2018/05,
        only "btc_jpy" is supported.
        :param amount: amount of the currency to sell/buy. (e.g. 0.1)
        :param price: price to sell/buy in JPY. (e.g. 10000 [yen])
        :return: information about exchange rate
        """
        if order_type not in ["sell", "buy"]:
            raise CoinCheckApiException("order_type should be \"sell\" or \"buy\"")
        if amount is not None and price is not None:
            raise CoinCheckApiException("only one of \"amount\" and \"price\" can be provided ")

        query = "order_type={}&pair={}".format(order_type, pair)
        if amount is not None:
            query += "&amount={}".format(amount)
        else:
            query += "&price={}".format(price)

        return self.execute_api("/api/exchange/orders/rate?{}".format(query), "GET", is_private=False)

    def get_sale_rate(self, pair):
        """
        get a rate of certain pair(e.g. btc_jpy) sold by coincheck.
        if you enter "btc_jpy" as the pair and get 60000, it means you can buy 1 bitcoin for 60000 yen.

        :param pair: currency pair joined by underscore
        (e.g. "btc_jpy", "eth_jpy", "etc_jpy", "lsk_jpy", "fct_jpy", "xmr_jpy", "rep_jpy",
        "xrp_jpy", "zec_jpy", "xem_jpy", "ltc_jpy", "dash_jpy", "bch_jpy" )
        :return: rate value in floating value.
        """
        response = self.execute_api("/api/rate/{}".format(pair), "GET", is_private=False)
        return float(response["rate"])

    def get_account_balance(self):
        """
        :return: account balance
        """
        return self.execute_api("/api/accounts/balance", "GET", is_private=True)

    def get_account_leverage_balance(self):
        """
        :return: leverage_account balance
        """
        return self.execute_api("/api/accounts/leverage_balance", "GET", is_private=True)

    def execute_api(self, path, method, is_private):
        """
        :param path: API path (e.g. /api/ticker )
        :param method: HTTP method in string. "GET", "POST", "PUT", "DELETE"
        :param is_private: boolean. True if this API needs authentication
        :return: response in json-deserialized dictionary object
        """
        url = Client.base_url + path
        headers = None
        if is_private:
            headers = coincheck_api.auth.create_auth_headers(
                url,
                access_key=self.access_key,
                secret=self.secret)
        logger.debug("HTTP call executed. url={}, method={}, headers={} is_private={}"
                     .format(url, method, headers, is_private))

        # execute an HTTP call
        response = requests.request(method, url, headers=headers)
        logger.debug("HTTP status code of response={} {}".format(response.status_code, response.content))

        response_body = json.loads(response.content)
        # success
        if 200 <= response.status_code < 400:
            return response_body
        # failure
        else:
            raise CoinCheckApiException(
                "API execute failure. response status_code={}, headers={}, body={}".format(
                    response.status_code, response.headers, response.content
                ))
