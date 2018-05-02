import sys,os
import unittest

# add root dir of this module to classpath
#sys.path.append(os.path.dirname(os.path.abspath(__file__)) +"/../")
from coincheck_api import Client, settings


class TestAccount(unittest.TestCase):
    """Test class of client.py
    """
    def setUp(self):
        self.client = Client(settings.access_key, settings.secret)

    def test_get_sale_rate(self):
        rate = self.client.get_sale_rate("btc_jpy")
        self.assertTrue( isinstance(rate, float))

        # self.assertGreater( rate, 1800000.0, "please...")

    def test_get_account_balance(self):
        response = self.client.get_account_balance()
        self.assertEqual(response["success"], True)
