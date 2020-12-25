from selenium import webdriver
import time
driver = webdriver.Chrome()

# driver.get('https://www.baidu.com')
driver.get('http://101.133.169.100/yuns/index.php/')
# 最大化窗口，如果不最大化窗口，页面有些控件显示不全，做自动化的时候可能定位不到控件
driver.maximize_window()
time.sleep(3)

# driver = webdriver.Firefox()
#
# driver.get('https://www.baidu.com')
# time.sleep(5)

# 一、通过partial_link_text定位元素
# # 1. 通过部分文本定位百度首页的“百度营销”按钮，并且点击它
# driver.find_element_by_partial_link_text('营销').click()
# time.sleep(2)
# # 2. 通过部分文本定位百度首页的“使用百度前必读”按钮，并且点击它
# driver.find_element_by_partial_link_text('使用百').click()
# time.sleep(2)

driver.find_element_by_link_text('女装 优质长绒棉A字型条纹连衣裙(').click()
time.sleep(2)

driver.quit()