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


class O2O_category_order(unittest.TestCase):

    #初始化
    def setUp(self):
        setUp.setUp_profile(self)

    def test_category_order(self):
        driver = self.driver
        sign_in.sign_in(self)

        #清空购物车
        clean_cart.clean_cart(self)

        #启动类目订货流程
        driver.execute_script("$('#nav-bottom li:eq(1)').click()")
        print u"进入类目"
        time.sleep(1)

        cate_num = str(driver.execute_script("return $('#left-menu li').length"))
        print u"当前共有%s条分类" %(cate_num)
        #循环执行类目
        for i in range(int(cate_num)):
            driver.execute_script("$('#left-menu li:eq(%s)').click()"%(i))
            ii = str(i+1)
            print u"进入第%s条分类..." %(ii)
            time.sleep(0.2)
            g_num = str(driver.execute_script(" return $('#cate-content li').length"))
            print u"当前分类下共有%s种商品" %(g_num)
            #默认选择每个分类下第一个商品
            # driver.execute_script("$('#cate-content li:eq(0)').click()")
            driver.find_element_by_xpath("//div[@id='cate-content']//li").click()
            time.sleep(0.3)
            driver.execute_script("$('#footer-bar a:eq(1)').click()") #加入购物车
            print u"选择该分类下第一个商品加入购物车"
            driver.back() #后退
            time.sleep(0.3)
            print u"加入购物车完成"

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




