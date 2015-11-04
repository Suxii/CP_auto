#-*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
import unittest, time

def sign_in(self):
    driver = self.driver
    driver.get(self.base_url + "/")
    driver.set_window_size(380,700)
    driver.implicitly_wait(5)

    #进入个人中心
    driver.execute_script("$('#nav-bottom li:eq(3)').click()")
    WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("//button[@id='submit']"))


    #调用登录接口
    driver.implicitly_wait(5)
    try:
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
        WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath("//div[@class='me-title']"))
        print u"登陆成功"
    except:
        print u"登录出现错误"
    finally: pass