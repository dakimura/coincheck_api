# -*- coding:utf-8 -*-
import hashlib
import hmac
import time


def create_auth_headers(url, access_key, secret, body=None):
    """
    get HTTP headers for API authentication
    :param url: API url. (e.g. https://coincheck.com/api/accounts/balance )
    :param access_key: Access Key string for API authentication
    :param secret: Secret Access Key string for API authentication
    :return: HTTP header dictionary
    """
    current_millis = str(int(round(time.time() * 1000)))
    message = current_millis + url + body
    signature = hmac.new(secret.encode("utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest()
    headers = {
        "ACCESS-KEY": access_key,
        "ACCESS-NONCE": current_millis,
        "ACCESS-SIGNATURE": signature
    }
    return headers
