from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://101.133.169.100/yuns/index.php')
# 最大化窗口，如果不最大化窗口，页面有些控件显示不全，做自动化的时候可能定位不到控件
driver.maximize_window()
time.sleep(3)

# 1. 获取当前页面的title
# 自动化只能定位Web页面地址栏下面的内容，也就是HTML的body体里面的内容
# title是在HTML的head体里面
title1 = driver.title
print(title1)
# ① 定位搜索框，输入“女装”
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').send_keys('女装')
time.sleep(2)
# ② 点击搜索按钮
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[2]').click()
# ③ 获取点击搜索后的title信息
title2 = driver.title
print(title2)

# 2. 获取当前页面的url
url = driver.current_url
print(url)

# 3. 设置浏览器尺寸
# ① 浏览器最大化
driver.maximize_window()
time.sleep(2)
# ② 设置浏览器宽高，参数分别为：(宽,高)
driver.set_window_size(1200,800)
time.sleep(2)
