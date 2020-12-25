from selenium import webdriver
import unittest
import os
import time
# from Uiframe0test.public.login import Mylogin
# from Uiframe0test.public.pagenew import NewPage
# from Uiframe0test.public.xuanting import MoveTo
from Uiframe0test.public.proinfo import ProInfo

class TestShouye(unittest.TestCase):
    # 我们自己定义的TestShouye类，继承了unittest的TestCase类，TestCase类里面的方法，TestShouye类都可以用
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        # self是类的一个实例化对象，self.driver相当于一个类的初始化变量，可以被这个类的其他方法所认识使用
        # 如果没有加self，只是driver变量，那么就是方法里面的一个局部变量，其他方法是不能认识和使用的
        self.driver.get('http://101.133.169.100/yuns/index.php/')  # 进入项目
        self.driver.maximize_window()  # 窗口最大化
        time.sleep(5)  # 休眠5秒钟
        # 打印开始时间：年-月-日 时:分:秒。strftime是格式化时间(大小写要求)，time.localtime(time.time())拿到当前的时间
        print("stratTimes:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))

    def tearDown(self) -> None:
        filedir = "E:test/screenshot/"  # 电脑的一个路径
        if not os.path.exists(filedir):  # 如果电脑没有上面的路径，就会在电脑上创建这个路径
            os.makedirs(os.path.join('E:/', 'test', 'screenshot'))
        # 打印执行完成的时间，如果用例执行失败了，可以通过这个时间找到截图
        print("endTimes:" + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
        # 定义一个文件路径及其名称，screen_name = E:test/screenshot/2020-12-18.png
        screen_name = filedir + time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())) + ".png"
        # 执行完后截图：路径/名称，拿到最后截图可以看图查错
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()  # 关闭浏览器

    def testShouye01_13(self):
        '''验证商品详情的数量框处是否能输入数字'''
        # 调用proinfo模块的商品详情方法
        ProInfo(self.driver).proinfo1("xpath", "//div[@class='detail'][1]/div/div/dl[4]/dd[1]/a")
        input_num = self.driver.find_element_by_id("buy_num")  # 定位输入框
        input_num.click()  # 点击输入框
        input_num.clear()  # 清空默认值
        a = "12"
        input_num.send_keys(a)  # 重新输入值
        new_num = self.driver.find_element_by_id("buy_num").get_attribute("value")
        # print(new_num)
        # 断言
        self.assertEqual(a, new_num)

    def testShouye01_14(self):
        '''验证点击商品详情页的“+”数量是否正常增加1'''
        # 调用proinfo模块的商品详情方法
        ProInfo(self.driver).proinfo()
        # 获取数量的初始值
        old_num = self.driver.find_element_by_id("buy_num").get_attribute("value")
        print(old_num)
        # 点击“+”
        self.driver.find_element_by_id("num_plus").click()
        time.sleep(1)
        # 获取最新的数量
        new_num = self.driver.find_element_by_id("buy_num").get_attribute("value")
        print(new_num)

        self.assertEqual(int(old_num) + 1, int(new_num))

    def testShouye01_15(self):
        '''当数量为最大添加量时，点击“+”是否有相关提示'''
        # 调用proinfo模块的商品详情方法
        ProInfo(self.driver).proinfo()
        input_num = self.driver.find_element_by_id("buy_num")  # 定位输入框
        input_num.click()  # 点击输入框
        input_num.clear()  # 清空默认值
        input_num.send_keys("9940")  # 输入最大值9940
        # 点击“+”
        self.driver.find_element_by_id("num_plus").click()
        time.sleep(2)
        # 弹出alert框，获取alert框的文本信息
        a_text = self.driver.switch_to.alert.text
        # 点击alert框的确定按钮
        self.driver.switch_to.alert.accept()
        # 断言  ??? 如何断言alert弹框消失了
        self.assertEqual("库存不足", a_text)

    def testShouye01_16(self):
        '''点击“-”数量是否正常减少1'''
        # 调用调用proinfo模块的商品详情方法
        ProInfo(self.driver).proinfo()
        # 在输入框中输入一个大于1的数字
        input_num = self.driver.find_element_by_id("buy_num")
        input_num.click()
        input_num.clear()
        input_num.send_keys("16")  # 输入16
        # 获取输入后的数值
        old_num = self.driver.find_element_by_id("buy_num").get_attribute("value")
        # 点击“-”
        self.driver.find_element_by_id("num_minus").click()
        # 获取点击后的数值
        new_num = self.driver.find_element_by_id("buy_num").get_attribute("value")
        # 断言
        self.assertEqual(int(old_num) - 1, int(new_num))

    def testShouye01_17(self):
        '''当数量为1时，点击“-”是否有相关提示'''
        # 调用proinfo模块的商品详情方法
        ProInfo(self.driver).proinfo()
        # 在数量输入框中输入1
        input_num = self.driver.find_element_by_id("buy_num")
        input_num.click()
        input_num.clear()
        input_num.send_keys("1")
        # 获取输入后的数值
        num = self.driver.find_element_by_id("buy_num").get_attribute("value")
        # 点击“-”
        self.driver.find_element_by_id("num_minus").click()
        time.sleep(2)
        # 弹出alert框，获取alert框的文本信息
        text = self.driver.switch_to.alert.text
        # 点击alert框的确定按钮
        self.driver.switch_to.alert.accept()
        # 断言
        self.assertEqual("最少为一个数量", text)

    def testShouye01_18(self):
        '''验证不选择商品规格，点击添加购物车是否有相应提示'''
        # 调用proinfo模块的商品详情方法
        ProInfo(self.driver).proinfo()
        # 获取购物车的数量
        old_num = self.driver.find_element_by_id("cart_num").text
        # 添加商品数量
        input_num = self.driver.find_element_by_id("buy_num")
        input_num.click()
        input_num.clear()
        input_num.send_keys("1")
        # 点击添加购物车
        self.driver.find_element_by_xpath("//div[@class='Gcart']/a[1]").click()
        time.sleep(2)
        # 获取提示文本
        tswb = self.driver.find_element_by_xpath("//div[@class='info']/div[3]/div[1]").text
        # tswb = self.driver.find_element_by_css_selector("sku_error").text  # 这个用css定位不到
        new_num = self.driver.find_element_by_id("cart_num").text  # 获取购物车数量
        # 断言
        self.assertEqual("没有选择产品规格", tswb)
        self.assertEqual(old_num, new_num)

    def testShouye01_19(self):
        '''验证不选择商品规格，点击添加购物车是否有相应提示'''
        # 调用proinfo模块的商品详情方法
        ProInfo(self.driver).proinfo()
        old_num = self.driver.find_element_by_id("cart_num").text  # 获取购物车的数量
        # 添加商品数量
        input_num = self.driver.find_element_by_id("buy_num")
        input_num.click()
        input_num.clear()
        input_num.send_keys("1")
        # 商品有两种属性规格，选择第一种属性规格
        self.driver.find_element_by_xpath("//div[@class='sku_box']/dl[1]/dd/a/em").click()
        # 点击添加购物车
        self.driver.find_element_by_xpath("//div[@class='Gcart']/a[1]").click()
        time.sleep(2)
        # 获取提示文本
        tswb = self.driver.find_element_by_xpath("//div[@class='info']/div[3]/div[1]").text
        new_num = self.driver.find_element_by_id("cart_num").text  # 获取购物车数量
        # 断言
        self.assertEqual("没有选择产品规格", tswb)
        self.assertEqual(old_num, new_num)

    def testShouye01_20(self):
        '''验证选择商品规格，点击添加购物车是否能正常添加'''
        # 调用proinfo模块的商品详情方法
        ProInfo(self.driver).proinfo()
        # 获取购物车的数量
        old_num = self.driver.find_element_by_id("cart_num").text
        # 添加商品数量
        input_num = self.driver.find_element_by_id("buy_num")
        input_num.click()
        input_num.clear()
        a = 1
        input_num.send_keys(a)
        # 商品有两种属性规格，选择所有属性规格
        self.driver.find_element_by_xpath("//div[@class='sku_box']/dl[1]/dd/a/em").click()
        self.driver.find_element_by_xpath("//div[@class='sku_box']/dl[2]/dd/a/em").click()
        # 点击添加购物车
        self.driver.find_element_by_xpath("//div[@class='Gcart']/a[1]").click()
        time.sleep(2)
        # 获取提示文本
        tswb1 = self.driver.find_element_by_xpath("//div[@class='buy_tip_name']/p").text
        tswb2 = self.driver.find_element_by_xpath("//div[@class='buy_tip_action']/a[1]").text
        tswb3 = self.driver.find_element_by_xpath("//div[@class='buy_tip_action']/a[2]").text
        # 获取购物车数量
        new_num = self.driver.find_element_by_id("cart_num").text
        # 断言
        self.assertEqual("宝贝已成功添加到购物车", tswb1)
        self.assertEqual("去付款", tswb2)
        self.assertEqual("继续购物", tswb3)
        self.assertEqual(int(old_num) + a, int(new_num))

if __name__ == "__main__":
    unittest.main()