# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTestaddgroup():
  def setup_method(self, method):
    self.wd = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.wd.quit()
  
  def test_test_add_group(self):
    self.wd.get("http://192.168.64.2/addressbook/index.php")
    self.wd.set_window_size(550, 691)
    self.wd.find_element(By.NAME, "user").send_keys("admin")
    self.wd.find_element(By.NAME, "pass").send_keys("secret")
    #self.wd.find_element(By.NAME, "pass").send_keys(Keys.ENTER) - doesn't work that way
    self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
    self.wd.find_element(By.LINK_TEXT, "groups").click()
    self.wd.find_element(By.NAME, "new").click()
    self.wd.find_element(By.NAME, "group_name").click()
    self.wd.find_element(By.NAME, "group_name").send_keys("skdncjdns")
    self.wd.find_element(By.NAME, "group_header").send_keys("kjndc skdjc ")
    self.wd.find_element(By.NAME, "group_footer").send_keys("sjdcnsd kcj sdkjc sjd c")
    self.wd.find_element(By.NAME, "submit").click()
    self.wd.find_element(By.LINK_TEXT, "groups").click()
    self.wd.find_element(By.LINK_TEXT, "Logout").click()
  
