#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time
import random

def clean_waitPay(self):
    driver = self.driver
    #清空待付款
    print u"启动清空待付款流程..."
    driver.execute_script("$('#nav-bottom li:eq(3)').click()")
    WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath("//div[@class='myoder']"))
    waitPay = int(driver.execute_script("return $('.me-content .app-flex div:eq(0) #count').text()")) #记录未付款订单数
    driver.execute_script("$('.app-flex div:eq(0)').click()") #点击待付款

    WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath("//div[@id='dfk']"))
    if waitPay == 0:
        print u"当前待付款订单数为零"
        driver.execute_script("$('#nav-bottom li:eq(0)').click()")
    else:
        print u"当前共有%s张待付款订单"%(waitPay)
        driver.execute_script("$('i').click()")
        time.sleep(0.2)
        print u"清空待付款成功"

    time.sleep(1)