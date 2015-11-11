#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time,os


def buy_scan(self,mode,cart_num,goods_num=1):
    driver = self.driver
    if mode == 0:
        try:
            t = 1
            while True:
                time.sleep(0.1)
                t = t + 1
                #检测库存不足
                if driver.execute_script("return $('.app-notify').text() == '被抢光辣,麻烦亲再看看其它宝贝吧~'"):
                    fault0 = driver.execute_script("return $('.app-notify').text()")
                    print "!!!--------*--------error:" + fault0+ "--------*--------!!!"
                    break

                elif driver.execute_script("return $('button#gotopay').length == 1"):#判断进入了订单界面
                    print u"立即购买成功，转入确认订单界面"
                    break

                #超时检测
                elif t == 20:
                    raise AssertionError
                    break

        except AssertionError:
            print u"立即购买失败：操作超时"

        except NoSuchElementException:
            print u"立即购买失败，未能定位[立即购买]按钮"



    elif mode == 1:
        try:
            t = 1
            while True:
                time.sleep(0.1)
                t = t + 1
                #检测库存不足
                if driver.execute_script("return $('.app-notify').text() == '被抢光辣,麻烦亲再看看其它宝贝吧~'"):
                    fault0 = driver.execute_script("return $('.app-notify').text()")
                    print "!!!--------*--------error:" + fault0 + "--------*--------!!!"
                    break

                #检测是否跳转购物车页面
                # elif driver.execute_script("return $('#shopCartNums').text()"):
                #     print "!!!--------*--------error:加入购物车按钮异常--------*--------!!!"
                #     break

                #检测购物车数量异常
                elif int(driver.execute_script("return $('#shopCartNums').text()")) != (cart_num + goods_num):
                    raise TypeError(u"购买数量异常")
                    break


                #检测是否成功加入购物车
                elif int(driver.execute_script("return $('#shopCartNums').text()")) == (cart_num + goods_num):
                    print u"加入购物车成功,待支付"
                    break

                #超时检测
                elif t == 20:
                    raise AssertionError
                    break

        except AssertionError:
            print u"加入购物车失败：操作超时"

        except TypeError:
            fault1 = u"异常捕捉：购买数量异常"
            print "!!!--------*--------error:" + fault1 + "--------*--------!!!"

        except NoSuchElementException:
            print u"加入购物车失败，未能定位[加入购物车]按钮"

