from selenium.webdriver.common.by import By
from model.group import Group


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
        self.groups_cache = None

    def fill_in_form(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def open_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and wd.find_elements(By.NAME, "new")):
            wd.find_element(By.LINK_TEXT, "groups").click()

    groups_cache = None

    def get_groups_list(self):
        if self.groups_cache is None:
            wd = self.app.wd
            self.open_groups_page()
            self.groups_cache = []
            for el in wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = el.text
                group_id = el.find_element(By.NAME, "selected[]").get_attribute("value")
                self.groups_cache.append(Group(name=text, group_id=group_id))
        return list(self.groups_cache)

    def select_first_group(self):
        self.select_group_by_index(0)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_group_by_id(self, group_id):
        wd = self.app.wd
        wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % group_id).click()

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element(By.NAME, "delete").click()
        self.open_groups_page()
        self.groups_cache = None

    def delete_group_by_id(self, group_id):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(group_id)
        wd.find_element(By.NAME, "delete").click()
        self.open_groups_page()
        self.groups_cache = None

    def edit_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_index(index)
        wd.find_element(By.NAME, "edit").click()
        self.fill_in_form(new_group_data)
        wd.find_element(By.NAME, "update").click()
        self.open_groups_page()
        self.groups_cache = None

    def edit_group_by_id(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_group_by_id(new_group_data.group_id)
        wd.find_element(By.NAME, "edit").click()
        self.fill_in_form(new_group_data)
        wd.find_element(By.NAME, "update").click()
        self.open_groups_page()
        self.groups_cache = None

    def edit_first_group(self, new_group_data):
        self.edit_group_by_index(0,new_group_data)

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def clear_from_spaces(self, group):
        return Group(group_id=group.group_id, name=" ".join(group.name.strip().split()))
