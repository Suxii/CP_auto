#-*-coding=utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from distutils import dir_util
from selenium.webdriver.common.proxy import ProxyType

import sys
import unittest,time
sys.path.append("/public")
from public import *



class O2O_category_order(unittest.TestCase):
  # 初始化
    def setUp(self):
        setUp.setUp_profile(self)

    def test_category_order(self):
        driver = self.driver
        sign_in.sign_in(self)

        #清空购物车
        clean_cart.clean_cart(self)

        #选择类目中所有商品加入购物车
        allpick_add.allpick_add(self)

        #进入购物车
        driver.execute_script("$('#nav-bottom li:eq(2)').click()")
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//button[@id='gotopay']"))
        payment = driver.execute_script("return $('.price-discount:last').text()")
        print u"合计金额为 " + payment

        #结算
        print u"====进行结算===="
        driver.find_element_by_xpath("//button[@id='gotopay']").click()
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//button[@id='gotopay']"))

        #提交订单
        print u"====转入订单结算===="
        order_commit.order_commit(self)
        time.sleep(1)

        #确认支付
        print u"====转到支付===="
        payfor.payfor(self)

        #退出
        quit_close.quit_close(self)

#运行
if __name__ == "__main__":
    unittest.main()


