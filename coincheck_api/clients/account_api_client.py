# -*- coding:utf-8 -*-
from coincheck_api.clients.private_api_client import PrivateApiClient


class AccountApiClient(PrivateApiClient):

    def __init__(self, access_key, secret):
        PrivateApiClient.__init__(self, access_key, secret)

    def get_account_balance(self):
        """
        get balance of a account
        :return: account balance
        """
        return self.execute_private_api("/api/accounts/balance", "GET")

    def get_account_leverage_balance(self):
        """
        get balance of a leverage account
        :return: leverage_account balance
        """
        return self.execute_private_api("/api/accounts/leverage_balance", "GET")

    def send_money(self, address, amount):
        """
        send bitcoin to a certain address
        :param address:
        :param amount:
        :return:
        """
        payload = {'address': address, 'amount': amount}
        return self.execute_private_api("/api/send_money", "POST", data=payload)

    def get_send_money_history(self, currency="btc"):
        """
        get the history of a certain sent currency
        :param currency: currency that you want to see the history. As of 2018-05, only "btc" is supported
        :return: history
        """
        return self.execute_private_api("/api/send_money?currency={}".format(currency), "GET")

    def get_deposit_money_history(self, currency="btc"):
        """
        get history of certain deposited currency
        :param currency: currency that you want to see the history. As of 2018-05, only "btc" is supported
        :return: history
        """
        return self.execute_private_api("/api/deposit_money?currency={}".format(currency), "GET")

    def send_money_fast(self, receipt_id):
        """
        send bitcoin quickly with some charge
        :param receipt_id: an id issued when received the money
        :return: sending money is succeeded or not
        """
        return self.execute_private_api("/api/deposit_money/{}/fast".format(receipt_id), "POST")

    def get_account(self):
        """
        show coincheck account information
        :return: account information
        """
        return self.execute_private_api("/api/accounts", "GET")
