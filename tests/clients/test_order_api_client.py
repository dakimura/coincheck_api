import logging
import unittest

from coincheck_api import settings
from coincheck_api.clients.order_api_client import OrderApiClient
from coincheck_api.exception import CoinCheckApiException


class TestOrderApi(unittest.TestCase):
    """Test class of order_api_client.py
    """

    def setUp(self):
        logging.basicConfig(
            format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s',
            level=logging.DEBUG)
        self.client = OrderApiClient(settings.access_key, settings.secret)

    def test_buy(self):
        # self.client.buy(rate=5000, btc_amount=0.1, dry_run=False)
        response = self.client.buy(rate=5000, btc_amount=0.1, dry_run=True)
        self.assertEqual(response["success"], True)

    def test_sell(self):
        response = self.client.sell(rate=20000000, btc_amount=0.005, dry_run=True)
        self.assertEqual(response["success"], True)

    def test_market_buy(self):
        response = self.client.market_buy(jpy_amount=500, dry_run=True)
        self.assertEqual(response["success"], True)

    def test_market_sell(self):
        response = self.client.market_sell(btc_amount=0.005, dry_run=True)
        self.assertEqual(response["success"], True)

    def test_leverage_buy(self):
        response = self.client.leverage_buy(rate=5000, btc_amount=0.1, dry_run=True)
        self.assertEqual(response["success"], True)

    def test_leverage_sell(self):
        response = self.client.leverage_sell(rate=5000, btc_amount=0.1, dry_run=True)
        self.assertEqual(response["success"], True)
