import logging
import unittest

from coincheck_api import Client, settings
from coincheck_api.exception import CoinCheckApiException


class TestAccount(unittest.TestCase):
    """Test class of client.py
    """

    def setUp(self):
        logging.basicConfig(
            format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s',
            level=logging.DEBUG)
        self.client = Client(settings.access_key, settings.secret)

    def test_get_ticker(self):
        response = self.client.get_btc_ticker()
        self.assertIsNotNone(response["ask"])
        self.assertIsNotNone(response["bid"])

    def test_get_trades(self):
        response = self.client.get_trades()
        self.assertEqual(response["success"], True)

    def test_get_order_books(self):
        response = self.client.get_order_books()
        self.assertIsNotNone(response["asks"])
        self.assertIsNotNone(response["bids"])

    def test_get_exchange_rate(self):
        response = self.client.get_exchange_rate("sell", amount=0.1)
        self.assertEqual(response["success"], True)

        response = self.client.get_exchange_rate("buy", price=10000)
        self.assertEqual(response["success"], True)

        # invalid order_type
        self.assertRaises(CoinCheckApiException, self.client.get_exchange_rate, "hogefuga", amount=0.1)

        # both amount and price are provided
        self.assertRaises(CoinCheckApiException, self.client.get_exchange_rate, "sell", amount=0.1, price=10000)

    def test_get_sale_rate(self):
        rate = self.client.get_sale_rate("btc_jpy")
        self.assertTrue(isinstance(rate, float))
        # self.assertGreater( rate, 1800000.0, "please...")

    def test_get_account_balance(self):
        response = self.client.get_account_balance()
        self.assertEqual(response["success"], True)
