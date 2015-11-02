#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time

def sign_in(self):
    driver = self.driver

    #输入登录信息
    print u"清空登录信息"
    driver.find_element_by_id("name").clear()
    print u"录入用户名为：Auto 密码：111111"
    driver.find_element_by_id("name").send_keys("Auto")
    driver.find_element_by_id("password").send_keys("111111")
    #点选登录
    print u"点选登录"
    driver.find_element_by_xpath("//button[@id='submit']").click()
    time.sleep(2)