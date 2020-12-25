from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://101.133.169.100/yuns/index.php')
# 最大化窗口，如果不最大化窗口，页面有些控件显示不全，做自动化的时候可能定位不到控件
driver.maximize_window()
time.sleep(3)

# driver = webdriver.Firefox()
#
# driver.get('https://www.baidu.com')
# time.sleep(5)

# 六、使用xpath定位控件
# 1、使用xpath绝对路径来定位控件
# 语法是从根节点开始的，单斜杠开头，一层一层往下写，层与层通过单斜杠/去分割：
# /html/body或者head/div/...

# 1. 定位云商的搜索框，并输入“女装”
driver.find_element_by_xpath('/html/body/div/div/div/div/form/input[1]').send_keys('女装')
# 2. 定位云商的搜索按钮，并点击它
driver.find_element_by_xpath('/html/body/div/div/div/div/form/input[2]').click()
# 3. 定位云商的9.9抢大牌按钮，并点击它
driver.find_element_by_xpath('/html/body/div[2]/div/div/div/a[1]').click()
time.sleep(2)
driver.quit()
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
# 注意：xpath同级元素不同标签名是分开排序的

# 1. 通过祖父级定位云商的搜索框，并输入“男装”
driver.find_element_by_xpath('//div[@class="schbox"]/form/input').send_keys('男装')
# 2. 通过自身特殊属性定位云商的搜索框，并清空内容
driver.find_element_by_xpath('//input[@name="key"]').clear()
time.sleep(2)
# 3. 通过两种属性定位云商的搜索框，并输入“冬装”
driver.find_element_by_xpath('//input[@name="key" and @class="but1"]').send_keys('冬装')
# 4. 拿同级同名标签的第2条，定位搜索按钮，并点击它
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[2]').click()
time.sleep(2)
# 5. 利用contains通过控件部分连续的文本定位“夏天最热”按钮，并点击它
driver.find_element_by_xpath('//div[@class="nav_pub"]/a[contains(@title,"天最")]').click()
time.sleep(2)
# 6. 定位云商的搜索栏下面的“首页”按钮，并点击它
driver.find_element_by_xpath('//div[@class="nav_pub"]/a[1]').click()
time.sleep(2)
# 7. 定位云商的秒杀按钮，并点击它
driver.find_element_by_xpath('//div[@class="nav_pub"]/a[2]')
# demo1

# ⑥ 标签省略不写，表示无论什么样的标签，只要class属性是属性值就行，属性要唯一
# //*[@属性名="属性值"]
driver.find_element_by_xpath('//*[@class="but2"]').click()