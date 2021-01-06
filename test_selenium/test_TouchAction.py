from selenium import webdriver
from selenium.webdriver import TouchActions


class Test_click:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_touch(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_id("kw")
        ele_search = self.driver.find_element_by_id("su")

        ele.send_keys("bilibili")
        action = TouchActions(self.driver)
        action.tap(ele_search)
        action.perform()

        action.scroll_from_element(ele, 0, 10000).perform()