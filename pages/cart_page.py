from selenium.webdriver.common.by import By
from base.base_page import BasePage

import time

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_checkout(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        checkout_button = self.driver.find_element(By.XPATH, "//button[@id='checkout']")
        checkout_button.click()
        time.sleep(1)


    


    
    