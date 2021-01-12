from selenium.webdriver.common.by import By

from test_selenium.test_po.pages.add_department_page import AddDepartment
from test_selenium.test_po.pages.base_page import BasePage


class MainPage(BasePage):
    def goto_addpartment(self):
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        self.driver.find_element(By.XPATH, '//*[@id="js_contacts47"]/div/div[1]/div/div[1]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="js_contacts47"]/div/div[1]/ul/li[1]/a').click()

        return AddDepartment(self.driver)

