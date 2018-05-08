import logging
import unittest

from coincheck_api import settings
from coincheck_api.clients.account_api_client import AccountApiClient
from coincheck_api.exception import CoinCheckApiException


class TestAccountApi(unittest.TestCase):
    """Test class of account_api_client.py
    """

    def setUp(self):
        logging.basicConfig(
            format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s',
            level=logging.DEBUG)
        self.client = AccountApiClient(settings.access_key, settings.secret)

    def test_get_account_balance(self):
        response = self.client.get_account_balance()
        self.assertEqual(response["success"], True)

    def test_get_account_leverage_balance(self):
        response = self.client.get_account_leverage_balance()
        self.assertEqual(response["success"], True)

    def test_send_money(self):
        response = self.client.send_money(address="hoge", amount=100, dry_run=True)
        self.assertEqual(response["success"], True)

    def test_get_send_money_history(self):
        response = self.client.get_send_money_history()
        self.assertEqual(response["success"], True)

    def test_get_deposit_money_history(self):
        response = self.client.get_deposit_money_history()
        self.assertEqual(response["success"], True)

    def test_deposit_money_fast(self):
        response = self.client.deposit_money_fast(receipt_id="hoge", dry_run=True)
        self.assertEqual(response["success"], True)

    def test_get_account(self):
        response = self.client.get_account()
        self.assertEqual(response["success"], True)