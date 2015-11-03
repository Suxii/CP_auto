#-*- coding: utf-8 -*-
from selenium import webdriver
import unittest, time

def setUp_profile(self):
    #配置火狐各人文件
    profile = webdriver.FirefoxProfile(r"Q:\firefoxx")
    #制定火狐浏览器
    self.driver = webdriver.Firefox(profile)
    time.sleep(3)
    self.base_url = "http://xd.k3cloud.kingdee.com"
    self.verificationErrors = []
    self.accept_next_alert = True