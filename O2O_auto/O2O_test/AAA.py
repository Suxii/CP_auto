#-*-coding=utf-8-*-
import sys
from selenium.webdriver.support.ui import WebDriverWait
from O2O_test.public import print_color
sys.path.append("/public")
from public import *
import unittest,time


clr = print_color.Color()
clr.print_red_text('red')
