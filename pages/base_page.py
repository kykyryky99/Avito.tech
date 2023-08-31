from urllib.parse import urlparse

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


class BasePage(object):
    def __init__(self, url: str, timeout: int = 10):
        self.driver: WebDriver = webdriver.Chrome()
        self.driver.implicitly_wait(timeout)

        self.url = url

    def open_page(self, url: str):
        self.driver.get(url)

