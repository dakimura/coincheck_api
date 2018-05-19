# -*- coding:utf-8 -*-
import json
from logging import getLogger

import requests

from coincheck_api.exception import CoinCheckApiException

logger = getLogger(__name__)


class ApiClient:
    base_url = "https://coincheck.com"

    def __init__(self):
        pass

    def execute_http_call(self, path, method, headers=None, data=None):
        """
        :param path: API path (e.g. /api/ticker )
        :param method: HTTP method in string. "GET", "POST", "PUT", "DELETE"
        :param headers: HTTP headers dictionary
        :param data: parameter dictionary to send. e.g. ({"key1":"value1", "key2":"value2"}
        :return: response in json-deserialized dictionary object
        """
        url = self.base_url + path

        logger.debug("HTTP call executed. url={}, method={}, headers={}".format(url, method, headers))

        # execute an HTTP call
        response = requests.request(method, url, headers=headers, data=data)
        logger.debug("HTTP status code of response={} {}".format(response.status_code, response.content))

        response_body = json.loads(response.content)
        # success
        if 200 <= response.status_code < 400:
            return response_body
        # failure
        else:
            raise CoinCheckApiException(
                "API execute failure. response status_code={}, headers={}, body={}".format(
                    response.status_code, response.headers, response.content
                ))
