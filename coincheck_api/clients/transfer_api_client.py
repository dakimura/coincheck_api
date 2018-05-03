# -*- coding:utf-8 -*-
from coincheck_api.clients.private_api_client import PrivateApiClient
from coincheck_api.exception import CoinCheckApiException


class TransferApiClient(PrivateApiClient):

    def __init__(self, access_key, secret):
        PrivateApiClient.__init__(self, access_key, secret)

    def transfer_to_leverage_account(self, amount, currency="JPY"):
        """
        transfer money to leverage account
        :param amount: amount to transfer
        :param currency: currency to transfer. As of 2018-05, only "JPY" is supported
        :return: succeeded or not
        """
        if currency not in ["JPY"]:
            raise CoinCheckApiException("currency should be \"JPY\", currently.")
        data = {"amount": amount, "currency": currency}
        return self.execute_private_api("/api/exchange/transfers/from_leverage", "POST", data=data)

    def transfer_from_leverage_account(self, amount, currency="JPY"):
        """
        transfer money from a leverage account to an account for spot tradings
        :param amount: amount to transfer
        :param currency: currency to transfer. As of 2018-05, only "JPY" is supported
        :return: succeeded or not
        """
        if currency not in ["JPY"]:
            raise CoinCheckApiException("currency should be \"JPY\", currently.")
        data = {"amount": amount, "currency": currency}
        return self.execute_private_api("/api/exchange/transfers/from_leverage", "POST", data=data)
