import sys,os
import unittest
from coincheck_api import Client, settings
import logging


class TestAccount(unittest.TestCase):
    """Test class of client.py
    """
    def setUp(self):
        logging.basicConfig(
            format='[%(asctime)s - %(name)s - %(levelname)s] %(message)s',
            level=logging.DEBUG)
        self.client = Client(settings.access_key, settings.secret)

    def test_get_sale_rate(self):
        rate = self.client.get_sale_rate("btc_jpy")
        self.assertTrue( isinstance(rate, float))

        # self.assertGreater( rate, 1800000.0, "please...")

    def test_get_account_balance(self):
        response = self.client.get_account_balance()
        self.assertEqual(response["success"], True)
