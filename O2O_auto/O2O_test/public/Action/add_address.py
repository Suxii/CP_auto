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
    driver.execute_script("$('li:eq(-1)').click()")
    driver.implicitly_wait(5)
    driver.find_element_by_xpath("//input[@id='receiverName']").send_keys(u"能哥还是叼啊")
    driver.find_element_by_xpath("//input[@id='receiverPhone']").send_keys(u"15502369874")
    driver.execute_script("$('#recieve-time').val('收货时间不限')")
    driver.execute_script("$('#province').val('天津')")
    driver.execute_script("$('#city').val('市辖区')")
    driver.execute_script("$('#county').val('东城区')")
    driver.execute_script("$('#addrDetail').val('金蝶六楼相声团')")
    time.sleep(0.5)
    #保存
    driver.execute_script("$('#edit-address>div>div:eq(2)').click()")