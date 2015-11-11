#-*- coding: utf-8 -*-

#打印商品详情页面的基础信息

def print_goods(self):
    driver = self.driver
    g_title = driver.execute_script("return $('#g-title .title h3').text()")
    print u"商品名称" + g_title
    g_price = driver.execute_script("return $('.price-integer').text()")
    print u"商品单价" + g_price
    price = driver.execute_script("return $('#g-price span:eq(3)').text()")
    print u"商品原价" + price
    g_inventory = driver.execute_script("return $('#stayStockNums').text()")
    print u"当前库存" + g_inventory

    driver.execute_script("$('#buttons-wrap div:eq(0)').click()")
    g_detail = driver.execute_script("return $('#tab1 p').text()")
    driver.execute_script("$('#buttons-wrap div:eq(1)').click()")

    #打印商品参数
    g_argument = driver.execute_script("return $('#tab2 .name').length")
    for i in range(int(g_argument)):
        print driver.execute_script("return $('#tab2 .name:eq(%s) .label').text()"%(i)) + ": " + driver.execute_script("return $('#tab2 .name:eq(%s) .title').text()"%(i)) +"\n"

    #打印FAQ
    # print driver.execute_script("return $('#tab3').text()")
    print "FAQ"

