from selenium import webdriver
import unittest
import os
import time
from Uiframe0test.public.login import Mylogin

"""
selenium 自动化测试框架的目录结构：
    case层：放的是自动化测试用例（app、web），
           一个.py文件就是一个项目的模块（可以细分），尽量让.py文件的行数不要太多，
           .py文件里面的一个test开头的方法对应一个自动化测试用例(手工测试用例)
    public层：放的是公用业务（常用的）模块的API
    report层：报告输出，呈现自动化执行结果是通过还是不通过
    Ven层：
    testrunner.py：批量运行所有case的（比如说有100个case，可以把100个case全部运行完）
"""
"""
unittest单元测试框架，一般包含但部分：
    ① setUp(初始化)，
    ② 以test开头的方法(其实就是用例)，
    ③ tearDown(清理、释放)
运行程序的时候，是按照上面的①②③的顺序来执行，即每执行一条测试用例，都会先打开浏览器，执行用例，然后关闭浏览器
"""
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

    def testShouye01_01(self):
        '''测试首页导航文案显示是否正常'''
        Mylogin(self.driver).login()
        # 定位控件
        firstPageNavi = self.driver.find_element_by_xpath("//div[@class='top']/span")
        loginText = self.driver.find_element_by_css_selector("div.login>a:nth-child(1)")
        regisText = self.driver.find_element_by_css_selector("div.login>a:nth-child(3)")

        # 断言 实际结果与预期结果是否一致 (预期结果, 实际结果)，这两个结果位置可以调换
        self.assertEqual("亲，欢迎您来到云商系统商城！", firstPageNavi.text)  # 断言控件文本内容是否与预期一致
        self.assertEqual("17731990979", loginText.text)  # 断言控件文本内容是否与预期一致
        self.assertEqual("退出", regisText.text)  # 断言控件文本内容是否与预期一致
        self.assertNotEqual("dd", regisText.text)  # 断言控件文本内容是否与预期不同

        # 断言实际结果是否包含了某个文本，(文本, 实际结果)
        self.assertIn("云商系统商城", firstPageNavi.text)

        # 断言实际结果为真
        self.assertTrue(self.driver.find_element_by_xpath("//div[@class='top']/span").is_displayed())
        self.assertFalse(firstPageNavi.is_displayed())  # 断言实际结果为假

        # 老师自创断言方法
        if loginText.text == "177****0979":
            print("等于")
        else:
            print("不等于")
            self.driver.find_element_by_xpath("王麻子")



    def testShouye01_02(self):
        '''验证搜索内容无时，提示语是否正常'''
        Mylogin(self.driver).login()
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys("王麻子")
        self.driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[2]").click()
        time.sleep(2)
        searchText = self.driver.find_element_by_xpath("//div[@class='nomsg']")
        self.assertEqual(searchText.text, "抱歉，没有找到相关的商品")



if __name__ == "__main__":
    unittest.main()