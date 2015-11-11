#-*-coding=utf-8-*-
import random
import sys
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
sys.path.append("/public")
from public import *



class O2O_perfer_order(unittest.TestCase):
  # 初始化
    def setUp(self):
        setUp.setUp_profile(self)

    def test_perfer_order(self):
        driver = self.driver
        sign_in.sign_in(self)

        #启动“猜你喜欢”订货流程
        print u"启动--猜你喜欢--订货流程"
        driver.execute_script("$('#nav-bottom li:eq(0)').click()")
        time.sleep(2)

        #选择第一个商品进入详情
        driver.execute_script("$('#swiper-seckill img:eq(0)').click()") #进入商品
        driver.implicitly_wait(5)

        #获取推荐商品的数量
        g_recommend = int(driver.execute_script("return $('#g-recommend .swiper-slide').length"))
        print u"猜你喜欢栏中共有%s件推荐商品"%(g_recommend)

        #在推荐商品中随机取一件下单
        x = random.randint(0,g_recommend-1)
        print u"随机选取一件推荐商品下单"
        driver.execute_script("$('#g-recommend .swiper-slide:eq(%s) img').click()"%(x))
        print u"进入商品详情成功"
        time.sleep(0.3)

        #选择立即购买
        cart_num = int(driver.execute_script("return $('#shopCartNums').text()")) #记录操作之前的购物车数量
        driver.execute_script("$('#footer-bar a:eq(0)').click()") #立即购买
        buy_scan.buy_scan(self,0,cart_num)
        time.sleep(0.3)

        #提交订单
        order_commit.order_commit(self)
        time.sleep(1)

        #确认支付
        payfor.payfor(self)

        #退出
        quit_close.quit_close(self)

#运行
if __name__ == "__main__":
    unittest.main()
