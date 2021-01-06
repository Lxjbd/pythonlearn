import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.common.keys import Keys


class Test_click:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    @pytest.mark.skip
    def test_click(self):
        self.driver.get("http://sahitest.com/demo/clicks.htm")
        ele_click = self.driver.find_element(By.XPATH, '//input[@value="click me"]')
        ele_doubleclick = self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]')
        ele_clickright = self.driver.find_element(By.XPATH, '//input[@value="right click me"]')
        action = ActionChains(self.driver)
        action.click(ele_click)
        action.double_click(ele_doubleclick)
        action.context_click(ele_clickright)
        action.perform()

    @pytest.mark.skip
    def test_movetoele(self):
        self.driver.get("https://www.baidu.com/")
        ele = self.driver.find_element_by_xpath('//*[@id="s-usersetting-top"]')
        action = ActionChains(self.driver)
        action.move_to_element(ele)
        action.perform()

    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        ele_drag = self.driver.find_element_by_xpath('//*[@id="dragger"]')
        ele_drop1 = self.driver.find_element_by_xpath('/html/body/div[2]')
        ele_drop2 = self.driver.find_element_by_xpath('/html/body/div[3]')
        ele_drop3 = self.driver.find_element_by_xpath('/html/body/div[4]')
        ele_drop4 = self.driver.find_element_by_xpath('/html/body/div[5]')
        action = ActionChains(self.driver)
        action.drag_and_drop(ele_drag, ele_drop1).pause(2)
        action.drag_and_drop(ele_drag, ele_drop2).pause(2)
        action.drag_and_drop(ele_drag, ele_drop3).pause(2)
        action.drag_and_drop(ele_drag, ele_drop4)
        # action.click_and_hold(ele_drag).release(ele_drop1).pause(3)
        # action.click_and_hold(ele_drag).release(ele_drop4)
        action.perform()

    def test_keys(self):
        self.driver.get("http://sahitest.com/demo/label.htm")
        ele = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele.click()

        action = ActionChains(self.driver)
        action.send_keys("chiweilong").pause(1)
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys("hejingniang").pause(1)
        action.send_keys(Keys.BACK_SPACE)
        action.perform()