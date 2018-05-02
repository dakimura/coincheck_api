# -*- coding:utf-8 -*-

"""
general exception used in this module
"""


class CoinCheckApiException(Exception):

    def __init__(self, message):
        super(CoinCheckApiException, self).__init__(message)