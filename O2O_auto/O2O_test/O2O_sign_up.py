#-*-coding=utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
import sys
sys.path.append("/public")
from public import *
import unittest,time


class O2O_sign_up(unittest.TestCase):

    #初始化
    def setUp(self):
        self.driver = webdriver.Firefox()
        time.sleep(3)
        self.base_url = "http://172.20.135.45"
        self.verificationErrors = []
        self.accept_next_alert = True
    #进入注册流程
    def test_sign_up(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.implicitly_wait(5)
        #调整浏览器大小
        driver.set_window_size(360,700)
        print u"调整浏览器大小"

        #启动注册流程
        driver.execute_script("$('#nav-bottom li:eq(3)').click()")
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//button[@id='submit']"))
        print u"进入注册页面"
        driver.find_element_by_xpath("//div[@class='login-helper']/a[1]").click()
        WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//button[@id='submitButton']"))

        #调用注册接口
        driver.implicitly_wait(5)
        try:
            sign_up.sign_up(self)
            print u"注册成功"
        except:
            print u"注册出现错误"
        finally: pass

#运行
if __name__ == "__main__":
    unittest.main()

