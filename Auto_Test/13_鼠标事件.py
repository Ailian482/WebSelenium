# 首先要导入鼠标事件的类
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
import time
driver = webdriver.Chrome()

driver.get('http://101.133.169.100/yuns/index.php')
# 最大化窗口，如果不最大化窗口，页面有些控件显示不全，做自动化的时候可能定位不到控件


# 12. 模拟鼠标放到控件上，move_to_element(控件的定位)，perform()实现事件
# 页面中可能会有多级菜单，比如要把鼠标放到一级菜单上面，二级菜单才会显示出来
# 把鼠标挪到“母婴玩具”控件上
# ① 先定位到“母婴玩具”控件
ele = driver.find_element_by_link_text('母婴玩具')
# time.sleep(2)
# ② 把鼠标挪到“母婴玩具”上，perform()方法实现
ActionChains(driver).move_to_element(ele).perform()
time.sleep(2)
# ③ 点击“母婴玩具”菜单下的“喂养用品”
driver.find_element_by_link_text('喂养用品').click()
time.sleep(2)

# 13. 右击某个控件，context_click()
# ① 先定位到“母婴玩具”控件
ele = driver.find_element_by_link_text('母婴玩具')
# ② 把鼠标挪到“母婴玩具”上，perform()方法实现
ActionChains(driver).move_to_element(ele).perform()
time.sleep(2)
# ③ 右击“母婴玩具”
ActionChains(driver).context_click(ele).perform()

# 14. 双击某个控件，double_click()
# ① 先定位到“母婴玩具”控件
ele = driver.find_element_by_link_text('母婴玩具')
# ② 把鼠标挪到“母婴玩具”上，perform()方法实现
ActionChains(driver).move_to_element(ele).perform()
time.sleep(2)
# ③ 双击“母婴玩具”
ActionChains(driver).double_click(ele).perform()

# 15. 拖曳控件，drag_and_drop(原控件,目标控件)
# ① 定位原控件
source = driver.find_element_by_link_text('秒杀')
time.sleep(2)
# ② 定位目标控件
target = driver.find_element_by_link_text('品牌街')
# ③ 把原控件拖到目标控件处
ActionChains(driver).drag_and_drop(source,target).perform()

# 16. 还有一种偏移方法drag_and_drop_by_offset(原控件,x方向偏移值,y方向偏移值)
ActionChains(driver).drag_and_drop_by_offset(source,100,0)

driver.quit()