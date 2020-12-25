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

# 一、通过id、name、class_name、link_text、partial_link_text、tag_name定位元素
# # 1. 通过id属性定位百度首页的“换一换”，并点击它
# driver.find_element_by_id('hotsearch-refresh-btn').click()
# time.sleep(2)
# # 2. 用过id属性定位百度“搜索”按钮，并点击搜索
# driver.find_element_by_id('su').click()
# time.sleep(2)
# # 3. 通过id属性定位百度搜索框元素，并输入'哈哈'
# driver.find_element_by_id('kw').send_keys('哈哈')
# time.sleep(2)
# # 4. 通过name属性定位百度的搜索框元素，并输入'哈哈'
# driver.find_element_by_name('wd').send_keys('哈哈')
# time.sleep(2)
# # 5. 通过name属性定位百度首页的“更多”按钮，并且点击它
# driver.find_element_by_name('tj_briicon').click()
# time.sleep(2)
# # 6. 通过class属性定位百度搜索框元素，并输入'哈哈'
# driver.find_element_by_class_name('s_ipt').send_keys('哈哈')
# time.sleep(2)
# # 7. 通过class属性定位百度首页的“换一换”按钮，并点击它
# driver.find_element_by_class_name('hot-refresh-text').click()
# time.sleep(2)
# # 8. 通过全文本定位百度首页的“hao123”按钮，并且点击它
# driver.find_element_by_link_text('hao123').click()
# time.sleep(2)
# # 9. 通过全文本定位百度首页的“地图”按钮，并且点击它
# driver.find_element_by_link_text('地图').click()
# time.sleep(2)
# # 10. 通过部分文本定位百度首页的“百度营销”按钮，并且点击它
# driver.find_element_by_partial_link_text('营销').click()
# # 11. 通过部分文本定位百度首页的“使用百度前必读”按钮，并且点击它
# driver.find_element_by_partial_link_text('使用百').click()
# # 12. 通过tag_name找百度首页的一组div标签类型，返回的结果会被存储在列表中，一般不用这种方法
# ele = driver.find_elements_by_tag_name('div')
# print(len(ele))


# 二、xpath和css_selector定位的同级元素排序区别：
# xpath同级元素不同标签名是分开排序的
# css_selector同级不同标签名是一起排序的

# 三、使用xpath绝对路径来定位控件
# 语法是从根节点开始的，单斜杠开头，一层一层往下写，层与层通过单斜杠/去分割：
# /html/body或者head/div/...

# # 1. 定位百度首页的‘新闻’按钮，并且点击它
# driver.find_element_by_xpath('/html/body/div/div/div[3]/a[1]').click()
# time.sleep(2)
# # 2. 定位百度首页的‘更多’按钮，并点击它
# driver.find_element_by_xpath('/html/body/div/div/div[3]/div/a').click()
# time.sleep(2)
# # 3. 定位百度的搜索框，并输入‘哈哈哈哈哈’
# driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/span[1]/input').send_keys('哈哈哈哈哈')
# time.sleep(2)


# 四、使用css_selector绝对路径来定位元素
# 和xpath绝对路径一样也是一层一层往下写的，但是语法有区别，由html开头，层与层通过空格或者大于号>来分割：
# html>head或者body>div>...   推荐使用大于号>分割
# html head或者body div ...   使用空格分割可能会出现跳级寻找，不建议使用

# # 1. 定位百度首页的‘视频’按钮，并点击它
# driver.find_element_by_css_selector('html>body>div>div>div:nth-child(3)>a:nth-child(4)').click()
# # 2. 定位百度首页的第一条热搜连接，并点击它
# driver.find_element_by_css_selector('html>body>div>div>div>div>div>div>ul>li:nth-child(1)>a>span:nth-child(2)').click()
# # 3. 定位百度首页的搜索框右侧的 图标 按钮，并点击它
# driver.find_element_by_css_selector('html>body>div>div>div>div>div>form>span:nth-child(8)>span:nth-child(1)').click()


# 五、使用xpath相对路径来定位控件，在谷歌浏览器验证路径唯一才写到代码里面
# 语法是双斜杠开头的：
# ① 如果要定位的元素本身没有特殊属性，则从父级逐层网上找有特殊属性的元素去定位：
# //中间某个有特殊属性元素的标签名[@属性名="属性值"]/.../要定位元素的标签名
# ② 如果其本身就有特殊属性，则可以通过其自身去定位
# //要定位元素的标签名[@属性名="属性值"]
# ③ 如果一种属性不能使定位唯一，那么可以通过多种属性用and连来，使其定位唯一化
# //要定位元素的标签名[@属性名1="属性值1" and @属性名2="属性值2" and @属性名3="属性值3"...]
# ④ 拿同级标签的第n条，从1开始
# //父级元素的标签名[@属性名="属性值"]/要定位元素的标签名[n]
# ⑤ contains的用法，拿部分连续的属性值片段
# //要定位元素的标签名[contains(@属性名,'部分连续的属性值片段')]

