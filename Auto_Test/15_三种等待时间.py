from selenium import webdriver
import time

# 显式等待时间需要导入的三行模块/类
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('http://101.133.169.100/yuns/index.php')

# 等待时间，意义在于给程序一个响应的时间，加载内容，然后再进行下一步操作
# 适合添加等待时间的场景：① 打开项目，需要时间去渲染和加载页面中的所有数据，② 页面跳转情况下

# 做UI自动化，不是去发现性能问题，主要是保证老功能的回归更加健壮，更加好的保证老功能没有受新功能的影响。
# 加载慢一般是后端性能问题

# 22. 强制等待时间，先要导入time模块，time.sleep(等待时间)方法，等待过程中，程序不动，过完等待时间才进行操作
time.sleep(3)

# 23. 隐式等待时间，implicitly_wait(等待时间)，是最大等待时间，下面要定位的控件加载出来了，就会直接往下操作，超时未加载出来就报错。
# 比如说等待时间设置的是10秒，但是要定位的控件3秒就加载出来了，那么3秒后程序就会继续往下走
# 要注意的问题：
# 在第一个页面点击某个控件，跳转到下一个页面，如果要用xpath方式定位第二个页面的控件，
# 但是点后击控件加载比较慢，第一个页面刚好有和第二个页面要定位的控件的xpath一样，
# 那么用implicitly_wait方法，就有可能定位到的是第一个页面的xpath，然后程序继续往下走，就会导致报错
# 遇到上面这种情况，第一个页面和第二个页面有相同的定位方式，用强制等待时间。
driver.implicitly_wait(10)
# 下面这个控件加载出来了，程序就继续往下走
driver.find_element_by_xpath('//div[@class="schbox"]/form/input[1]').send_keys('女装')
time.sleep(2)
# 24. 显式等待时间，要导入WebDriverWait类
# 最大等待15秒，每隔0.5秒检测是否出现下面xpath的控件，出现了就会返回定位到的控件，可以用一个变量去接
# By. 后面跟的是八大定位方式
# ① until，
ele = WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located(
    (By.XPATH,"//div[@class='schbox']/form/input[1]")))
ele.send_keys('冬装')
time.sleep(3)

# 最大等待15秒，每隔0.5秒检测是否不存在下面xpath的控件，
# ② until_not，跳转后，上一个页面的控件不存在，这种方法不精确
# ele = WebDriverWait(driver,15,0.5).until_not(EC.presence_of_element_located(
#     (By.XPATH,"//div[@class='schbox']/form/input[1]")))

driver.quit()