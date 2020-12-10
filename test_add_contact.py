# Generated by Selenium IDE
from selenium import webdriver
from selenium.webdriver.common.by import By
from contact import Contact


class TestAddContact:
    def setup_method(self):
        self.wd = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self):
        self.wd.quit()

    def test_add_contact(self):
        self.open_home_page()
        self.login(username='admin', password='secret')
        self.create_contact(Contact(firstname='test contact', mobile='+78943562435'))
        self.return_to_home_page()
        self.logout()

    def open_home_page(self):
        self.wd.get("http://192.168.64.2/addressbook/index.php")

    def login(self, username, password):
        self.wd.find_element(By.NAME, "user").send_keys(username)
        self.wd.find_element(By.NAME, "pass").send_keys(password)
        # self.wd.find_element(By.NAME, "pass").send_keys(Keys.ENTER) - doesn't work that way
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def create_contact(self, contact):
        # open contact creation form
        self.wd.find_element(By.LINK_TEXT, "add new").click()
        # fill in form
        self.wd.find_element(By.NAME, "firstname").click()
        self.wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        self.wd.find_element(By.NAME, "mobile").click()
        self.wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        # submit form
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()

    def return_to_home_page(self):
        self.wd.find_element(By.LINK_TEXT, "home page").click()
