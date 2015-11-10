#-*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time
import buy_scan

#所有类目商品加入购物车，使用前必须在可以点击类目的界面
#启动类目订货流程

def allpick_add(self):
    driver = self.driver
    driver.execute_script("$('#nav-bottom li:eq(1)').click()") #点击类目
    print u"进入类目"
    time.sleep(1)

    cate_num = str(driver.execute_script("return $('#left-menu li').length")) #记录分类数量
    print u"当前共有%s条分类" %(cate_num)

    #循环执行类目
    for i in range(int(cate_num)):
        driver.execute_script("$('#left-menu li:eq(%s)').click()"%(i))
        ii = str(i+1)
        time.sleep(0.2)
        g_num = str(driver.execute_script(" return $('#cate-content li').length")) #记录商品种类数量
        print u"=-=-=-=进入第%s条分类..." %(ii)+u"当前分类下共有%s种商品=-=-=-=" %(g_num)


        #进入商品详情
        for n in range(int(g_num)):
            #driver.find_element_by_xpath("//div[@id='cate-content']//li").click()
            driver.execute_script("$('#left-menu li:eq(%s)').click()"%(i))
            time.sleep(0.3)
            driver.execute_script("$('#cate-content li:eq(%s) div').click()"%(n))
            #参数
            cart_num = int(driver.execute_script("return $('#shopCartNums').text()")) #记录操作之前的购物车数量
            goods_num = 1 #购买商品数量默认为 1
            time.sleep(0.3)

            print u"选择该分类下第%s个商品加入购物车"%(n+1)
            driver.execute_script("$('#footer-bar a:eq(1)').click()") #加入购物车

            buy_scan.buy_scan(self,1,cart_num,goods_num)

            driver.back() #后退

            time.sleep(0.2)

