import pytest
import allure
from selenium import webdriver
from utils.config_reader import ConfigReader

class BaseTest:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, request):
        config = ConfigReader.load_config()

        driver = webdriver.Chrome()
        driver.get(config.base_url)
        
        request.cls.driver = driver
        yield
        driver.quit() 


    def allure_screenshot(self, name="dashboard_screenshot"):
        screenshot = self.driver.get_screenshot_as_png()
        allure.attach(screenshot, name=name, attachment_type=allure.attachment_type.PNG)
        with open("Report/{}.png".format(name), "wb") as f:
            f.write(screenshot)
