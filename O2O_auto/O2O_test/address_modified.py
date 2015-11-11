#-*-coding=utf-8-*-
import random
import sys
import unittest
import time
from selenium.webdriver.support.ui import WebDriverWait
sys.path.append("/public")
from public import *



class O2O_address_modified(unittest.TestCase):
  # ≥ı ºªØ
    def setUp(self):
        setUp.setUp_profile(self)

    def test_address_modified(self):
        driver = self.driver
        sign_in.sign_in(self)

        add_address.add_address(self)
        update_address.update_address(self)
        delete_address.add_address(self)
