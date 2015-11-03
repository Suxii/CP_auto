#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import random

def add_address(self):
    driver = self.driver
    #进入收货地址
    driver.execute_script("$('div.me-content:eq(2) h2.me-content-title').click()")
    driver.implicitly_wait(5)
    time.sleep(0.2)
    addr_num = driver.execute_script("$('li').length")
    print u"当前共有%s个收货地址"%(addr_num)
    driver.implicitly_wait(5)
    driver.execute_script("$('.right:eq(-2) button:first').click()")
    driver.implicitly_wait(5)
    time.sleep(0.5)