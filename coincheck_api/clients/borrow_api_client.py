# -*- coding:utf-8 -*-
from coincheck_api.clients.private_api_client import PrivateApiClient
from coincheck_api.exception import CoinCheckApiException


class BorrowApiClient(PrivateApiClient):

    def __init__(self, access_key, secret):
        PrivateApiClient.__init__(self, access_key, secret)

    def borrow_currency(self, amount, currency):
        """
        borrow bitcoin/etherium from coincheck
        :param amount: amount to borrow
        :param currency: currency to borrow
        :return: borrowed information (rate etc.)
        """
        if currency not in ["btc", "eth"]:
            raise CoinCheckApiException("currency to borrow should be \"btc\" or \"etc\"")

        data = {"amount": amount, "currency": currency}
        return self.execute_private_api("/api/lending/borrows", "POST", data=data)

    def get_borrowings(self):
        """
        get borrowings information
        :return: borrowings information
        """
        return self.execute_private_api("/api/lending/borrows/matches", "GET")

    def repay_currency(self, borrow_id):
        """
        repay money to coincheck
        :param borrow_id: id issued when borrowed
        :return: succeeded or not
        """
        return self.execute_private_api("api/lending/borrows/{}/repay".format(borrow_id), "POST")
