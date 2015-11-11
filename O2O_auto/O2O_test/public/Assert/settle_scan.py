#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time,os

def settle_scan(self):
    driver = self.driver
    try:
        #提交购物车信息
        print u"提交购物车信息"
        t = 1
        while True:
            time.sleep(0.1)
            t = t + 1

            if driver.execute_script("return $('.app-notify').text() == '未选择任何商品~'"):
                fault0 = driver.execute_script("return $('.app-notify').text()")
                print "!!!--------*--------error:" + fault0+ "--------*--------!!!"
                break

            if driver.execute_script("return $('#gotopay').text() == '提交订单'"):#判断进入了提交订单界面
                print u"提交购物车信息成功：转入提交订单界面"
                break

            elif t == 20:
                raise AssertionError
                break

    except AssertionError:
        print u"提交购物车信息失败：提交超时"
