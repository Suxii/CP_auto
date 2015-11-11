#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import random

from O2O_test.public.Assert import commit_scan

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

    commit_scan.commit_scan(self)

    time.sleep(0.25)
