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

# 三、通过class_name定位元素，如果属性值有空格的说明是复合类，不要用，会定位不到
# 1. 通过class属性定位百度首页的“换一换”按钮，并点击它
driver.find_element_by_class_name('hot-refresh-text').click()
time.sleep(2)
# 2. 通过class属性定位百度搜索框元素，并输入'哈哈'
driver.find_element_by_class_name('s_ipt').send_keys('哈哈')
time.sleep(2)

driver.quit()