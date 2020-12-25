
from selenium import webdriver
# -*- coding:UTF-8 -*-
import time
# 打开浏览器，进入携程旅行官网
driver = webdriver.Chrome()
# 进入携程旅行官网（普通时间控件）
# driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
# 进入铁路12306官网（有readonly属性的时间控件）
driver.get('https://www.12306.cn/index/')
driver.maximize_window() # 最大化窗口
# 休眠5秒钟
time.sleep(5)

# 时间控件有普通时间控件和带有readonly="readonly"属性两种
# 时间控件是一个input标签，用浏览器的检查元素是检查不到，那么如何输入时间呢？
# 1、对于普通时间控件
# 定位时间输入框控件，先把默认值清空，然后用send_keys()方法直接往输入框输入时间
# 要注意的点是：输入的时间的格式要与输入框控件value属性设置的格式一致
# # 输入入住日期
# # ① 定位输入框
# tbox = driver.find_element_by_id('HD_CheckIn')
# # ② 清空输入框默认值
# tbox.clear()
# # ③ 按格式输入日期，月份和日如果输入的是一位数，程序会自动用0补全为两位数
# tbox.send_keys('2019-1-2')
# # ④ 打印输入的日期
# print(tbox.get_attribute("value"))
# # 输入退房日期
# tbox_out = driver.find_element_by_id('HD_CheckOut')
# tbox_out.clear()
# tbox_out.send_keys('2019-1-3')
# print(tbox_out.get_attribute("value"))
#
# time.sleep(5)
# driver.quit()

# 2、对于有readonly属性的时间控件
# ① 需要调用用js方法定位到时间控件并用.removeAttribute('属性名')把readonly属性去掉，有三种方法定位
# a.通过id属性定位到时间控件.getElementById('id属性值')
# js = "document.getElementById('train_date').removeAttribute('readonly')"

# b.通过name属性定位到时间控件.getElementsByName('name属性值')
# 找到的是当前html页面所有 name 是'name属性值'的控件，放到一个列表里面
# js = "document.getElementsByName('train_date')[0].removeAttribute('readonly')"

# c.通过标签类型(tag_name)定位到时间控件.getElementsByTagName('input')[第几个]
# 找到的是当前html页面所有标签类型是 input 的控件，放到一个列表里面
js = "document.getElementsByTagName('input')[6].removeAttribute('readonly')"

# ② 通过execute_script()方法执行js
driver.execute_script(js)
# ③ 定位输入框，清空默认值，并且输入相应格式的日期
t = driver.find_element_by_xpath("//input[@id='train_date']")
# t = driver.find_element_by_id('train_date')
t.clear()  # 清空默认值
time.sleep(2)  # 休眠2秒看效果
t.send_keys('2020-1-1')  # 输入日期
time.sleep(5)

driver.quit()