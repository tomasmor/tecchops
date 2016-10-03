import pytest
from selenium import webdriver

from lxml import etree

def basic_url():
    tree = etree.parse("config.xml")
    return tree.xpath("//url")[0].text

def browsers():
    tree = etree.parse("config.xml")
    browsers_list = [node.text for node in tree.xpath("//browser")]
    return browsers_list

@pytest.fixture()
def url_for_redirect():
    tree = etree.parse("config.xml")
    return tree.xpath("//redirected_url")[0].text

@pytest.fixture(params=browsers())
def browser_handler(request):
    browser_type = request.param
    driver = getattr(webdriver, browser_type)()
    driver.implicitly_wait(10)
    driver.get(basic_url())
    def browser_teardown():
        driver.quit()
    request.addfinalizer(browser_teardown)
    return driver
