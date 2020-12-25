import time

class NewPage(object):
    def __init__(self, driver):
        self.driver = driver

    def l_newpage(self, text):  # 控件文本信息定位
        self.driver.find_element_by_link_text(text).click()
        time.sleep(2)
        if len(self.driver.window_handles) >= 2:
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(5)
        else:
            pass

    def p_newpage(self, xpath):  # xpath定位方式
        self.driver.find_element_by_xpath(xpath).click()
        time.sleep(2)
        if len(self.driver.window_handles) >= 2:
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(5)
        else:
            pass

    def c_newpage(self, css):  # css_selector定位方式
        self.driver.find_element_by_css_selector(css).click()
        time.sleep(2)
        if len(self.driver.window_handles) >= 2:
            self.driver.switch_to.window(self.driver.window_handles[1])
            time.sleep(5)
        else:
            pass