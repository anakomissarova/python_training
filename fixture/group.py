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
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.open_groups_page()

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "delete").click()
        self.open_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.NAME, "edit").click()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        wd.find_element(By.NAME, "update").click()
        self.open_groups_page()