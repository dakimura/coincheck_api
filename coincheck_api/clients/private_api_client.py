# -*- coding:utf-8 -*-
import coincheck_api.auth
from coincheck_api.clients.api_client import ApiClient
from logging import getLogger
logger = getLogger(__name__)

try:
    # python2
    from urllib import urlencode
except ImportError:
    # python3
    from urllib.parse import urlencode


class PrivateApiClient(ApiClient):
    """
    In order to use private APIs (e.g. Order, Account balance check)
    You should create an API key in advance.
    https://coincheck.com/ja/documents/exchange/api#auth
    """

    def __init__(self, access_key, secret):
        self.access_key = access_key
        self.secret = secret

    def execute_private_api(self, path, method, data=None):
        """
        execute an api which needs authentication headers
        :param path: API path (e.g. /api/ticker )
        :param method: HTTP method in string. "GET", "POST", "PUT", "DELETE"
        :param data: parameter dictionary to send. e.g. ({"key1":"value1", "key2":"value2"}
        :return: response in json-deserialized dictionary object
        """
        url = ApiClient.base_url + path
        body = ""
        if method in ["POST", "PUT", "DELETE"] and data is not None:
            body = urlencode(data)
        headers = coincheck_api.auth.create_auth_headers(
            url,
            access_key=self.access_key,
            secret=self.secret,
            body=body)

        return self.execute_http_call(path, method, headers, data)
