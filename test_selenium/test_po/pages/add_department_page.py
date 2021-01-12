from selenium.webdriver.common.by import By

from test_selenium.test_po.pages.base_page import BasePage
from test_selenium.test_po.pages.contact_page import ContactPage


class AddDepartment(BasePage):

    def add_department(self):
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys("谢境")
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a').click()
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2] //*[@id="1688850120919824_anchor"]').click()
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()
        self.driver.refresh()

        return ContactPage(self.driver)

    def add_department_fail(self):
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys("谢境")
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a').click()
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2] //*[@id="1688850120919824_anchor"]').click()
        self.find(By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()

        return ContactPage(self.driver)
