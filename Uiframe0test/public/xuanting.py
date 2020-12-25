from selenium.webdriver.common.action_chains import ActionChains
import time

class MoveTo(object):
    def __init__(self, driver):
        self.driver = driver

    def moveto(self, way, text):  # way是定位方式，text是用来定位的信息
        if way == "xpath":
            ele = self.driver.find_element_by_xpath(text)
            ActionChains(self.driver).move_to_element(ele).perform()
            time.sleep(2)
        elif way == "css":
            ele = self.driver.find_element_by_css_selector(text)
            ActionChains(self.driver).move_to_element(ele).perform()
            time.sleep(2)
        elif way == "id":
            ele = self.driver.find_element_by_id(text)
            ActionChains(self.driver).move_to_element(ele).perform()
            time.sleep(2)
        elif way == "name":
            ele = self.driver.find_element_by_name(text)
            ActionChains(self.driver).move_to_element(ele).perform()
            time.sleep(2)
