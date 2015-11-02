#-*-coding=utf-8-*-
import unittest
import HTMLTestRunner
import time
import os
import sys
sys.path.append("/O2O_test")
from O2O_test import *

if __name__ == "__main__":
#定义一个单元测试容器
    testunit = unittest.TestSuite()

#酱测试用例加入测试容器
alltestnames = [
    O2O_sign_up.O2O_sign_up,
    O2O_sign_in.O2O_sign_in
    ]
for test in alltestnames:
    testunit.addTest(unittest.makeSuite(test))

#取执行时间
now= time.strftime(u"%Y-%m-%d  %H.%M.%S", time.localtime())
#定义测试报告的存放路径，支持相对路路径
cur_dir = "D:\\autotest\\report"
folder_name = now+u"测试报告"
if os.path.isdir(cur_dir):
    os.mkdir(os.path.join(cur_dir,folder_name))
    ad = "D:\\autotest\\report\\"+folder_name
    os.chdir(ad)
    filename = (now+'_result.html')
    fp = file(filename, 'wb')

#定义测试报告
runner = HTMLTestRunner.HTMLTestRunner(
    stream = fp,
    title = u'CP自动化用例测试报告',
    description = u'用例执行情况:')

#运行测试用例
runner.run(testunit)