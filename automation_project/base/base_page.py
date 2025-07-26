from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find (self, by_locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(by_locator))

    def click(self, by_locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(by_locator)).click()

        

    