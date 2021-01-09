from selenium.webdriver.common.by import By
from model.contact import Contact
import re


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
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements(By.NAME, "selected[]")[index].click()
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        wd.find_element(By.CSS_SELECTOR, "div.msgbox")
        self.open_home_page()
        self.contacts_cache = None

    def edit_first_contact(self, contact):
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        self.fill_in_form(contact)
        wd.find_element(By.NAME, "update").click()
        self.open_home_page()
        self.contacts_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements(By.XPATH, "//img[@alt='Edit']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        wd.find_elements(By.XPATH, "//img[@alt='Details']")[index].click()

    def get_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        contact_id = wd.find_element(By.NAME, "id").get_attribute("value")
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        middlename = wd.find_element(By.NAME, "middlename").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        address = wd.find_element(By.NAME, "address").text
        home = wd.find_element(By.NAME, "home").get_attribute("value")
        work = wd.find_element(By.NAME, "work").get_attribute("value")
        mobile = wd.find_element(By.NAME, "mobile").get_attribute("value")
        secondary = wd.find_element(By.NAME, "phone2").get_attribute("value")
        email1 = wd.find_element(By.NAME, "email").get_attribute("value")
        email2 = wd.find_element(By.NAME, "email2").get_attribute("value")
        email3 = wd.find_element(By.NAME, "email3").get_attribute("value")
        return Contact(contact_id=contact_id, firstname=firstname, middlename=middlename, lastname=lastname,
                       address=address, home=home, mobile=mobile, work=work, secondary=secondary,
                       email1=email1, email2=email2, email3=email3)

    def get_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        contact_info = wd.find_element(By.ID, "content").text
        home = re.search("H: (.*)", contact_info).group(1) if re.search("H: (.*)", contact_info) else ""
        work = re.search("W: (.*)", contact_info).group(1) if re.search("W: (.*)", contact_info) else ""
        mobile = re.search("M: (.*)", contact_info).group(1) if re.search("M: (.*)", contact_info) else ""
        secondary = re.search("F: (.*)", contact_info).group(1) if re.search("F: (.*)", contact_info) else ""
        return Contact(home=home, mobile=mobile, work=work, secondary=secondary)

    def fill_in_form(self, contact):
        self.fill_in_field("firstname", contact.firstname)
        self.fill_in_field("middlename", contact.middlename)
        self.fill_in_field("lastname", contact.lastname)
        self.fill_in_field("mobile", contact.mobile)

    def fill_in_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
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
                lastname = contact.find_element(By.CSS_SELECTOR, "td:nth-of-type(2)").text
                firstname = contact.find_element(By.CSS_SELECTOR, "td:nth-of-type(3)").text
                address = contact.find_element(By.CSS_SELECTOR, "td:nth-of-type(4)").text
                emails = wd.find_element(By.CSS_SELECTOR, "td:nth-of-type(5)").text
                phones = contact.find_element(By.CSS_SELECTOR, "td:nth-of-type(6)").text
                self.contacts_cache.append(Contact(contact_id=contact_id, firstname=firstname, lastname=lastname,
                                                   address=address, phones_from_homepage=phones,
                                                   emails_from_homepage=emails))
        return list(self.contacts_cache)
