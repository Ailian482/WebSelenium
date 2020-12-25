from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
# 最大化窗口，如果不最大化窗口，页面有些控件显示不全，做自动化的时候可能定位不到控件
driver.maximize_window()
time.sleep(3)

# 一、通过id定位元素
# 1. 通过id属性定位百度首页的“换一换”，并点击它
driver.find_element_by_id('hotsearch-refresh-btn').click()
time.sleep(2)
# 2. 通过id属性定位百度搜索框元素，并输入'哈哈'
driver.find_element_by_id('kw').send_keys('哈哈')
# 3. 用过id属性定位百度“搜索”按钮，并点击搜索
driver.find_element_by_id('su').click()
time.sleep(2)
# 关闭浏览器
driver.quit()