# -*- coding: utf-8 -*-

from selenium import webdriver
import logging
import os
from time import sleep, time

logging.basicConfig(filename="log.txt", level=logging.DEBUG)
logger = logging.getLogger(__name__)

def find_currency_widget(driver):
    logger.info("Find all widgets on page")
    widgets = driver.find_elements_by_class_name(
            "personalized-widget")
    assert len(widgets) > 0, "No widgets on page at all"
    logger.info("Find all personalized widgets")
    currency = []
    for widget in widgets:
        headers = widget.find_elements_by_class_name("personalized-widget-title")
        logger.info("Checking headers name in found widgets")
        for header in headers:
            if header.text == u"Курсы":
                currency.append(widget)
    return currency
