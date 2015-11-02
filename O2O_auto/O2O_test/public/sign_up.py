#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import random

def sign_up(self):
    driver = self.driver

    #生成随机电话号码与用户名
    rnum = random.randint(13000000000,13999999999)
    ruser = "Auto" + str(random.randint(1000,9999))
    print u"生成随机信息"

    #输入注册信息
    driver.find_element_by_id("mobile").clear()
    driver.find_element_by_id("mobile").send_keys("%s"%(rnum))
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys("%s"%(ruser))
    driver.find_element_by_id("password").send_keys("111111")
    driver.find_element_by_id("password2").send_keys("111111")
    print u"录入注册信息成功"

    #点选同意协议
    driver.find_element_by_xpath("//ins").click()
    print u"勾选协议"
    time.sleep(0.25)

    #点选注册
    driver.find_element_by_xpath("//button[@id='submitButton']").click()
    print u"注册..."
    time.sleep(2)

