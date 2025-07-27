from base.base_test import BaseTest
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader

import time

class TestLogin(BaseTest):
    def test_login(self):
        config = ConfigReader.load_config()
        
        login_page = LoginPage(self.driver)
        
        time.sleep(1)
        self.allure_screenshot("test_login_screenshot")

        login_page.login(config.username, config.password)

        time.sleep(2)
        self.allure_screenshot("test_login_inventory_screenshot")

        
        
