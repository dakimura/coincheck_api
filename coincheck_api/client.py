# -*- coding:utf-8 -*-
from logging import getLogger

from coincheck_api.clients.account_api_client import AccountApiClient
from coincheck_api.clients.borrow_api_client import BorrowApiClient
from coincheck_api.clients.order_api_client import OrderApiClient
from coincheck_api.clients.public_api_client import PublicApiClient
from coincheck_api.clients.transfer_api_client import TransferApiClient
from coincheck_api.clients.withdraw_api_client import WithdrawApiClient

logger = getLogger(__name__)


class Client(PublicApiClient, OrderApiClient, AccountApiClient, BorrowApiClient, WithdrawApiClient, TransferApiClient):
    """
    In order to use private APIs (e.g. Order, Account balance check)
    You should create an API key in advance.
    https://coincheck.com/ja/documents/exchange/api#auth
    """

    def __init__(self, access_key, secret):
        PublicApiClient.__init__(self)
        OrderApiClient.__init__(self, access_key, secret)
