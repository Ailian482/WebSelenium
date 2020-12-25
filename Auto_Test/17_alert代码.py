from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://101.133.169.100/yuns/index.php')

# 什么是alert？就是鼠标右击不能查看元素的就是alert，如果鼠标右击可以查看元素的就不是alert
# 如何操作alert？请看下面分解
# ① 往alert输入框输入内容
driver.switch_to.alert.send_keys('test')
time.sleep(2)
# ② 获取alert上的文本信息
print(driver.switch_to.alert.text)
# ③ 点击确定、保存、confirm等正向按钮
driver.switch_to.alert.accept()
# ④ 点击取消按钮、不保存、cancel等反向按钮
driver.switch_to.alert.dissmis()
driver.quit()