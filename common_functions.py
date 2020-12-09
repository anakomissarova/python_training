from selenium.webdriver.common.by import By


def open_home_page(driver):
    driver.get("http://192.168.64.2/addressbook/index.php")


def login(driver, username, password):
    driver.find_element(By.NAME, "user").send_keys(username)
    driver.find_element(By.NAME, "pass").send_keys(password)
    # self.wd.find_element(By.NAME, "pass").send_keys(Keys.ENTER) - doesn't work that way
    driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()


def logout(driver):
    driver.find_element(By.LINK_TEXT, "Logout").click()
