from base.base_test import BaseTest
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.iventory_page import InventoryPage
from pages.login_page import LoginPage
from utils.config_reader import ConfigReader

import time

class TestCheckout(BaseTest):
    def test_checkout(self):
        config = ConfigReader.load_config()

        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        
        time.sleep(1)
        self.allure_screenshot("1_test_checkout_login_screenshot")
        
        login_page.login(config.username, config.password)

        time.sleep(5)
        self.allure_screenshot("2_test_checkout_dashboard_screenshot")

        time.sleep(1)

        inventory_page.add_to_cart("Sauce Labs Bike Light")
        inventory_page.add_to_cart("Sauce Labs Bolt T-Shirt")
        inventory_page.add_to_cart("Sauce Labs Fleece Jacket")

        time.sleep(2)
        inventory_page.go_to_cart()
        self.allure_screenshot("3_test_checkout_cart_screenshot")

        cart_page.click_checkout()

        checkout_page.enter_shipping_info("John", "Doe", "70000")
        time.sleep(2)
        self.allure_screenshot("4_test_checkout_enter_shipping_info_screenshot")
        checkout_page.click_continue()

        checkout_page.scroll_to_bottom()
        time.sleep(2)
        self.allure_screenshot("5_test_checkout_scroll_to_bottom_screenshot")

        checkout_page.click_finish()

        time.sleep(2)
        self.allure_screenshot("6_test_checkout_did_click_finish_screenshot")

        assert checkout_page.verify_checkout_complete(), "Checkout was not completed successfully"

