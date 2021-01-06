import json
from time import sleep

from selenium import webdriver


class TestWechat:
    def setup(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)
        self.driver.maximize_window()

    def test_cookie(self):
        # cookies = self.driver.get_cookies()
        # with open("cookie.json", "w") as f:
        #     json.dump(cookies, f)

        self.driver.get("https://work.weixin.qq.com/")

        with open("cookie.json", "r") as f:
            cookies = json.load(f)

        for cookie in  cookies:
            self.driver.add_cookie(cookie)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(2)
        self.driver.find_element_by_xpath('//*[@id="menu_customer"]/span').click()