from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://101.133.169.100/yuns/index.php')
# 最大化窗口，如果不最大化窗口，页面有些控件显示不全，做自动化的时候可能定位不到控件


# send_keys和clear主要是用在输入框，click所有控件都能点击
# 4. 在输入框输入内容：send_keys()
driver.find_element_by_name('key').send_keys('女装')
time.sleep(2)
# driver.find_element_by_css_selector('.but2').click()
# 5. 清空输入框的内容：clear()
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').clear()
# time.sleep(2)
# 6. 点击"夏天最热"按钮
driver.find_element_by_link_text('夏天最热').click()
# 7. 点击"优惠券"按钮
driver.find_element_by_xpath('//div[@class="nav_pub"]/a[3]').click()
