# -*- coding: utf-8 -*-

from selenium import webdriver
import logging
from time import sleep, time

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

def find_currency_widget(driver):
    logger.info("Find all widgets on page")
    widgets = driver.find_elements_by_class_name(
            "personalized-widget")
    assert len(widgets) > 0, "No widgets on page at all"
    logger.info("Find currency widget")
    currency = []
    for widget in widgets:
        headers = widget.find_elements_by_class_name("personalized-widget-title")
        for header in headers:
            if header.text == u"Курсы":
                currency.append(widget)
    return currency
