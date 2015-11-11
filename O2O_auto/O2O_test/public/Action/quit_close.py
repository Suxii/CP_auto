#-*-coding=utf-8-*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time

def quit_close(self):
    driver = self.driver
    self.driver.quit()
    self.assertEqual([],self.verificationErrors)
    time.sleep(2)

