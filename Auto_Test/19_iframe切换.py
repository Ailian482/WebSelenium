from selenium import webdriver
import time

driver = webdriver.Chrome()

# 错误信息为：Message: no such element，一般原因有以下几个方面
# ① 等待时间不够，控件还没有加载出来
# ② 定位方式写错了
# ③ 多窗体情况下，窗体焦点不在要定位的窗体上
# ④ 有iframe，插了一个新的html页面

# 下面讲述有iframe的情况，如何处理

# 进入126邮箱
driver.get('https://mail.126.com/')
driver.maximize_window()
time.sleep(8)

# 按照我们平时写的定位方式直接去定位，报错了！
# # 定位账号输入框，输入账号
# mail_name = driver.find_element_by_name('email')
# mail_name.send_keys('Ailian_1104')
# # 定位密码输入框，输入密码
# mail_pwd = driver.find_element_by_name('password')
# mail_pwd.send_keys('ailian1104')

# 一、从iframe外面的html切换到iframe里面的html去
# 检查网页代码，发现html里面有一个iframe里面还插入了一个新的html
# 解决方法：先切换到iframe里面，再找控件；如果嵌套多个iframe，只能一层一层切换，不能跨层切换
# 下面看实现代码：
# 1. 定位到iframe
# ① 方法1：如果iframe标签有id或name属性，属性值不为空且不为动态变化的，那么直接把属性值传进去，switch_to.frame('属性值')
# driver.switch_to.frame('x-URS-iframe1608100383110.1702') # x-URS-iframe后面的一串数字是动态变化的，所以不能直接用该值
# ② 方法2（也是万能方法）：可以用xpath或其他方法定位
to_iframe = driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
# to_iframe = driver.find_element_by_xpath('//iframe[contains(@id,"x-URS-iframe")]')
# to_iframe = driver.find_element_by_xpath('//iframe[starts-with(@id,"x-URS-iframe")]')
# to_iframe = driver.find_element_by_css_selector('div#loginDiv>iframe')

# 2. 切到iframe里面
driver.switch_to.frame(to_iframe)
# 3. 定位账号输入框，输入账号
mail_name = driver.find_element_by_name('email')
mail_name.send_keys('Ailian_1104')
# 4. 定位密码输入框，输入密码
mail_pwd = driver.find_element_by_name('password')
mail_pwd.send_keys('ailian1104')
# 5. 点击登录
login = driver.find_element_by_id('dologin')
login.click()
time.sleep(5)

# 二、从iframe里面的html切换到iframe外面的html去
driver.switch_to.parent_frame() # 从子frame切回到父frame，不能跨层返回
# driver.switch_to.default_content() # 从frame切回主文档
# 点击登录成功后的通讯录按钮
driver.find_element_by_id('_mail_tabitem_1_117text').click()

driver.quit()