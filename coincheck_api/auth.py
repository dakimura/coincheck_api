# -*- coding:utf-8 -*-
import time
import hmac
import hashlib


def create_auth_headers(url, *, access_key, secret):
    """
    get HTTP headers for API authentication
    :param url: API url. (e.g. https://coincheck.com/api/accounts/balance )
    :param access_key: Access Key string for API authentication
    :param secret: Secret Access Key string for API authentication
    :return: HTTP header dictionary
    """
    current_millis = str(round(time.time() * 1000))
    message = current_millis + url
    signature = hmac.new(secret.encode("utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest()
    headers = {
        "ACCESS-KEY": access_key,
        "ACCESS-NONCE": current_millis,
        "ACCESS-SIGNATURE": signature
    }
    return headers
