from selenium.webdriver.common.by import By
from base.base_page import BasePage

import time

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    def add_to_cart(self, item_name):
        item_selector = f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button"
        add_to_cart_button = self.driver.find_element(By.XPATH, item_selector)
        add_to_cart_button.click()
        time.sleep(1)

    def go_to_cart(self):
        cart_button = self.driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
        cart_button.click()
        time.sleep(1)

    


    


    
    