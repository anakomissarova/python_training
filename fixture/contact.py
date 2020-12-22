from selenium.webdriver.common.by import By


class ContactHelper:
    
    def __init__(self, app):
        self.app = app
        
    def create(self, contact):
        wd = self.app.wd
        self.open_home_page()
        # open contact creation form
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill in form
        self.fill_in_form(contact)
        # submit form
        wd.find_element(By.NAME, "submit").click()
        self.open_home_page()

    def open_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.open_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.fill_in_form(contact)
        wd.find_element(By.NAME, "update").click()
        self.open_home_page()

    def fill_in_form(self, contact):
        wd = self.app.wd
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)

    def count(self):
        wd = self.app.wd
        return len(wd.find_elements(By.NAME, "selected[]"))