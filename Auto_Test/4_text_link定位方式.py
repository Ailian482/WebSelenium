from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
# 最大化窗口，如果不最大化窗口，页面有些控件显示不全，做自动化的时候可能定位不到控件
driver.maximize_window()
time.sleep(3)

# driver = webdriver.Firefox()
#
# driver.get('https://www.baidu.com')
# time.sleep(5)

# 四、通过link_text定位元素
# 1. 通过全文本定位百度首页的“hao123”按钮，并且点击它
driver.find_element_by_link_text('hao123').click()
time.sleep(2)
print(driver.window_handles)
print(driver.current_window_handle)
# 2. 通过全文本定位hao123首页的“hao123新闻”按钮，并且点击它
driver.switch_to.window(driver.window_handles[1])
driver.find_element_by_link_text('hao123新闻').click()
time.sleep(2)

driver.quit()