from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://101.133.169.100/yuns/index.php')
# 最大化窗口，如果不最大化窗口，页面有些控件显示不全，做自动化的时候可能定位不到控件

# 8. 获取控件的尺寸，用size方法，这是一个属性方法，类似于属性，调用的时候不需要加括号，动作方法例如click()要加括号
# 返回的是字典
# ① 获取输入框的尺寸
size = driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').size
print(type(size))
print(size)
print(size['height'])
# ② 获取搜索按钮的尺寸
size = driver.find_element_by_xpath('//div[@class="schbox"]/form/input[2]').size
print(size)
print(size['width'])

# 9. 获取控件上面的文本信息，text方法
# 获取“联系客服”控件的文本“联系客服”
text = driver.find_element_by_css_selector('.contact_help>dl:first-child>dd:nth-last-child(2)').text
print(text)

# 10. 获取控件的属性值，get_attribute('属性名')
# 获取9.9抢大牌控件的 href 属性的属性值
attribute = driver.find_element_by_css_selector('div.schhot>a').get_attribute('href')
print(attribute)

# 11. 判断控件是否在页面是显示出来了，is_displayed()方法，返回的是布尔类型值，先要定位控件
# 判断输入框是否已经加载出来了
dis = driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').is_displayed()
print(dis)

if dis == True:
    driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').send_keys('女装')
    # value 属性的属性值是输入信息后页面的 回显值
    at = driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').get_attribute('value')
    print(at)
else:
    # 如果页面元素没有加载出来，就设置一个休眠时间，8秒
    time.sleep(8)
    driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').send_keys('女装')
driver.quit()