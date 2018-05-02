# -*- coding:utf-8 -*-
import requests
import json
from coincheck_api.exception import CoinCheckApiException
import coincheck_api.auth
from logging import getLogger
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
        return float( response["rate"] )

    def get_account_balance(self):
        return self.execute_api("/api/accounts/balance", "GET", is_private=True)

    def execute_api(self, path, method, is_private):
        """
        :param path: API path (e.g. /api/ticker )
        :param method: HTTP method in string. "GET", "POST", "PUT", "DELETE"
        :param is_private: boolean. True if this API needs authentication
        :return: response in json-deserialized dictionary object
        """
        url = Client.base_url + path
        headers = None
        if is_private :
            headers = coincheck_api.auth.create_auth_headers(
                url,
                access_key = self.access_key,
                secret = self.secret)
        logger.debug("HTTP call executed. {} {} {} {}".format(url, method, headers, is_private))

        # execute an HTTP call
        response = requests.request(method, url, headers=headers)
        logger.debug("HTTP status code of response={} {}".format(response.status_code, response.content) )

        response_body = json.loads( response.content )
        # success
        if 200 <= response.status_code < 400 :
            return response_body
        # failure
        else:
            raise CoinCheckApiException(
                "API execute failure. response status_code={}, headers={}, body={}".format(
                    response.status_code, response.headers, response.content
                ))

