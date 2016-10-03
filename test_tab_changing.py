# -*- coding: utf-8 -*-

from selenium import webdriver
import logging
from time import sleep, time


from basic import find_currency_widget

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger()

class TestTabChanging(object):
    def test_tab_changing(self, browser_handler):
        currency = find_currency_widget(browser_handler)
        assert len(currency) > 0, "No widgets with currency found"
        widget = currency[0]
        logger.info("Find tab with inforamtion about metals")
        metal = widget.find_element_by_xpath("//*[@data-type='metal']")
        metal.click()
        logger.info("After click metal tab should be active")
        def wait_for_state_change(timeout=1, poke_interval=0.1):
            start = time()
            metal_after_click = currency[0].find_element_by_xpath(
                "//*[@data-type='metal']")
            while time() < start + timeout:
                if metal_after_click.get_attribute("class") == "active":
                    return True
                else:
                    sleep(poke_interval)
            logger.info("Timeout of waiting was exceeded")
            assert False
        wait_for_state_change()
