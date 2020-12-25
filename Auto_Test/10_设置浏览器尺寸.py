from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://101.133.169.100/yuns/index.php')
# 最大化窗口，如果不最大化窗口，页面有些控件显示不全，做自动化的时候可能定位不到控件

# 3. 设置浏览器尺寸
# ① 浏览器最大化
driver.maximize_window()
time.sleep(2)
# ② 设置浏览器宽高，参数分别为：(宽,高)
driver.set_window_size(1200,800)
time.sleep(2)
driver.quit()