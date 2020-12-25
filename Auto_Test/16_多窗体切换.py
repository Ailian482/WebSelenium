from selenium import webdriver
import time
driver = webdriver.Firefox()

# 打开百度
driver.get('https://www.baidu.com')
# 输入123
driver.find_element_by_id('kw').send_keys('123')
# 点击搜索
driver.find_element_by_id('su').click()
# 浏览器最大化
driver.maximize_window()
# 打印日志信息,打印出当前浏览器所有的窗体信息，一般是列表
print(driver.window_handles)

# 休眠5秒
time.sleep(5)

# 点击“hao123_上网从这里开始”
driver.find_element_by_xpath('//div[@id=1]/h3/a[1]').click()
time.sleep(3)
# 打印日志信息,打印出当前浏览器所有的窗体信息
print(driver.window_handles)

# 打印当前窗体焦点或句柄所在的窗体信息
print(driver.current_window_handle)

# 如果窗体焦点或句柄不在你想要的操作的窗体上，那么就不能操作窗体
# 切换窗体焦点或句柄到第二个窗体
driver.switch_to.window(driver.window_handles[1])
print(driver.current_window_handle)

# # 打印所有窗体信息
# print(driver.window_handles)
# # 切换窗体焦点或句柄到第一个窗体
# driver.switch_to.window(driver.window_handles[0])
# print(driver.current_window_handle)

time.sleep(2)
# close()和quit()方法区别
# ① 多窗体情况
# close()方法是关闭当前窗体焦点所在的窗体
driver.close()
time.sleep(3)
# 窗体虽然关闭了，但是窗体焦点还是在被关闭的窗体上，所以要进行窗体切换
driver.switch_to.window(driver.window_handles[0])

# quit()方法是关闭所有窗体
# 点击“hao123_上网从这里开始”
driver.find_element_by_xpath('//div[@id=1]/h3/a[1]').click()
time.sleep(3)
driver.quit()

# ② 单窗体情况,两种方法都是关闭窗口退出浏览器
# 打开百度,close()方法关闭
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
time.sleep(3)
driver.close()
# 打开百度,quit()方法关闭
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
time.sleep(3)

driver.quit()