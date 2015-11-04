#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import random

def clean_cart(self):
    driver=self.driver

    #清空购物车
    print u"启动清空购物车流程..."
    driver.execute_script("$('#nav-bottom li:eq(2)').click()")
    s_num = str(driver.execute_script("return $('.cart-list li').length"))

    if s_num == 0:
        print u"当前购物车为空"
        driver.execute_script("$('#nav-bottom li:eq(0)').click()")
    else:
        print u"当前购物车中共有%s种商品"%(s_num)
        driver.execute_script("$('i').click()")
        time.sleep(0.2)
        driver.execute_script("$('#dialog-yes').click()")
        print u"清空购物车成功"

    time.sleep(1)
