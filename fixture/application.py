from selenium import webdriver
from selenium.webdriver.common.by import By


class Application:
    def __init__(self):
        self.wd = webdriver.Firefox()
        self.vars = {}

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        self.wd.get("http://192.168.64.2/addressbook/index.php")

    def login(self, username, password):
        self.open_home_page()
        self.wd.find_element(By.NAME, "user").send_keys(username)
        self.wd.find_element(By.NAME, "pass").send_keys(password)
        # self.wd.find_element(By.NAME, "pass").send_keys(Keys.ENTER) - doesn't work that way
        self.wd.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        self.wd.find_element(By.LINK_TEXT, "Logout").click()

    def create_group(self, group):
        self.open_groups_page()
        # init group creation
        self.wd.find_element(By.NAME, "new").click()
        # fill in group form
        self.wd.find_element(By.NAME, "group_name").click()
        self.wd.find_element(By.NAME, "group_name").send_keys(group.name)
        self.wd.find_element(By.NAME, "group_header").send_keys(group.header)
        self.wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        self.wd.find_element(By.NAME, "submit").click()
        self.open_groups_page()

    def open_groups_page(self):
        self.wd.find_element(By.LINK_TEXT, "groups").click()

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
        self.return_to_home_page()

    def return_to_home_page(self):
        self.wd.find_element(By.LINK_TEXT, "home page").click()