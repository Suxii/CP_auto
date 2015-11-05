#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import random

def order_commit(self):
    driver = self.driver
    #描述结算信息
    driver.execute_script("$('li.inline-block-wrap div:first').click()")
    print u"选择送货方式为上门自提"

    driver.execute_script("$('.icheckbox_square-blue:eq(0)').click()") #第一个单选框 开具发票
    print u"选择开具发票"

    driver.execute_script("$('.icheckbox_square-blue:eq(1)').click()") #第二个单选框 积分抵扣
    print u"选择积分抵扣"

    spayment = str(driver.execute_script("return $('#payMoney').text()"))
    print u"应支付金额为 ￥" + spayment

    #提交结算订单
    print u"提交结算订单"
    driver.find_element_by_xpath("//button[@id='gotopay']").click()

    try:
        t = 1
        while True:
            time.sleep(0.1)
            t = t + 1
            if driver.execute_script("$('.app-notify').text() == '库存不足辣~'") or t == 10:
                fault = str(driver.execute_script("return $('.app-notify').text()"))
                print u"报错:" + fault
                break
    except:
        print u"提交结算订单成功"

    time.sleep(0.25)
