# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from group import Group


class TestTestaddgroup():
  def setup_method(self, method):
    self.wd = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.wd.quit()
  
  def test_add_group(self):
    self.open_home_page()
    self.login(username="admin", password="secret")
    self.open_groups_page()
    self.create_group(Group(name="skdncjdns", header="kjndc skdjc ", footer="sjdcnsd kcj sdkjc sjd c"))
    self.open_groups_page()
    self.logout()

  def test_add_empty_group(self):
    self.open_home_page()
    self.login(username="admin", password="secret")
    self.open_groups_page()
    self.create_group(Group(name="", header="", footer=""))
    self.open_groups_page()
    self.logout()

  def logout(self):
    self.wd.find_element(By.LINK_TEXT, "Logout").click()

  def create_group(self, group):
    # init group creation
    self.wd.find_element(By.NAME, "new").click()
    # fill in groupform
    self.wd.find_element(By.NAME, "group_name").click()
    self.wd.find_element(By.NAME, "group_name").send_keys(group.name)
    self.wd.find_element(By.NAME, "group_header").send_keys(group.header)
    self.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
    # submit group creation
    self.wd.find_element(By.NAME, "submit").click()

  def open_groups_page(self):
    self.wd.find_element(By.LINK_TEXT, "groups").click()

  def login(self, username, password):
    self.wd.find_element(By.NAME, "user").send_keys(username)
    self.wd.find_element(By.NAME, "pass").send_keys(password)
    # self.wd.find_element(By.NAME, "pass").send_keys(Keys.ENTER) - doesn't work that way
    self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def open_home_page(self):
    self.wd.get("http://192.168.64.2/addressbook/index.php")
    self.wd.set_window_size(550, 691)
  
