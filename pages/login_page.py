from selenium.webdriver.common.by import By
from base.base_page import BasePage

import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

        self.username_input = (By.NAME, "user-name")
        self.password_input = (By.NAME, "password")
        self.login_button = (By.ID, "login-button")

   
    def login(self, username, password):
        self.find(self.username_input).send_keys(username)
        self.find(self.password_input).send_keys(password)
        time.sleep(2)
        self.click(self.login_button)
        assert "/inventory.html" in self.driver.current_url, "Login failed or did not redirect to inventory page"


    
    