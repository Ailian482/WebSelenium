# 首先要导入键盘事件类
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://101.133.169.100/yuns/index.php')

# 模拟单个的键盘事件，直接send_keys(Keys.变量名) 调用键盘按键方法，
# 如果是Ctrl+a、Ctrl+x、Ctrl+v，send_keys(Keys.变量名,'相应参数')

# 在输入框中输入“女装”
driver.find_element_by_xpath('//input[@class="but1"]').send_keys('女装')
time.sleep(2)
# 17. 模拟键盘的回退键，send_keys(Keys.BACK_SPACE)
driver.find_element_by_xpath('//input[@class="but1"]').send_keys(Keys.BACK_SPACE)
time.sleep(2)
# 在输入框中输入“装”
driver.find_element_by_xpath('//input[@class="but1"]').send_keys('装')
time.sleep(2)
# 18. 模拟键盘的空格键，send_keys(Keys.SPACE)
driver.find_element_by_xpath('//input[@class="but1"]').send_keys(Keys.SPACE)
time.sleep(2)
# 在输入框中输入“夏装”
driver.find_element_by_xpath('//input[@class="but1"]').send_keys('夏')
time.sleep(2)
# 19. 模拟键盘的全选Ctrl+a，send_keys(Keys.(CONTROL,'a'))
driver.find_element_by_xpath('//input[@class="but1"]').send_keys(Keys.CONTROL,'a')
time.sleep(2)
# 20. 模拟键盘的剪切Ctrl+x，send_keys(Keys.(CONTROL,'x'))
driver.find_element_by_xpath('//input[@class="but1"]').send_keys(Keys.CONTROL,'x')
time.sleep(2)
# 21. 模拟键盘的粘贴Ctrl+v，send_keys(Keys.(CONTROL,'v'))
driver.find_element_by_xpath('//input[@class="but1"]').send_keys(Keys.CONTROL,'v')
time.sleep(2)

# 注意：全选然后复制粘贴，应该复制后点一下输入框，然后才会在原来内容后面继续添加信息
driver.find_element_by_xpath('//input[@class="but1"]').send_keys(Keys.CONTROL,'a')
time.sleep(2)
# 22. 模拟键盘的复制Ctrl+c，send_keys(Keys.(CONTROL,'c'))
driver.find_element_by_xpath('//input[@class="but1"]').send_keys(Keys.CONTROL,'c')
time.sleep(2)
# # 清空输入框
# driver.find_element_by_xpath('//input[@class="but1"]').clear()
# time.sleep(2)
# 把前面复制的内容粘贴到输入框
driver.find_element_by_xpath('//input[@class="but1"]').send_keys(Keys.CONTROL,'v')
time.sleep(2)

# 点击搜索
driver.find_element_by_xpath('//input[@class="but2"]').click()
time.sleep(3)

driver.quit()