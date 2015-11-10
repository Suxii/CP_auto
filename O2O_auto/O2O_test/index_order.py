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
sys.path.append("/public")
from public import *
import unittest,time


class O2O_index_order(unittest.TestCase):

    #初始化
    def setUp(self):
        setUp.setUp_profile(self)

    def test_index_order(self):
        driver = self.driver
        sign_in.sign_in(self)

        #清空购物车
        clean_cart.clean_cart(self)

        #启动首页订货流程
        driver.execute_script("$('#nav-bottom li:eq(0)').click()")
        print u"====================进入首页===================="
        time.sleep(2)


        #选择秒杀栏前N个商品：
        print u"选择秒杀栏前N个商品"
        for i in range(1):#选择前两个商品
            driver.execute_script("$('#swiper-seckill img:eq(%s)').click()"%(i)) #进入商品
            driver.implicitly_wait(5)
            cart_num = int(driver.execute_script("return $('#shopCartNums').text()")) #记录操作之前的购物车数量
            driver.execute_script("$('#footer-bar a:eq(1)').click()") #加入购物车
            time.sleep(0.1)
            buy_scan.buy_scan(self,1,cart_num)
            driver.back() #后退
        time.sleep(0.3)

        #选择1元购的前N个商品：
        print u"选择1元购的前N个商品"
        for i in range(1):#选择前两个商品
            driver.execute_script("$('#swiper-street1 .swiper-slide:eq(%s)' img).click()"%(i)) #进入商品
            driver.implicitly_wait(5)
            cart_num = int(driver.execute_script("return $('#shopCartNums').text()")) #记录操作之前的购物车数量
            driver.execute_script("$('#footer-bar a:eq(1)').click()") #加入购物车
            time.sleep(0.1)
            buy_scan.buy_scan(self,1,cart_num)
            driver.back() #后退
        time.sleep(0.3)

        #选择答题购的前N个商品：
        print u"选择答题购的前N个商品"
        for i in range(1):#选择前两个商品
            driver.execute_script("$('#swiper-street2 .swiper-slide:eq(%s)' img).click()"%(i)) #进入商品
            driver.implicitly_wait(5)
            cart_num = int(driver.execute_script("return $('#shopCartNums').text()")) #记录操作之前的购物车数量
            driver.execute_script("$('#footer-bar a:eq(1)').click()") #加入购物车
            time.sleep(0.1)
            buy_scan.buy_scan(self,1,cart_num)
            driver.back() #后退
        time.sleep(0.3)

        print u"添加商品操作完成"

        #进入购物车
        driver.execute_script("$('#nav-bottom li:eq(2)').click()")
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//button[@id='gotopay']"))
        payment = driver.execute_script("return $('.price-discount:last').text()")
        print u"合计金额为 " + payment

        #结算
        print u"进行结算"
        driver.find_element_by_xpath("//button[@id='gotopay']").click()
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//button[@id='gotopay']"))

        #提交订单
        print u"转入订单结算"
        order_commit.order_commit(self)
        time.sleep(1)

        #确认支付
        print u"转到支付"
        payfor.payfor(self)

        #退出
        quit_close.quit_close(self)

#运行
if __name__ == "__main__":
    unittest.main()

