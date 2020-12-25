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

# 一、通过id、name、class_name、link_text、partial_link_text、tag_name定位元素

# 12. 通过tag_name找百度首页的一组div标签类型，返回的结果会被存储在列表中，一般不用这种方法
ele = driver.find_elements_by_tag_name('div')
print(len(ele))
