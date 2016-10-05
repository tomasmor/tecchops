# -*- coding: utf-8 -*-

from selenium import webdriver
import logging
from time import sleep, time

from basic import find_currency_widget, logger

class TestRedirect(object):
    def test_check_redirect(self, browser_handler, url_for_redirect):
        """
        Check widget is redirecting user to the page with currency
        """
        currency = find_currency_widget(browser_handler)
        assert len(currency) > 0, "No widgets with currency found"
        for widget in currency:
            logger.info("Find widget body to click")
            body = widget.find_element_by_class_name("currency-body")
            body.click()
            assert browser_handler.current_url == url_for_redirect,"Widget redirected to the wrong page"
