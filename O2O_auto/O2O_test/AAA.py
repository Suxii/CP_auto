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
from distutils import dir_util
from selenium.webdriver.common.proxy import ProxyType

import sys
sys.path.append("/public")
from public import *
import unittest,time
from O2O_test import *


class AAA(unittest.TestCase):

    def setUp(self):
        setUp.setUp_profile(self)

if __name__ == "__main__":
    unittest.main()
