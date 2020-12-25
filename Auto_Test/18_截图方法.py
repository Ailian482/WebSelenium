from selenium import webdriver
import time
driver = webdriver.Chrome()

# 打开百度
driver.get('https://www.baidu.com')
driver.maximize_window()
time.sleep(3)
# 截图get_screenshot_as_file('保存路径/图片名称')，
# 注意：保存路径一定要是电脑存在的路径,文件名一定要以".png"结尾如果有同名文件，会被覆盖
driver.get_screenshot_as_file('E:/test/screentshot1/test.png')
driver.quit()