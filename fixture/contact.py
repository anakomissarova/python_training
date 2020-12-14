from selenium.webdriver.common.by import By


class ContactHelper:
    
    def __init__(self, app):
        self.app = app
        
    def create(self, contact):
        wd = self.app.wd
        # open contact creation form
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill in form
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        # submit form
        wd.find_element(By.NAME, "submit").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_home_page()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        wd.find_element(By.NAME, "update").click()
        self.return_to_home_page()
