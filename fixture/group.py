from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element(By.NAME, "new").click()
        # fill in group form
        wd.find_element(By.NAME, "group_name").click()
        self.fill_in_form(group)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.open_groups_page()

    def fill_in_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).send_keys(text)

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element(By.NAME, "delete").click()
        self.open_groups_page()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        wd.find_element(By.NAME, "edit").click()
        self.fill_in_form(new_group_data)
        wd.find_element(By.NAME, "update").click()
        self.open_groups_page()
