#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time
import random

def payfor(self):
    driver=self.driver
    try:
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//button[@class='button']"))
        print u"转入付款界面"
        #选择用钱包支付
        #选择余款支付方式
        #确认付款
        try:
            driver.find_element_by_xpath("//button[@class='button']").click()
            print u"确认使用微信付款"
        except:
            print u"付款失败"
    except:
        print u"转入付款界面失败"
        pass
    time.sleep(2)
