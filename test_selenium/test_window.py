from time import sleep

from selenium import webdriver


class TestWindow:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def test_window(self):
        self.driver.get("https://www.baidu.com/")
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        self.driver.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[3]/a').click()

        window = self.driver.window_handles
        self.driver.switch_to.window(window[-1])

        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__userName"]').send_keys("chiweilong")
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__phone"]').send_keys("190216558")
        sleep(2)
        self.driver.switch_to.window(window[0])
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__footerULoginBtn"]').click()

        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__userName"]').send_keys("chiweilong")
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__password"]').send_keys("liuyu123")
        sleep(1)
        self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_11__submit"]').click()