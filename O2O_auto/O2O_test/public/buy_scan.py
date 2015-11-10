#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time

def buy_scan(self,mode,cart_num,goods_num=1):
    driver = self.driver

    if mode == 0:
        try:
            t = 1
            while True:
                time.sleep(0.1)
                t = t + 1
                #检测库存不足
                if driver.execute_script("$('.app-notify').text() == '被抢光辣,麻烦亲再看看其它宝贝吧~'") or t == 20:
                    fault0 = driver.execute_script("return $('.app-notify').text()")
                    print "!!!--------*--------error:" + fault0+ "--------*--------!!!"
                    break
        except:
            print u"立即购买成功，转入确认订单界面"


    elif mode == 1:
        try:
            t = 1
            while True:
                time.sleep(0.1)
                t = t + 1
                #检测库存不足
                if driver.execute_script("$('.app-notify').text() == '被抢光辣,麻烦亲再看看其它宝贝吧~'") or t == 20:
                    fault0 = driver.execute_script("return $('.app-notify').text()")
                    print "!!!--------*--------error:" + fault0+ "--------*--------!!!"
                    break

                #检测购物车数量异常
                elif int(driver.execute_script("return $('#shopCartNums').text()")) != (cart_num + goods_num):
                    fault1 = u"购买数量异常"
                    print "!!!--------*--------error:" + fault1 + "--------*--------!!!"
                    break
        except:
            print u"加入购物车成功"

