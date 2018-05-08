# -*- coding:utf-8 -*-
from logging import getLogger

from coincheck_api.clients.private_api_client import PrivateApiClient

logger = getLogger(__name__)


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

    def send_money(self, address, amount, dry_run=False):
        """
        send bitcoin to a certain address
        :param address:
        :param amount:
        :param dry_run: for debug. when true, sending money is not actually executed
        :return:
        """
        payload = {'address': address, 'amount': amount}
        if dry_run:
            logger.info("[dry run] sending money is executed. address={}, amount={}".format(address, amount))
            return { "success": True, "id": "276", "address": address, "amount": amount, "fee": "0.002" }
        else:
            logger.info("sending money is executed. address={}, amount={}".format(address, amount))
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

    def deposit_money_fast(self, receipt_id, dry_run=False):
        """
        deposi bitcoin quickly with some charge
        :param receipt_id: an id issued when received the money
        :param dry_run: for debug. when true, sending money is not actually executed
        :return: sending money is succeeded or not
        """
        if dry_run:
            logger.info("[dry run] deposit money (fast) is executed. receipt_id={}".format(receipt_id))
            return {"success": True}
        else:
            logger.info("deposit money (fast) is executed. receipt_id={}".format(receipt_id))
            return self.execute_private_api("/api/deposit_money/{}/fast".format(receipt_id), "POST")

    def get_account(self):
        """
        show coincheck account information
        :return: account information
        """
        return self.execute_private_api("/api/accounts", "GET")
