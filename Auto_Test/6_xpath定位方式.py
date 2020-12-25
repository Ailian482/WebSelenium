from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('https://www.baidu.com')
# 最大化窗口，如果不最大化窗口，页面有些控件显示不全，做自动化的时候可能定位不到控件
driver.maximize_window()
time.sleep(3)
# demo2
# driver = webdriver.Firefox()
#
# driver.get('https://www.baidu.com')
# time.sleep(5)

# 六、使用xpath定位控件
# 1、使用xpath绝对路径来定位控件
# 语法是从根节点开始的，单斜杠开头，一层一层往下写，层与层通过单斜杠/去分割：
# /html/body或者head/div/...

# 1. 定位百度首页的‘新闻’按钮，并且点击它
driver.find_element_by_xpath('/html/body/div/div/div[3]/a[1]').click()
time.sleep(2)
# 2. 定位百度首页的‘更多’按钮，并点击它
driver.find_element_by_xpath('/html/body/div/div/div[3]/div/a').click()
time.sleep(2)
# 3. 定位百度的搜索框，并输入‘哈哈哈哈哈’
driver.find_element_by_xpath('/html/body/div/div/div/div/div/form/span[1]/input').send_keys('哈哈哈哈哈')
time.sleep(2)



# 2、使用xpath相对路径来定位控件，在谷歌浏览器验证路径唯一才写到代码里面
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

# 1. 通过祖父级定位百度首页的'设置'按钮，并点击它
driver.find_element_by_xpath('//div[@id="head"]/div/span').click()
# 2. 通过父级定位百度首页的'登录'按钮，并点击它
driver.find_element_by_xpath('//div[@id="u1"]/a').click()
# 3. 通过元素本身属性定位百度首页的“二维码”图标，并点击它
driver.find_element_by_xpath('//img[@class="icon"]').click()
# 4. 通过元素本身两种属性同时成立去定位百度首页的'设为首页'按钮，并点击它
driver.find_element_by_xpath('//a[@class="c-color-gray2" and @href="//www.baidu.com/cache/setindex/index.html"]').click()
# 5. 利用contains定位百度首页的“百度一下”按钮，并点击它
driver.find_element_by_xpath('//input[contains(@value,"度一")]').click()
# 6. 通过父级定位，拿同级a标签的第5条，百度首页的'贴吧'按钮，并点击它
driver.find_element_by_xpath('//div[@id="s-top-left"]/a[5]').click()
# 7. 通过祖父级定位百度首页的'设为首页'按钮，并点击它
driver.find_element_by_xpath('//div[@class="s-bottom-layer-left"]/p[1]/a[@class="c-color-gray2"]').click()
# 8. 通过父级定位百度首页的'设为首页'按钮，并点击它
driver.find_element_by_xpath('//p[@class="lh"][1]/a').click()
# 9. 通过父级定位百度首页的'有奖调研'按钮，并点击它
driver.find_element_by_xpath('//p[@class="lh activity"]/a').click()
# 10. 通过祖父级定位百度首页的‘京公网安备11000002000001号’按钮，并点击它
driver.find_element_by_xpath('//div[@id="s-bottom-layer-right"]/a/span')
# 11. 通过祖父的父级来定位百度首页的“百度热榜”按钮，并点击它
driver.find_element_by_xpath("//div[@id='s-hotsearch-wrapper']/div/a/div").click()
# 12. 用contains定位元素文本包含“素媛”的百度首页的第4条热搜链接
# driver.find_element_by_xpath('//ul[@id="hotsearch-content-wrapper"]/li/a/span[contains(text(),"素媛")]').click()
# # 13. 用contains定位元素文本包含“热榜”的百度首页的“百度热榜”按钮
# driver.find_element_by_xpath('//a[@class="hot-title"]/div[contains(text(),"热榜")]')
