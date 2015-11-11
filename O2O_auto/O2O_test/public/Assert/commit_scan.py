#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time,os

def commit_scan(self):
    driver = self.driver
    try:
        #提交结算订单
        print u"提交结算信息"
        driver.find_element_by_xpath("//button[@id='gotopay']").click()
        t = 1
        while True:
            time.sleep(0.1)
            t = t + 1

            if driver.execute_script("return $('.app-notify').text() == '库存不足辣~'"):
                fault0 = driver.execute_script("return $('.app-notify').text()")
                print "!!!--------*--------error:" + fault0+ "--------*--------!!!"
                break

            elif driver.execute_script("return $('.app-notify').text() == '限购宝贝一天只能购买一次哟~'"):
                fault1 = driver.execute_script("return $('.app-notify').text()")
                print "!!!--------*--------error:" + fault1+ "--------*--------!!!"
                break

            elif driver.execute_script("return $('.button').length == 1"):#判断进入了支付界面
                print u"提交结算订单成功，转入支付界面"
                break

            elif t == 20:
                raise AssertionError
                break

    except AssertionError:
        print u"提交结算订单失败：提交超时"

    except NoSuchElementException:
        print u"提交结算订单失败，无法定位[提交订单]按钮"
