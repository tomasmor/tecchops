# -*- coding: utf-8 -*-

from selenium import webdriver
import logging

from basic import find_currency_widget, logger


class TestWidgetExists(object):
    def test_check_widget_exists(self, browser_handler):
        """
        Check that widget with currency exists.
        """
        currency = find_currency_widget(browser_handler)
        assert len(currency) > 0, "No widgets with currency found"
        logger.info(len(currency))
        if len(currency) > 1:
            logger.warning("There are two  more widgets with currency")
