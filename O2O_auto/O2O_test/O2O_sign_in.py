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
        self.driver = webdriver.Firefox()
        time.sleep(3)
        self.base_url = "http://172.20.135.45"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_sign_in(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(5)
        driver.set_window_size(360,700)

        #启动注册流程
        driver.execute_script("$('#nav-bottom li:eq(3)').click()")
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//button[@id='submit']"))


        #调用登录接口
        driver.implicitly_wait(5)
        try:
            sign_in.sign_in(self)
            print u"登陆成功"
        except:
            print u"登录出现错误"
        finally: pass

#运行
if __name__ == "__main__":
    unittest.main()

