import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


class Test_dw:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.baidu.com/")

    def test_dw(self):
        self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys("bilibili")
        self.driver.find_element(By.CSS_SELECTOR, '#su').click()
