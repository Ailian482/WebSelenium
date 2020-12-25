from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
# 最大化窗口，如果不最大化窗口，页面有些控件显示不全，做自动化的时候可能定位不到控件
driver.maximize_window()
time.sleep(3)

# driver = webdriver.Firefox()
#
# driver.get('https://www.baidu.com')
# time.sleep(5)




# 1、使用css_selector绝对路径来定位元素
# 和xpath绝对路径一样也是一层一层往下写的，但是语法有区别，由html开头，层与层通过空格或者大于号>来分割：
# html>head或者body>div>...   推荐使用大于号>分割
# html head或者body div ...   使用空格分割可能会出现跳级寻找，不建议使用

# 1. 定位百度首页的‘视频’按钮，并点击它
driver.find_element_by_css_selector('html>body>div>div>div:nth-child(3)>a:nth-child(4)').click()
# 2. 定位百度首页的第一条热搜连接，并点击它
driver.find_element_by_css_selector('html>body>div>div>div>div>div>div>ul>li:nth-child(1)>a>span:nth-child(2)').click()
# 3. 定位百度首页的搜索框右侧的 图标 按钮，并点击它
driver.find_element_by_css_selector('html>body>div>div>div>div>div>form>span:nth-child(8)>span:nth-child(1)').click()

# 2、使用css_selector相对路径来定位控件，在谷歌浏览器验证路径唯一才写到代码里面
# 语法是标签名开头的：
# ① 如果要定位的元素本身没有特殊属性，则从父级逐层网上找有特殊属性的元素去定位：
# 中间某个有特殊属性元素的标签名[属性名="属性值"]>...>要定位元素的标签名
# ② 如果其本身就有特殊属性，则可以通过其自身去定位
# 标签名[属性名="属性值"]
# ③ 如果一种属性不能使定位唯一，那么可以通过多种属性用中括号[]隔开写，使其定位唯一化
# 要定位元素的标签名[属性名1="属性值1"][属性名2="属性值2"][属性名3="属性值3"]...
# ④ id、class属性有特殊写法：
# 标签名[id="id值"] ---> 写成：标签名#id值  （标签名可以省略不写）
# 标签名[class="class值"] ---> 写成：标签名.class值  （标签名可以省略不写）
# ⑤ 拿同级标签的第n条，从1开始
# 父级标签名[属性名="属性值"]>要定位元素标签名:nth-child(n)
# ⑥ 拿同级标签的第1条
# 父级标签名[属性名="属性值"]>要定位元素标签名:first-child(n)
# ⑦ 拿同级标签的最后一条
# 父级标签名[属性名="属性值"]>要定位元素标签名:last-child(n)
# ⑧ 拿同级标签的倒数第n条
# 父级标签名[属性名="属性值"]>要定位元素标签名:nth-last-child(n)
# 注意：find_element_by_css_selector同级不同标签名是一起排序的

# 1. 通过祖父级特殊属性定位百度"设置"按钮，并点击它
driver.find_element_by_css_selector('div[id="head"]>div>span').click()
# 2. 通过父级特殊属性定位百度"设置"按钮，并点击它
driver.find_element_by_css_selector('div[id="u1"]>span').click()
# 3. 通过自身特殊属性定位百度搜索框，并输入"竹"
driver.find_element_by_css_selector('input[id="kw"]').send_keys('竹')
time.sleep(2)
# 4. 通过元素本身两种属性同时成立定位百度搜索框，并输入"子"
driver.find_element_by_css_selector('input[id="kw"][name="wd"]').send_keys('子')
time.sleep(2)
# 5. 通过id特殊写法定位百度搜索框，并输入"林"
driver.find_element_by_css_selector('input#kw').send_keys('林')
time.sleep(2)
# 6. 通过class特殊写法定位百度搜索框，并输入"1"
driver.find_element_by_css_selector('input.s_ipt').send_keys('1')
time.sleep(2)
# 7. 通过nth-child()拿同级标签的第2条，百度首页的“hao123”按钮，并点击它
driver.find_element_by_css_selector('div#s-top-left>a:nth-child(2)').click()
time.sleep(2)
# 8. 通过nth-child()拿同级标签的第6条，百度首页的“更多”按钮，并点击它
driver.find_element_by_css_selector('div#s-top-left>div:nth-child(7)').click()
time.sleep(2)
# 9. 通过nth-child()拿同级标签的第1条，百度首页的“新闻”按钮，并点击它
driver.find_element_by_css_selector('div#s-top-left>a:nth-child(1)').click()
time.sleep(2)
# 10. 用first-child拿同级标签的第1条，百度首页的“新闻”按钮，并点击它
driver.find_element_by_css_selector('div#s-top-left>a:first-child').click()
time.sleep(2)
# 11. 用last-child拿同级标签的最后一条，百度首页的“更多”按钮，并点击它
driver.find_element_by_css_selector('div#s-top-left>div:last-child').click()
time.sleep(2)
# 12. 用nth-last-child()拿同级标签的倒数第2条，百度首页的“学术”按钮，并点击它
driver.find_element_by_css_selector('div#s-top-left>a:nth-last-child(2)').click()
time.sleep(2)
# 13. 定位百度首页的“帮助中心“按钮，并点击它
driver.find_element_by_css_selector('div#bottom_layer>div>p:last-child>a').click()
time.sleep(2)
# 14. 定位百度首页的”登录“按钮，并点击它
driver.find_element_by_css_selector('div#u1>a').click()
time.sleep(2)
# 15. 定位百度首页的“百度热榜”按钮，并点击它
driver.find_element_by_css_selector('a.hot-title>div').click()
time.sleep(2)


driver.find_element_by_css_selector('input.but1').click()

# driver.find_element_by_css_selector('input#kw').send_keys('林')