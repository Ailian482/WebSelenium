import time
from Uiframe0test.public.pagenew import NewPage # 调用新页面

class ProInfo(object):
    def __init__(self, driver):
        self.driver = driver

    def proinfo(self):  # 进入到“女装sss优质长绒棉A字型条纹连衣裙(七分袖) 412932 优衣库UNIQLO”商品详情页面
        # 滚动到页面中间
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.5)")
        time.sleep(1)
        NewPage(self.driver).p_newpage("//div[@class='detail'][1]/div/div/dl[4]/dd[1]/a")

    def proinfo1(self, way, text):  # 自定义进入商品详情页面，way代表控件的定位方式, text代表控件的定位信息
        # 滚动到页面中间
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight*0.5)")
        time.sleep(1)
        if way == "xpath":
            # self.driver.find_element_by_xpath("//div[@class='detail'][1]/div/div/dl[1]/dd[1]/a").click()
            NewPage(self.driver).p_newpage(text)
            time.sleep(2)

        elif way == "css":
            NewPage(self.driver).c_newpage(text)
            time.sleep(2)
        elif way == "link":
            NewPage(self.driver).l_newpage(text)
            time.sleep(2)
