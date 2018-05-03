# -*- coding:utf-8 -*-
from coincheck_api.clients.api_client import ApiClient
from coincheck_api.exception import CoinCheckApiException


class PublicApiClient(ApiClient):

    def get_btc_ticker(self):
        """
        get ticker information of Bitcoin
        :return: ticker information of Bitcoin
        """
        return self.execute_http_call("/api/ticker", "GET", headers=None)

    def get_trades(self, pair="btc_jpy"):
        """
        get latest information about trades of a certain currency pair.
        :param pair: currency pair joined by underscore. As of 2018/05, only "btc_jpy" is supported.
        :return:
        """
        return self.execute_http_call("/api/trades?pair={}".format(pair), "GET", headers=None)

    def get_order_books(self):
        """
        get order books of bitcoin
        :return: order books of bitcoin
        """
        return self.execute_http_call("/api/order_books", "GET", headers=None)

    def get_exchange_rate(self, order_type, amount=None, price=None, pair="btc_jpy"):
        """
        get exchange rate of a certain currency pair.
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

        return self.execute_http_call("/api/exchange/orders/rate?{}".format(query), "GET", headers=None)

    def get_sale_rate(self, pair):
        """
        get a rate of a certain pair(e.g. btc_jpy) sold by coincheck.
        if you enter "btc_jpy" as the pair and get 60000, it means you can buy 1 bitcoin for 60000 yen.

        :param pair: currency pair joined by underscore
        (e.g. "btc_jpy", "eth_jpy", "etc_jpy", "lsk_jpy", "fct_jpy", "xmr_jpy", "rep_jpy",
        "xrp_jpy", "zec_jpy", "xem_jpy", "ltc_jpy", "dash_jpy", "bch_jpy" )
        :return: rate value in floating value.
        """
        response = self.execute_http_call("/api/rate/{}".format(pair), "GET")
        return float(response["rate"])
