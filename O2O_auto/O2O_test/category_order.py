#-*-coding=utf-8-*-
import sys
import unittest
import time

from selenium.webdriver.support.ui import WebDriverWait

sys.path.append("/public")
from public import *

##############################################################################
# 采用遍历的方式对类目中的每项商品订货，采用加入购物车的方式，然后一起结算
##############################################################################

class O2O_category_order(unittest.TestCase):
  # 初始化
    def setUp(self):
        setUp.setUp_profile(self)

    def test_category_order(self):
        driver = self.driver
        sign_in.sign_in(self)

        #清空购物车
        clean_cart.clean_cart(self)

        #清空待付款
        clean_waitPay.clean_waitPay(self)

        #选择类目中所有商品加入购物车
        allpick_add.allpick_add(self)

        #进入购物车
        driver.execute_script("$('#nav-bottom li:eq(2)').click()")
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//button[@id='gotopay']"))
        payment = driver.execute_script("return $('.price-discount:last').text()")
        print u"合计金额为 " + payment

        #结算
        print u"结算购物车"
        driver.find_element_by_xpath("//button[@id='gotopay']").click()
        settle_scan.settle_scan(self)
        time.sleep(0.3)

        order_commit.order_commit(self)
        time.sleep(0.5)

        #确认支付
        payfor.payfor(self)

        #退出
        quit_close.quit_close(self)

#运行
if __name__ == "__main__":
    unittest.main()


