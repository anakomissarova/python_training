from selenium.webdriver.common.by import By


class ContactHelper:
    
    def __init__(self, app):
        self.app = app
        
    def create(self, contact):
        wd = self.app.wd
        # open contact creation form
        wd.find_element(By.LINK_TEXT, "add new").click()
        # fill in form
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").send_keys(contact.mobile)
        # submit form
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
        self.return_to_home_page()

    def return_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()
