# -*- coding:utf-8 -*-

import json
from logging import getLogger

from coincheck_api.clients.private_api_client import PrivateApiClient
from coincheck_api.exception import CoinCheckApiException

logger = getLogger(__name__)


class OrderApiClient(PrivateApiClient):

    def __init__(self, access_key, secret):
        PrivateApiClient.__init__(self, access_key, secret)

    def buy(self, rate, btc_amount, dry_run=False):
        """
        buy bitcoin at limit
        :param rate: rate of btc/jpy (e.g. 1200000)
        :param btc_amount: amount of bitcoin (e.g. 0.1)
        :param dry_run: for debug. when true, order is not actually executed
        :return: order information
        """
        if rate is None:
            raise CoinCheckApiException("you need to specify rate when order at a limit price")
        return self.order(order_type="buy", rate=rate, amount=btc_amount, dry_run=dry_run)

    def sell(self, rate, btc_amount, dry_run=False):
        """
        sell bitcoin at limit
        :param rate: rate of btc/jpy (e.g. 1200000)
        :param btc_amount: amount of bitcoin (e.g. 0.1)
        :param dry_run: for debug. when true, order is not actually executed
        :return: order information
        """
        if rate is None:
            raise CoinCheckApiException("you need to specify rate when order at a limit price")
        return self.order(order_type="sell", rate=rate, amount=btc_amount, dry_run=dry_run)

    def market_buy(self, jpy_amount, dry_run=False):
        """
        buy bitcoin without limit.
        [CAUTION] !!!!!! you need to specify "JPY" amount, not "BTC" amount !!!!!!!!
        it's due to the weird api spec of coincheck
        https://coincheck.com/ja/documents/exchange/api#order-new
        :param jpy_amount: amount of JPY to buy without llimit
        :param dry_run: for debug. when true, order is not actually executed
        :return: order information
        """
        return self.order("market_buy", rate=None, amount=None, market_buy_amount=jpy_amount, dry_run=dry_run)

    def market_sell(self, btc_amount, dry_run=False):
        """
        sell bitcoin without limit.
        :param btc_amount: amount of btc to sell without limit
        :param dry_run: for debug. when true, order is not actually executed
        :return: order information
        """
        return self.order("market_sell", rate=None, amount=btc_amount, dry_run=dry_run)

    def leverage_buy(self, rate, btc_amount, dry_run=False):
        """
        buy bitcoin at a certain price in a leveraged order
        :param rate: rate of btc/jpy (e.g. 1200000)
        :param btc_amount: amount of bitcoin to buy
        :param dry_run: for debug. when true, order is not actually executed
        :return: order information
        """
        return self.order("leverage_buy", rate=rate, amount=btc_amount, dry_run=dry_run)

    def leverage_sell(self, rate, btc_amount, dry_run=False):
        """
        sell bitcoin at a certain price in a leveraged order
        :param rate: rate of btc/jpy (e.g. 1200000)
        :param btc_amount: amount of bitcoin to sell
        :param dry_run: for debug. when true, order is not actually executed
        :return: order information
        """
        return self.order("leverage_sell", rate=rate, amount=btc_amount, dry_run=dry_run)

    def leverage_market_buy(self, btc_amount, dry_run=False):
        """
        buy bitcoin without limit in a leverage order
        :param btc_amount: amount of bitcoin to buy
        :param dry_run: for debug. when true, order is not actually executed
        :return: order information
        """
        return self.order("leverage_buy", rate=None, amount=btc_amount, dry_run=dry_run)

    def leverage_market_sell(self, btc_amount, dry_run=False):
        """
        sell bitcoin without limit in a leverage order
        :param btc_amount: amount of bitcoin to sell
        :param dry_run: for debug. when true, order is not actually executed
        :return: order information
        """
        return self.order("leverage_sell", rate=None, amount=btc_amount, dry_run=dry_run)

    def close_long(self, rate, btc_amount, position_id, dry_run=False):
        """
        close a position by selling bitcoin at a certain price
        :param rate: rate of btc/jpy (e.g. 1200000)
        :param btc_amount: amount of bitcoin to sell
        :param position_id: id issued when ordered
        :param dry_run: for debug. when true, order is not actually executed
        :return:
        """
        return self.order("close_long", rate=rate, amount=btc_amount, position_id=position_id, dry_run=dry_run)

    def close_short(self, rate, btc_amount, position_id, dry_run=False):
        """
        close a position by selling bitcoin at a certain price
        :param rate: rate of btc/jpy (e.g. 1200000)
        :param btc_amount: amount of bitcoin to sell
        :param position_id: id issued when ordered
        :param dry_run: for debug. when true, order is not actually executed
        :return:
        """
        return self.order("close_short", rate=rate, amount=btc_amount, position_id=position_id, dry_run=dry_run)

    def market_close_long(self, btc_amount, position_id, dry_run=False):
        """
        close a position by selling bitcoin without limit
        :param btc_amount: amount of bitcoin to sell
        :param position_id: id issued when ordered
        :param dry_run: for debug. when true, order is not actually executed
        :return:
        """
        return self.order("close_long", rate=None, amount=btc_amount, position_id=position_id, dry_run=dry_run)

    def market_close_short(self, btc_amount, position_id, dry_run=False):
        """
        close a position by selling bitcoin without limit
        :param btc_amount: amount of bitcoin to sell
        :param position_id: id issued when ordered
        :param dry_run: for debug. when true, order is not actually executed
        :return:
        """
        return self.order("close_short", rate=None, amount=btc_amount, position_id=position_id, dry_run=dry_run)

    def order(self, order_type, rate, amount, market_buy_amount=None,
              position_id=None, stop_loss_rate=None, pair="btc_jpy", dry_run=False):
        """
        order
        :param order_type: one of ["buy", "sell", "market_buy", "market_sell",
                              "leverage_buy", "leverage_sell", "close_long", "close_short"]
        :param rate: rate to order
        :param amount: amount of bitcoin to order
        :param market_buy_amount: amount of JPY to buy without limit
        :param position_id: position_id to close
        :param stop_loss_rate: stop_loss_rate to order.
        for instance, if order_type="buy", rate=48400 and stop_loss_rate=48300,
        when btc/jpy exceeds 48300, order is executed.
        if order_type="sell", rate=None and stop_loss_rate=48400,
        when btc/jpy falls below 48400, sell order is executed without limit.
        cf. https://coincheck.com/ja/info/faq_posts/35
        :param pair: currency pair. As of 2018-05, only "btc_jpy" is supported.
        :param dry_run: for debug. when it's true, order is not executed actually.
        :return:
        """
        if order_type not in ["buy", "sell", "market_buy", "market_sell",
                              "leverage_buy", "leverage_sell", "close_long", "close_short"]:
            raise CoinCheckApiException("""order_type should be one of [buy, sell, 
            market_buy, market_sell,leverage_buy, leverage_sell, close_long, close_short""")

        data = {"order_type": order_type, "pair": pair}
        if rate is not None:
            data["rate"] = rate
        if amount is not None:
            data["amount"] = amount
        if market_buy_amount is not None:
            data["market_buy_amount"] = market_buy_amount
        if position_id is not None:
            data["position_id"] = position_id
        if stop_loss_rate is not None:
            data["stop_loss_rate"] = stop_loss_rate

        if dry_run:
            logger.info("[dry run] order is executed. request data={}".format(json.dumps(data)))
            return {"success": True, "id": 12345, "rate": str(rate), "amount": str(amount),
                    "order_type": order_type, "stop_loss_rate": stop_loss_rate, "pair": pair,
                    "created_at": "2015-01-10T05:55:38.000Z"}
        else:
            response = self.execute_private_api("/api/exchange/orders", "POST", data=data)
            logger.info("order is executed. request data={}".format(data))
            return response

    def get_open_orders(self):
        """
        get open orders
        :return: open orders
        """
        return self.execute_private_api("/api/exchange/orders/opens", "GET")

    def cancel_open_order(self, order_id):
        """
        cancel an open order
        :param order_id: id of the order the user wants to cancel
        :return: canceled order id
        """
        return self.execute_private_api("/api/exchange/orders/{}".format(order_id), "DELETE")

    def get_order_transactions(self):
        """
        get recent orders' information
        :return: recent orders' information
        """
        return self.execute_private_api("/api/exchange/orders/transactions", "GET")

    def get_order_transactions_pagination(self, limit=None, order=None, start_id=None, end_id=None):
        """
        get recent orders' information with pagination functionality
        :param limit: the number of items to get
        :param order: "desc" or "asc"
        :param start_id: get items after the id
        :param end_id: get items before the id
        :return: recent orders' information
        """
        data = {"limit": limit, "order": order, "starting_after": start_id, "ending_before": end_id}
        return self.execute_private_api("/api/exchange/orders/transactions_pagination", "GET", data=data)

    def get_leverage_positions(self, status, limit=None, order=None, start_id=None, end_id=None):
        """
        get positions in a certain status with pagination functionality
        :param status: "open" or "closed"
        :param limit: the number of items to get
        :param order: "desc" or "asc"
        :param start_id: get items after the id
        :param end_id: get items before the id
        :return: positions in a certain status
        """
        if status not in ["open", "closed"]:
            raise CoinCheckApiException("status should be \"open\" or \"closed\".")
        data = {"limit": limit, "order": order, "starting_after": start_id, "ending_before": end_id}
        return self.execute_private_api("/api/exchange/leverage/positions", "GET", data=data)
