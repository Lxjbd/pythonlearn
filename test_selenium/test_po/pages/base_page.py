import json

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:

    def __init__(self, base_driver=None):
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Chrome()
            self._test_cookie()
        else:
            self.driver = base_driver
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def _test_cookie(self):
        # cookies = self.driver.get_cookies()
        # with open("cookie.json", "w") as f:
        #     json.dump(cookies, f)

        self.driver.get("https://work.weixin.qq.com/")

        with open("../cookie.json", "r") as f:
            cookies = json.load(f)

        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")

    def find(self, by, value):
        return self.driver.find_element(by=by, value=value)
