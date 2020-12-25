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

# 二、通过name定位元素
# 1. 通过name属性定位百度的搜索框元素，并输入'哈哈'
driver.find_element_by_name('wd').send_keys('哈哈')
time.sleep(2)
# 2. 通过name属性定位百度首页的“更多”按钮，并且点击它
driver.find_element_by_name('tj_briicon').click()
time.sleep(2)

driver.quit()