from selenium.webdriver.common.by import By
from base.base_page import BasePage

import time

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_shipping_info(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        time.sleep(1)

    def click_continue(self):
        self.driver.find_element(By.XPATH, "//input[@id='continue']").click()
        time.sleep(1)

    def click_finish(self):
        self.driver.find_element(By.XPATH, "//button[@id='finish']").click()
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)

    def verify_checkout_complete(self):
        success_message = self.driver.find_element(By.XPATH, "//h2[@class='complete-header']").text
        success_message_2 = self.driver.find_element(By.XPATH, "//div[@class='complete-text']").text

        return "Thank you for your order!" in success_message and "Your order has been dispatched, and will arrive just as fast as the pony can get there!" in success_message_2

    
    