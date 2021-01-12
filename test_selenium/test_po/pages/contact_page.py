from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_selenium.test_po.pages.base_page import BasePage


class ContactPage(BasePage):

    def get_list(self):
        # def wait(x):
        #     return len(self.driver.find_elements_by_xpath('//ul[@role="group"] //li')) >=2
        # WebDriverWait(self.driver, 10).until(wait)
        name_ele_list = self.driver.find_elements_by_xpath('//ul[@role="group"] //li')
        name_list = []
        for ele in name_ele_list:
            ele = ele.text.strip()
            name_list.append(ele)

        return name_list

    def get_toast(self):
        toast = self.driver.find_element_by_xpath('//*[@id="js_tips"]')
        toast = toast.text
        return toast
