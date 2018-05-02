#-*- coding:utf-8 -*-
"""
get logger for this module.
usage from other classes in this module:
    from <this module's name> import get_module_logger
    logger = get_module_logger(__name__)
"""

from logging import getLogger,StreamHandler,Formatter,DEBUG


# logging template
def get_module_logger(modname):
    """
    :param modname: module name
    :return: logger for this module
    """
    logger = getLogger(modname)
    handler = StreamHandler()
    formatter = Formatter('[%(asctime)s - %(name)s - %(levelname)s] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(DEBUG)
    logger.propagate = False
    return logger