# # 1. 通过祖父级定位百度首页的'设置'按钮，并点击它
# driver.find_element_by_xpath('//div[@id="head"]/div/span').click()
# # 2. 通过父级定位百度首页的'登录'按钮，并点击它
# driver.find_element_by_xpath('//div[@id="u1"]/a').click()
# # 3. 通过元素本身属性定位百度首页的“二维码”图标，并点击它
# driver.find_element_by_xpath('//img[@class="icon"]').click()
# # 4. 通过元素本身两种属性同时成立去定位百度首页的'设为首页'按钮，并点击它
# driver.find_element_by_xpath('//a[@class="c-color-gray2" and @href="//www.baidu.com/cache/setindex/index.html"]').click()
# # 5. 利用contains定位百度首页的“百度一下”按钮，并点击它
# driver.find_element_by_xpath('//input[contains(@value,"度一")]').click()
# # 6. 通过父级定位，拿同级a标签的第5条，百度首页的'贴吧'按钮，并点击它
# driver.find_element_by_xpath('//div[@id="s-top-left"]/a[5]').click()
# # 7. 通过祖父级定位百度首页的'设为首页'按钮，并点击它
# driver.find_element_by_xpath('//div[@class="s-bottom-layer-left"]/p[1]/a[@class="c-color-gray2"]').click()
# # 8. 通过父级定位百度首页的'设为首页'按钮，并点击它
# driver.find_element_by_xpath('//p[@class="lh"][1]/a').click()
# # 9. 通过父级定位百度首页的'有奖调研'按钮，并点击它
# driver.find_element_by_xpath('//p[@class="lh activity"]/a').click()
# # 10. 通过祖父级定位百度首页的‘京公网安备11000002000001号’按钮，并点击它
# driver.find_element_by_xpath('//div[@id="s-bottom-layer-right"]/a/span')
# # 11. 通过祖父的父级来定位百度首页的“百度热榜”按钮，并点击它
# driver.find_element_by_xpath("//div[@id='s-hotsearch-wrapper']/div/a/div").click()
# # 12. 用contains定位元素文本包含“素媛”的百度首页的第4条热搜链接
# driver.find_element_by_xpath('//ul[@id="hotsearch-content-wrapper"]/li/a/span[contains(text(),"素媛")]').click()
# # 13. 用contains定位元素文本包含“热榜”的百度首页的“百度热榜”按钮
# driver.find_element_by_xpath('//a[@class="hot-title"]/div[contains(text(),"热榜")]')





# 六、使用css_selector相对路径来定位控件，在谷歌浏览器验证路径唯一才写到代码里面
# 语法是标签名开头的：
# ① 如果要定位的元素本身没有特殊属性，则从父级逐层网上找有特殊属性的元素去定位：
# 中间某个有特殊属性元素的标签名[属性名="属性值"]>...>要定位元素的标签名[同级标签名所在位置（该项试情况写）]
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

# # 1. 通过祖父级特殊属性定位百度"设置"按钮，并点击它
# driver.find_element_by_css_selector('div[id="head"]>div>span').click()
# # 2. 通过父级特殊属性定位百度"设置"按钮，并点击它
# driver.find_element_by_css_selector('div[id="u1"]>span').click()
# # 3. 通过自身特殊属性定位百度搜索框，并输入"竹"
# driver.find_element_by_css_selector('input[id="kw"]').send_keys('竹')
# time.sleep(2)
# # 4. 通过元素本身两种属性同时成立定位百度搜索框，并输入"子"
# driver.find_element_by_css_selector('input[id="kw"][name="wd"]').send_keys('子')
# time.sleep(2)
# # 5. 通过id特殊写法定位百度搜索框，并输入"林"
# driver.find_element_by_css_selector('input#kw').send_keys('林')
# time.sleep(2)
# # 6. 通过class特殊写法定位百度搜索框，并输入"1"
# driver.find_element_by_css_selector('input.s_ipt').send_keys('1')
# time.sleep(2)
# # 7. 通过nth-child()拿同级标签的第2条，百度首页的“hao123”按钮，并点击它
# driver.find_element_by_css_selector('div#s-top-left>a:nth-child(2)').click()
# # 8. 通过nth-child()拿同级标签的第6条，百度首页的“更多”按钮，并点击它
# driver.find_element_by_css_selector('div#s-top-left>div:nth-child(7)').click()
# # 9. 通过nth-child()拿同级标签的第1条，百度首页的“新闻”按钮，并点击它
# driver.find_element_by_css_selector('div#s-top-left>a:nth-child(1)').click()
# # 10. 用first-child拿同级标签的第1条，百度首页的“新闻”按钮，并点击它
# driver.find_element_by_css_selector('div#s-top-left>a:first-child').click()
# # 11. 用last-child拿同级标签的最后一条，百度首页的“更多”按钮，并点击它
# driver.find_element_by_css_selector('div#s-top-left>div:last-child').click()
# # 12. 用nth-last-child()拿同级标签的倒数第2条，百度首页的“学术”按钮，并点击它
# driver.find_element_by_css_selector('div#s-top-left>a:nth-last-child(2)').click()


