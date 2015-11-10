#-*-coding: utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import  HTMLTestRunner
import sys
from selenium.webdriver.support.ui import WebDriverWait
sys.path.append("/public")
from public import *
import unittest,time,re


class O2O_sign_in(unittest.TestCase):

    #初始化
    def setUp(self):
        setUp.setUp_profile(self)

    def test_sign_in(self):
        driver = self.driver
        sign_in.sign_in(self)

        #退出
        quit_close.quit_close(self)

#运行
if __name__ == "__main__":
    unittest.main()

