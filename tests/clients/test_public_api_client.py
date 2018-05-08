import logging
import unittest

from coincheck_api import settings
from coincheck_api.clients.public_api_client import PublicApiClient
from coincheck_api.exception import CoinCheckApiException


class TestPublicApi(unittest.TestCase):
    """Test class of public_api_client.py
    """

    def setUp(self):
        logging.basicConfig(
            format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s',
            level=logging.DEBUG)
        self.client = PublicApiClient()

    def test_get_trades(self):
        response = self.client.get_trades()
        self.assertEqual(response["success"], True)

    def test_get_order_books(self):
        response = self.client.get_order_books()
        self.assertIsNotNone(response["asks"])

    def test_get_exchange_rate(self):
        response = self.client.get_exchange_rate(order_type="buy", amount=0.5)
        self.assertEqual(response["success"], True)

        response = self.client.get_exchange_rate(order_type="sell", price=100000.0)
        self.assertEqual(response["success"], True)

        # invalid order type
        self.assertRaises(CoinCheckApiException, self.client.get_exchange_rate, order_type="hoge", amount=0.5)

        # both amount and price are provided
        self.assertRaises(CoinCheckApiException, self.client.get_exchange_rate, order_type="sell", amount=0.5, price=100000.0)

    def test_get_sale_rate(self):
        response = self.client.get_sale_rate("btc_jpy")
        self.assertIsInstance(response, float)

        response = self.client.get_sale_rate("xem_btc")
        self.assertIsInstance(response, float)