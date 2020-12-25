# 首先要导入一个Select类
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
# 打开浏览器，进入携程旅行官网
driver = webdriver.Chrome()
driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
driver.maximize_window() # 最大化窗口
# 休眠5秒钟
time.sleep(5)

# 通过Select类选择下拉框选项，只能是控件类型(tag_name)为select的控件
# 下拉框的选项都是属于下拉选择框，所以先要定位下拉选择框，然后再进行选择
# 如果下拉框的控件类型是dt(是一个表格)，那么先要定位点击下拉选择框，然后再定位选项，点击选项
# 选择select标签类型下拉框的选项的方法：
# ① 通过选择项可见文本进行选择:Select(下拉框控件定位).select_by_visible_text(option标签的文本)
s = driver.find_element_by_id('J_roomCountList')
Select(s).select_by_visible_text('6间')  # 选择6间

time.sleep(5)
# ② 通过option标签的value属性值进行选择:Select(下拉框控件定位).select_by_value(option标签的value属性值)
Select(s).select_by_value("5")

time.sleep(5)
# ③ 通过选项下标(所有选项当成一个列表，从0开始)进行选择，Select(下拉框控件定位).select_by_index(选项下标)
Select(s).select_by_index(7)
time.sleep(5)

driver.quit()
