from selenium.webdriver.common.by import By
from model.contact import Contact


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
        self.contacts_cache = None

    def open_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/index.php"):
            wd.find_element(By.LINK_TEXT, "home").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element(By.CSS_SELECTOR, "div.msgbox")
        self.open_home_page()
        self.contacts_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_home_page()
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.fill_in_form(contact)
        wd.find_element(By.NAME, "update").click()
        self.open_home_page()
        self.contacts_cache = None

    def fill_in_form(self, contact):
        self.fill_in_field("firstname", contact.firstname)
        self.fill_in_field("middlename", contact.middlename)
        self.fill_in_field("lastname", contact.lastname)
        self.fill_in_field("mobile", contact.mobile)

    def fill_in_field(self, field_name, text):
        wd = self.app.wd
        if text:
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contacts_cache = None

    def get_contacts_list(self):
        if self.contacts_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contacts_cache = []
            for contact in wd.find_elements(By.NAME, "entry"):
                contact_id = contact.find_element(By.NAME, "selected[]").get_attribute("id")
                firstname = contact.find_element(By.CSS_SELECTOR, "td:nth-of-type(3)").text
                lastname = contact.find_element(By.CSS_SELECTOR, "td:nth-of-type(2)").text
                self.contacts_cache.append(Contact(contact_id=contact_id, firstname=firstname, lastname=lastname))
        return list(self.contacts_cache)