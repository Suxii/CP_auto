#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import random

def payfor(self):
    driver=self.driver
    #选择用钱包支付
    #选择余款支付方式
    #确认付款
    driver.find_element_by_xpath("//button[@class='button']").click()
    time.sleep(2)
