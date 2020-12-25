from appium import webdriver
import os
import time
import unittest
from Uiframe0test.public.Applogin import AppLogin


class AndroidLogout(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1'
        desired_caps['deviceName'] = 'Android EMulator'
        desired_caps['noRest'] = 'True'
        desired_caps['appPackage'] = 'cn.xiaochuankeji.tieba'
        desired_caps['appActivity'] = '.ui.base.SplashActivity'

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        print("starTime:" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))

    def tearDown(self) -> None:
        filedir = "E:/test/Androidscr/"
        if not os.path.exists(filedir):
            os.mkdir(os.path.join("E:/", "test", "Androidscr"))
        print("endTime:" + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())))
        screen_name = filedir + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time())) + ".png"
        self.driver.get_screenshot_as_file(screen_name)
        self.driver.quit()  # 关闭App

    def testlogout01_07(self):
        '''App是否能正常退出当前账号'''
        AppLogin(self.driver).appLogin()
        # 点击 个人主页 的设置齿轮按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/setting").click()
        # 点击 退出当前账号 按钮
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tvLogout").click()
        time.sleep(2)
        # 点击 确定
        self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/bt_positive").click()
        time.sleep(1)
        # 断言
        self.assertTrue(self.driver.find_element_by_id("cn.xiaochuankeji.tieba:id/tv_notLogin_goLogin").is_displayed())

if __name__ == "__main__":
    # suite = unittest.TestLoader().loadTestsFromTestCase(AndroidLogout)
    # unittest.TextTestRunner(verbosity=2).run(suite)
    unittest.main()
