#-*-coding=utf-8-*-
import sys

from selenium.webdriver.support.ui import WebDriverWait
sys.path.append("/public")
from public import *
import unittest


class O2O_sign_up(unittest.TestCase):

    #初始化
    def setUp(self):
        setUp.setUp_profile(self)

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

        #退出
        quit_close.quit_close(self)

#运行
if __name__ == "__main__":
    unittest.main()

