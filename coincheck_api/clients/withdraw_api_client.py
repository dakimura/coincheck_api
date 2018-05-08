# -*- coding:utf-8 -*-
from coincheck_api.clients.private_api_client import PrivateApiClient
from coincheck_api.exception import CoinCheckApiException


class WithdrawApiClient(PrivateApiClient):

    def __init__(self, access_key, secret):
        PrivateApiClient.__init__(self, access_key, secret)

    def get_bank_account(self):
        """
        get bank account registered to coincheck
        :return: bank account information
        """
        return self.execute_private_api("/api/bank_accounts", "GET")

    def register_bank_account(self, bank_name, branch_name, bank_account_type, number, name):
        """
        register a bank account used to send money from coincheck
        :param bank_name: bank name
        :param branch_name: branch name
        :param bank_account_type: "futsu"(savings account) or "toza"(checking account)
        :param number: account number
        :param name: name of the bank account holder
        :return: registered account information
        """
        if bank_account_type not in ["futsu", "toza"]:
            raise CoinCheckApiException(
                "bank_account_type should be \"futsu\"(savings account) or \"toza\"(checking account)")
        data = {"bank_name": bank_name, "branch_name": branch_name, "bank_account_type": bank_account_type,
                "number": number, "name": name}
        return self.execute_private_api("/api/bank_accounts", "POST", data=data)

    def delete_bank_account(self, bank_id):
        """
        delete a registration of a bank account
        :param bank_id: id of the bank
        :return: succeeded to delete or not
        """
        return self.execute_private_api("/api/bank_accounts/{}".format(bank_id), "DELETE")

    def get_withdraws(self, limit=None, order=None, start_id=None, end_id=None):
        """
        get history of requests to withdraw JPY with pagination functionality
        :param limit: the number of items to get
        :param order: "desc" or "asc"
        :param start_id: get items after the id
        :param end_id: get items before the id
        :return: history of requests to withdraw JPY
        """
        data = {"limit": limit, "order": order, "starting_after": start_id, "ending_before": end_id}
        return self.execute_private_api("/api/withdraws", "GET", data=data)

    def request_withdraw(self, bank_account_id, amount, currency="JPY"):
        """
        request to withdraw JPY
        :param bank_account_id: bank id
        :param amount: amount to withdraw
        :param currency: currency to withdraw. As of 2018-05, only "JPY" is supported.
        :return: result of the request
        """
        data = {"bank_account_id": bank_account_id, "amount": amount, "currency": currency}
        return self.execute_private_api("/api/withdraws", "POST", data=data)

    def cancel_withdraw(self, withdraw_request_id):
        """
        cancel a request to withdraw.
        the request only in "pending" status can be canceled.
        :param withdraw_request_id: id issued when requested to withdraw
        :return: cancel is succeeded or not
        """
        return self.execute_private_api("api/withdraws/{}".format(withdraw_request_id), "DELETE")
