# -*- coding:UTF8- -*-

from selenium import webdriver
import time

driver = webdriver.Chrome()
# 打开浏览器，并进入中国铁路12306官网
# driver.get("https://www.12306.cn/index/")  # 这个网址没有实现，滚动条滚到底部
driver.get('http://101.133.169.100/yuns/index.php')  # 云商系统
# driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')  # 携程旅行
time.sleep(5)  # 休眠3秒
# driver.maximize_window()  # 窗口最大化
time.sleep(5)  # 休眠5秒

# 如何处理滚动条？
# 通过调用js方法去实现
# ① 把滚动条滚动到底部，设置一个超过屏幕分辨率的很大的值
js = "var q=document.documentElement.scrollTop=10000"  # var q 就是定义一个变量q
driver.execute_script(js)  # execute_script()方法实现js
time.sleep(3)
# ② 把滚动条滚动到最顶部，设置值为0
js = "var q=document.documentElement.scrollTop=0"
driver.execute_script(js)
time.sleep(3)

# ③ 滚动到body体高度的50%，(x, y)，分别表示左右位移和上下位移，body表示html的body体的高度
driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.5)")
time.sleep(3)

# ④ 滚动到body体宽度的50%，(x, y)，分别表示左右位移和上下位移，body表示html的body体的高度
driver.execute_script("window.scrollTo(document.body.scrollWidth*0.5, 0)")
time.sleep(3)

# ⑤ 相对当前滚动条坐标，滚动滚动条到某个坐标位置(x, y)，x和y都可以为负数，为整数表示向右、向下滚动，为负数表示向左、向上滚动
driver.execute_script("window.scrollBy(0, 100)")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 100)")
time.sleep(3)

# ⑥ 滚动到绝对坐标，不管滚动条在何处，都会移动到相应的坐标处
driver.execute_script("window.scrollTo(0, 100)")
time.sleep(3)
# 定位"秒杀"，并点击它
text = driver.find_element_by_link_text("秒杀").click()

driver.quit()

