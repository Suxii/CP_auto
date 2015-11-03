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


        #启动首页订货流程
        driver.execute_script("$('#nav-bottom li:eq(0)').click()")
        print u"进入首页"
        time.sleep(2)


        #选择秒杀栏前N个商品：
        driver.find_element_by_xpath("//div[@id='swiper-seckill']/div/div/img").click()
        driver.implicitly_wait(5)
        # driver.execute_script("$('#footer-bar a:eq(0)').click()") #立即购买
        driver.execute_script("$('#footer-bar a:eq(1)).click()") #加入购物车
        driver.back() #后退

        #选择分会场的前N个商品：
        driver.find_element_by_xpath("//div[@id='swiper-street1']/div/div/img").click()
        driver.implicitly_wait(5)
        # driver.execute_script("$('#footer-bar a:eq(0)').click()") #立即购买
        driver.execute_script("$('#footer-bar a:eq(1)').click()") #加入购物车
        driver.back() #后退

        print u"加入购物车完成"

        # for i in range(1):
        #     # driver.find_element_by_xpath("//div[@id='swiper-seckill']/div/div[(%s)]/img"%(i)).click()
        #     # driver.find_element_by_xpath("//div[@id='swiper-seckill']/div[@class='swiper-wrapper']/div[%s]"%(i)).click()
        #     driver.execute_script("$('div#swiper-seckill div.swiper-wrapper>div:eq(%s)').click()"%(i))
        #     driver.implicitly_wait(5)
        #     driver.find_element_by_xpath(u"//[contains(text(),'加入购物车')]").click()
        #     time.sleep(0.2)
        #     driver.navigate().back()
        #     i = i + 1


