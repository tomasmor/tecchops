# -*- coding: utf-8 -*-

from selenium import webdriver
import logging
from time import sleep, time


from basic import find_currency_widget

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class TestRedirect(object):
    def test_check_redirect(self, browser_handler, url_for_redirect):
        currency = find_currency_widget(browser_handler)
        assert len(currency) > 0, "No widgets with currency found"
        widget = currency[0]
        logger.info("Find widget body to click")
        body = widget.find_element_by_class_name("currency-body")
        body.click()
        assert browser_handler.current_url == url_for_redirect,"Widget redirected to the wrong page"
